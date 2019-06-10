import rpyc
from rpyc.utils.server import ThreadedServer
import subprocess

class MonitorService(rpyc.Service):

    filename = 'test.py'

    #funkcja wywoluje sie podczas nawiazywania polaczenia
    def on_connect(self, conn):
        print("Nawiazano polaczenie")

    #funkcja wywoluje sie podczas zakonczenia polaczenia
    def on_disconnect(self, conn):
        print("Zerwano polaczenie")


    def exposed_save_code(self, code : list):
        file = open(self.filename, 'w')
        file.truncate()
        for line in code:
            file.write(line)
        file.close()
        return True


    #funkcja wywolujaca kod zaposany w pliku test.py
    def exposed_execute_code(self, n : int):
        fib = subprocess.call("python "+self.filename + ' ' + str(n))
        return int(fib)


if __name__ == '__main__':
    t = ThreadedServer(MonitorService, port = 19961, protocol_config={'allow_public_attrs': True})
    t.start()

