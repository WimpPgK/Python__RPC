import rpyc
from rpyc.utils.server import ThreadedServer


class MonitorService(rpyc.Service):

    #funkcja wywoluje sie podczas nawiazywania polaczenia
    def on_connect(self, conn):
        print("Nawiazano polaczenie")

    #funkcja wywoluje sie podczas zakonczenia polaczenia
    def on_disconnect(self, conn):
        print("Zerwano polaczenie")


    def exposed_run_fibonacci(self, n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            pom2 = 1;
            result = 1;

            for i in range(n-2):
                pom1 = result
                result = pom1 + pom2;
                pom2 = pom1;

            return result;




if __name__ == '__main__':
    t = ThreadedServer(MonitorService, port = 19961, protocol_config={'allow_public_attrs': True})
    t.start()

