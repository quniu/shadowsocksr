import unittest
from utils.net_util import  *

class MyTestCase(unittest.TestCase):
    def test_from_map_ipv6_get_ipv4(self):
        self.assertEqual("192.168.204.1", from_map_ipv6_get_ipv4("0:0:0:0:0:ffff:192.168.204.1"))


if __name__ == '__main__':
    unittest.main()
