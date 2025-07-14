from config import db_url
from csv import QUOTE_NONE
from sqlmodel import create_engine, Session
from sqlalchemy import Engine
from models import *
import pandas as pd

class DataLoader:
    def __init__(self):
        self.engine: Engine = create_engine(db_url)
        self.data_control_register: DataControl = DataControl(status='ON')

    def load(self, file_path: str) -> bool:
        filename = file_path.split('/')[1]
        print(f'Loading file {filename} to the database...')

        with Session(self.engine) as session:
            model_class: SQLModel = file_class_map[filename]
            rows_uploaded = 0
            try:
                for chunk in pd.read_csv(file_path, sep='\t', chunksize=20000, quoting=QUOTE_NONE, engine='python'):
                    chunk.replace('\\N', None, inplace=True)
                    read_rows: list = [model_class(**row) for row in chunk.to_dict(orient='records')]
                    session.add_all(read_rows)
                    session.commit()
                    rows_uploaded += len(chunk)
                    print(f'{rows_uploaded} rows uploaded.')
                print(f'File {filename} successfully loaded!')
            
            except Exception as e:
                session.rollback()
                print(e)
                self.update_data_control('KO')
                return False

        return True

    def staging_to_production(self):
        print('Moving data from staging to productive tables...')
        for table_name in [class_.__name__.lower() for class_ in file_class_map.values()]:
            with self.engine.begin() as conn:
                conn.exec_driver_sql(f"DROP TABLE IF EXISTS pro_{table_name}")
                conn.exec_driver_sql(f"CREATE TABLE pro_{table_name} (LIKE {table_name} INCLUDING ALL)")
                conn.exec_driver_sql(f"INSERT INTO pro_{table_name} SELECT * FROM {table_name}")
                conn.exec_driver_sql(f"DELETE FROM {table_name}")

    def update_data_control(self, status: str):
        with Session(self.engine) as session:
            self.data_control_register.status = status
            session.add(self.data_control_register)
            session.commit()