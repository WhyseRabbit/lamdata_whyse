import pandas as pd

def choose_target(self, target_name: str) -> pd.Series:
    """Choose a target from a DataFrame and transform it into a pandas Series."""
    return self[target_name]


if __name__ == "__main__":
#    mydf = DF({
#        "no" : (1, 2, 3),
#        "yes" : (4, 5, 6)
#        })
#    print(mydf.choose_target("yes"))
    breakpoint()

