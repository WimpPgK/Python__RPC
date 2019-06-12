from rpyc import Service
from rpyc.utils.server import ThreadedServer
import subprocess
from dbmanager import DbManager
import difflib
import threading

class Module4Server(Service):

    filename = 'test.py'
    db = DbManager('localhost', 'root', '', 'testowa')
    message_for_client = ''
    client_program_id = 0
    db_thread = threading.Thread()

    def exposed_create_table(self):
        self.db = DbManager('localhost', 'root', '', 'testowa')
        self.db.executesql("CREATE TABLE IF NOT EXISTS programs (id integer PRIMARY KEY AUTO_INCREMENT, program_name VARCHAR(128) NOT NULL, code_text VARCHAR(4096) NOT NULL, date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        self.db.executesql("CREATE TABLE IF NOT EXISTS programs_diffs (id integer PRIMARY KEY AUTO_INCREMENT, program1_id integer NOT NULL, program2_id integer NOT NULL, similarity float NOT NULL DEFAULT 0, diff VARCHAR(4096) NULL)")

    def exposed_save_code(self, code : list):
        file = open(self.filename, 'w')
        file.truncate()
        code_text = ''
        for line in code:
            file.write(line)
            code_text += line

        self.db_thread = threading.Thread(target=self.save_into_db, args=(code_text,))
        self.db_thread.start()
        
        file.close()
        return

    def save_into_db(self, code : str):
        sql = "INSERT INTO programs (program_name, code_text) VALUES (\'" + self.filename + "\',\'" + code + "\')"
        self.db.executesql(sql)
        self.db.commit_changes()
        self.client_program_id = self.db.cursor.lastrowid
        return self.client_program_id

    def exposed_execute_code(self, n : int):
        fib = subprocess.call("python "+self.filename + ' ' + str(n))
        return int(fib)

    def exposed_compare_code(self, n : int):
        sql = "SELECT * FROM programs"
        self.db.executesql(sql)
        rows = self.db.get_result()
        row = next((x for x in rows if x['id'] == n), None)
        if row == None:
            return 
        code = str(row['code_text'])
        message = ''
        new_id_text = '=========\nID = '
        sim = 'Similarity = '
        for r in rows:
            r_id = int(r['id'])
            if r_id == n:
                continue
            
            code2 = str(r['code_text'])
            c1 = code.splitlines(False)
            c2 = code2.splitlines(False)
            diff = difflib.unified_diff(c1, c2)
            match = difflib.SequenceMatcher(None, code, code2)
            m = match.ratio()
            str_diff = ''
            sql = ''
            temp_text = new_id_text+str(r['id'])+'\n'
            message += temp_text
            temp_text = sim+str(m)+'\n'
            message += temp_text
            for line in diff:
                str_diff += line
                message += line+'\n'
            sql = "INSERT INTO programs_diffs (program1_id, program2_id, similarity, diff) VALUES ("+str(n)+","+str(r_id)+","+str(m)+",\'"+str_diff+"\')"
            self.db.executesql(sql)
            self.db.commit_changes()
        self.message_for_client = message
        
    def exposed_get_message(self):
        return self.message_for_client

    def exposed_get_program_id(self):
        if self.db_thread.is_alive:
            self.db_thread.join()
        return  self.client_program_id

if __name__ == '__main__':
    s = ThreadedServer(Module4Server, hostname='localhost', port=18871, protocol_config={"allow_public_attrs" : True})
    s.start()
    