import unittest
from module_4_client import module_4_client

class TestClient(unittest.TestCase):

    def test_client_with_q(self):
        client = module_4_client(True, 'q')

    def test_client_with_wrong_value(self):
        client = module_4_client(True, '-1')

    def test_client_working(self):
        client = module_4_client(True, '10')

if __name__ == '__main__':
    unittest.main()
