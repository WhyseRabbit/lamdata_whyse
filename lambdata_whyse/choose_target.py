# Package Imports:
import pandas as pd

def choose_target(self, df, target_name: str):

    """Choose a target from a DataFrame by entering a column name as a string
    and transform it into a pandas Series.

    target_name = name of column as a string; string must be valid column
    name to function properly.

    Returns a pandas Series to be divided by the train_val_test_split function.
    """
    
    return self.df[target_name]
