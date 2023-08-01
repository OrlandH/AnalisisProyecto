import pyodbc
import pandas as pd
from sqlalchemy import create_engine
import couchdb

couchdb_url = 'http://admin:admin@localhost:5984/' 
server = couchdb.Server(couchdb_url)

sql_server_name = 'DESKTOP-7KQ1FEP\SQLDEVELOPER' 
sql_database_name = 'ProyectoAnalisis' 


connection_string = f'DRIVER=ODBC Driver 18 for SQL Server;SERVER={sql_server_name};DATABASE={sql_database_name};Trusted_Connection=yes;'

try:

    sql_connection = pyodbc.connect(connection_string)
    print("Conexión con SQL Server exitosa")
except pyodbc.Error as ex:
    print("Error al conectar con SQL Server:")
    print(ex)
    exit()

couchdb_databases = ['comidadesperdiciada', 'conciertos', 'hobb', 'jugadoresfutboldataset', 'mongo_destino2', 'nasa', 'salario']

for db_name in couchdb_databases:
    db = server[db_name]
    rows = [doc for doc in db]
    df = pd.DataFrame(rows)
    
    table_name = db_name
    
    try:

        engine = create_engine(f'mssql+pyodbc://{sql_server_name}/{sql_database_name}?trusted_connection=yes&driver=ODBC+Driver+18+for+SQL+Server')
        
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Datos de la base de datos '{db_name}' migrados con éxito.")
    except Exception as ex:
        print(f"Error al migrar datos de la base de datos '{db_name}':")
        print(ex)

sql_connection.close()
