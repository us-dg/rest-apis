import pandas as pd

def database_init(engine):

    # Importing Tables from the csv files
    categories = pd.read_csv('./Northwind_database_csv/categories.csv')
    customers = pd.read_csv('./Northwind_database_csv/customers.csv')
    employees = pd.read_csv('./Northwind_database_csv/employees.csv')
    employee_territories = pd.read_csv('./Northwind_database_csv/employee-territories.csv')
    order_details = pd.read_csv('./Northwind_database_csv/order-details.csv')
    orders = pd.read_csv('./Northwind_database_csv/orders.csv')
    products = pd.read_csv('./Northwind_database_csv/products.csv')
    regions = pd.read_csv('./Northwind_database_csv/regions.csv')
    shippers = pd.read_csv('./Northwind_database_csv/shippers.csv')
    suppliers = pd.read_csv('./Northwind_database_csv/suppliers.csv')
    territories = pd.read_csv('./Northwind_database_csv/territories.csv')

    # Creating the tables from dataframe
    categories.to_sql('categories', con=engine, index=False)
    customers.to_sql('customers', con=engine, index=False)
    employees.to_sql('employees', con=engine, index=False)
    employee_territories.to_sql('employee_territories', con=engine, index=False)
    order_details.to_sql('order_details', con=engine, index=False)
    orders.to_sql('orders', con=engine, index=False)
    products.to_sql('products', con=engine, index=False)
    regions.to_sql('regions', con=engine, index=False)
    shippers.to_sql('shippers', con=engine, index=False)
    suppliers.to_sql('suppliers', con=engine, index=False)
    territories.to_sql('territories', con=engine, index=False)

    print('All of the tables have been successfully created ')
