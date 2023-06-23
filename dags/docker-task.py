from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator


with DAG('docker-dag', start_date=datetime(2022,1,1), schedule_interval='@daily', catchup=False) as dag:
    create_table = PostgresOperator(
        task_id = 'create_table',
        postgres_conn_id= 'postgres',
        sql='''
            CREATE TABLE IF NOT EXISTS test(
                time varchar(255) not null
            );
        '''
    )

    insert_execution_time = PostgresOperator(
        task_id = 'insert_execution_time',
        postgres_conn_id= 'postgres',
        sql="INSERT INTO test (time) VALUES (%s);",
        parameters=[str(datetime.now())],
    )    

    retrive_data = PostgresOperator(
        task_id = 'retrive_data',
        postgres_conn_id= 'postgres',
        sql="select * from test;"
    )    

    create_table >> insert_execution_time >> retrieve_data
