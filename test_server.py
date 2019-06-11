import unittest
from module_4_server import Module3Server

server = Module3Server()

class TestServer(unittest.TestCase):
    def test_create_table(self):
        server.exposed_create_table()

    def test_save_code(self):
        content = ''
        with open('code.txt', 'r') as file:
            content = file.readlines()

        server.exposed_save_code(content)

    def test_execute_code(self):
        server.exposed_execute_code(8)

    def test_compare_code(self):
        server.exposed_compare_code(11)

if __name__ == '__main__':
    unittest.main()