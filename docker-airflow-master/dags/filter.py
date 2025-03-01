# country data which start with letter I


import pandas as pd

def filter_function():
    print("Applying Filter condition to take countries which start with I Letter ")

    df = pd.read_csv("/usr/local/airflow/ip_files/countries_cleaned.csv")

    df = df[df['country'].str.startswith("I")].reset_index(drop=True)

    df.to_csv("/usr/local/airflow/op_files/countries_filtered.csv")