import pandas as pd

def load_data(eng):
    df = pd.read_csv('./Northwind_database_csv/customers.csv')
    df.to_sql('customers', con=eng)
    return "Data Uploaded"

