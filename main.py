import pandas as pd

pd.set_option('display.max_columns', 8)

general = 'test/general.csv'
prenatal = 'test/prenatal.csv'
sports = 'test/sports.csv'
lines_display = 20
random_state_value = 30

if __name__ == '__main__':
    general_df = pd.read_csv(general)
    prenatal_df = pd.read_csv(prenatal)
    sports_df = pd.read_csv(sports)

    # the column names in all dataframes should match
    prenatal_df.columns = general_df.columns
    sports_df.columns = general_df.columns

    # merge all the dataframes into one large dataframe
    hospitals = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)

    # delete the first column '
    hospitals.drop(columns=hospitals.columns[0], inplace=True)

    print(hospitals.sample(n=lines_display, random_state=random_state_value))
