import pandas as pd

pd.set_option('display.max_columns', 8)

general = 'test/general.csv'
prenatal = 'test/prenatal.csv'
sports = 'test/sports.csv'
lines_display = 20
random_state_value = 30


def stage2_implementation():
    general_df = pd.read_csv(general)
    prenatal_df = pd.read_csv(prenatal)
    sports_df = pd.read_csv(sports)

    # the column names in all dataframes should match
    prenatal_df.columns = general_df.columns
    sports_df.columns = general_df.columns

    # merge all the dataframes into one large dataframe
    hospitals = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)

    # delete the first column
    hospitals.drop(columns=hospitals.columns[0], inplace=True)

    return hospitals


gender_mapper = {'female': 'f', 'male': 'm', 'woman': 'f', 'man': 'm'}
gender = 'gender'
hospital_type = 'hospital'
zero_columns = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']


def stage3_implementation():
    hospitals = stage2_implementation()
    # delete all the empty rows
    hospitals.dropna(axis='index', how='all', inplace=True)

    # unify the genders
    hospitals.loc[:, gender] = [gender_mapper[g] if g in gender_mapper else g for g in hospitals[gender]]

    # replace the Nan values with f in the prenatal hospital
    hospitals[gender] = hospitals.groupby(hospital_type)[gender].apply(lambda x: x.fillna('f'))

    # print(hospitals.loc[hospitals.hospital == 'prenatal', ['hospital', 'gender']])
    # print("####################################")
    # replace the Nan values with 0 in the corresponding columns
    hospitals[zero_columns] = hospitals[zero_columns].fillna(0)

    # print the shape of the dataframe
    print(hospitals.shape)

    print(hospitals.sample(n=lines_display, random_state=random_state_value))


if __name__ == '__main__':
    stage3_implementation()
