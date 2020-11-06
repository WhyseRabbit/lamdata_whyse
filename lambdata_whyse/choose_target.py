# Package Imports:
import pandas as pd

def choose_target(self, target_name: str) -> pd.Series:

    """Choose a target from a DataFrame by entering a column name as a string
    and transform it into a pandas Series.

    target_name = name of column as a string; string must be valid column
    name to function properly.

    Returns a pandas Series to be divided by the train_val_test_split function.
    """
    
    return self[target_name]


if __name__ == "__main__":
    """# only use code below if this script
    # not if it is imported from another script"""
    {"yes" : [1, 2, 3, 4 , 5, 6, 7, 8, 9, 10],
    "no" : [True, False, False, False, True, False, True,
    True, False, True],
    "maybe" : [0.5, 1.2, 4.82, 42.0, 5.9, 9.4, 6.9, 7.1, 2.5, 18.2]
    }

    y = choose_target("yes")

    print(y)
