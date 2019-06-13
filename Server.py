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
        try:
            val = int(n)
            if val % 1 != 0 or val < 0:
                raise ValueError()

            p = subprocess.Popen(["python", self.filename, str(n)], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT)
            p.wait()
            print(p.returncode)
            if p.returncode == 1 and val !=2 and val !=0:
                raise Exception

        except ValueError:
            er_comment = "Wprowadzono niepoprawna wartosc, sprobuj ponownie."
            return er_comment

        except Exception:
            er_comment = "Blad w programie obliczajacym ciag Fib"
            return er_comment

        else:
            fib = subprocess.call("python " + self.filename + ' ' + str(n))
            return str(fib) + " - program zadzialal poprawnie"




if __name__ == '__main__':
    t = ThreadedServer(MonitorService, port = 19961, protocol_config={'allow_public_attrs': True})
    t.start()

