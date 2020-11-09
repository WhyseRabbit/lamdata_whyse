import unittest
from .lambdata_whyse import choose_target

df = {
    "yes" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    "no" : [1.45, 2.87, 3.99, 4.37, 5.66, 6.51, 7.81, 8.26, 9.05, 0.07],
    "maybe" : ["cat", "and", "hat", "fish", "dog", "rat", "fork", "win",
    "neat", "lazy"]
}

class TestChoose_Target(unittest.TestCase):

    def ct_test_repr(self):
        df = df
        yes = choose_target(df, "yes")
        self.assertCountEqual(len(yes = 10))


if __name__ == "__main__":
    unittest.main()
