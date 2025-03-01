from operator import index

import pandas as pd
import datetime


def pre_process():
    print("Before adding date column")

    df = pd.read_csv("/usr/local/airflow/ip_files/countries.csv")

    df['process_date'] = datetime.date.today()

    df = df.fillna("empty_string")

    df.to_csv("/usr/local/airflow/ip_files/countries_cleaned.csv",index=False)

    print("File is cleaned and date is added in file ")





