import pandas as pd
from sklearn.model_selection import train_test_split
from .choose_target import choose_target

def t_v_t_split(self, df, features,
                train_size=0.7, val_size=0.1,
                test_size=0.2, random_state=None,
                shuffle=True) -> [pd.DataFrame, pd.DataFrame, pd.DataFrame,
                                  pd.Series, pd.Series, pd.Series]:
    """
    This is meant to be used with the choose_target function; it effectively splits a DataFrame into 3 different
    pandas DataFrames and 3 pandas Series. It derives from sklearn.model_selection.train_test_split.

    df = pandas DataFrame used in the model.
    X = features to be used in this model.
    y = choose_target, a string you feed the function related to the data.
    train_size (int or float) = Choose ratio or number of lines within training model.
    val_size (int or float) = Choose ratio or number of lines within validation model.
    test_size (int or float) = Choose ratio or number of lines within testing model.
    random_state (int): Controls the reproducible shuffling done to the models.
    shuffle (bool): Whether or not to shuffle the data before split.

    Returns:
        Training, validation, and testing DataFrames for X; training, validation, and testing Series for y.
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


if __name__ == "__main__":
#    DF = df({
#        "yes" : (1, 2, 3),
#        "no" : (4, 5, 6),
#        "maybe" : (7, 8, 9)
#         })
#    print(DF.t_v_t_split(DF))
    breakpoint()
