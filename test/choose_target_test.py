import unittest
from .lambdata_whyse import choose_target

df = {
    "yes" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    "no" : [1.45, 2.87, 3.99, 4.37, 5.66, 6.51]
}

class TestChoose_Target(unittest.TestCase):

    def test_ct_function(self):

