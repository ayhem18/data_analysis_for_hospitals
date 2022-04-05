from multipledispatch import dispatch
import pandas as pd

pd.set_option('display.max_columns', 8)

general = 'test/general.csv'
prenatal = 'test/prenatal.csv'
sports = 'test/sports.csv'
lines_display = 20

if __name__ == '__main__':
    general_df = pd.read_csv(general)
    prenatal_df = pd.read_csv(prenatal)
    sports_df = pd.read_csv(sports)

    print(general_df.head(lines_display))

    print(prenatal_df.head(lines_display))

    print(sports_df.head(lines_display))
