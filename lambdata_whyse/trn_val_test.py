# Package Imports:
import pandas as pd
from sklearn.model_selection import train_test_split
# Local Imports:
from .choose_target import choose_target


def train_val_test_split(self, df, features,
                         train_size=0.7, val_size=0.1,
                         test_size=0.2, random_state=None,
                         shuffle=True):

    """
    This is meant to be used with the choose_target function; it effectively
    splits a DataFrame into 3 different pandas DataFrames and 3 pandas Series.
    It derives from sklearn.model_selection.train_test_split.

    df (no default) = pandas DataFrame used in the model.
    X (no default) = features to be used in this model.
    y (default = choose_target()) = choose_target, a string you feed the function related to the data.
    train_size (int or float; default = 0.7) = Choose ratio or number of lines
    within training model.
    val_size (int or float; default = 0.1) = Choose ratio or number of lines within
    validation model.
    test_size (int or float; default = 0.2) = Choose ratio or number of lines within
    testing model.
    random_state (int; no default value): Controls the reproducible shuffling done to the models.
    shuffle (bool; default = True): Whether or not to shuffle the data before split.

    Returns:
        Training, validation, and testing DataFrames for X;
        training, validation, and testing Series for y.
    """

    X = df[features]
    y = choose_target


    X_train_val, X_test, y_train_val, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state, shuffle=shuffle
            )


    X_train, X_val, y_train, y_val = train_test_split(
            X_train_val, y_train_val, test_size=val_size / (train_size + val_size),
            random_state=random_state, shuffle=shuffle
            )


    return X_train, X_val, X_test, y_train, y_val, y_test
