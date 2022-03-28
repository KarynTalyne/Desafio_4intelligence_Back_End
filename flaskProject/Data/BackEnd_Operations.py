import pandas as pd
import os.path


def verify_csv():
    if (not (os.path.isfile('Data.csv'))):
        create_csv()


def create_csv():
    COLUNAS = ['id', 'name', 'company', 'created_at', 'amount_products']
    Data = pd.DataFrame(columns=COLUNAS)
    Data.to_csv('Data.csv')

def clear_csv( ):
    create_csv()

def update_csv(Data_modified):
    Data_modified.to_csv('Data.csv')

def view_all():
    verify_csv()
    Data_read = pd.read_csv('Data.csv', index_col=[0])
    return Data_read

class CRUD:

    def create_data(r_id, r_name, r_company, r_created_at, r_amount_products):
        verify_csv()
        Data_read = pd.read_csv('Data.csv', index_col=[0])
        new_row = (r_id, r_name, r_company, str(r_created_at), str(r_amount_products))
        dfNew = pd.DataFrame([new_row], columns=['id', 'name', 'company', 'created_at', 'amount_products'])
        aux = pd.concat([Data_read, dfNew])
        update_csv(aux)

    def read_specific_data(r_name, r_company):
        verify_csv()
        Data_read = pd.read_csv('Data.csv', index_col=[0])
        Data_aux = Data_read[(Data_read["name"].str.contains(r_name)) &
                             (Data_read["company"].str.contains(r_company))]
        return Data_aux

    def delete_data(r_id):
        verify_csv()
        Data_read = pd.read_csv('Data.csv', index_col=[0])
        df_remove = Data_read.loc[(Data_read['id'] != r_id)]
        update_csv(df_remove)


