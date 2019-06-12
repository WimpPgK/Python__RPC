import unittest
from module_4_client import module_3_client

class TestClient(unittest.TestCase):

    def test_client(self):
        client = module_3_client()

if __name__ == '__main__':
    unittest.main()
