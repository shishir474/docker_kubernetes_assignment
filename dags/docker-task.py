from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator

#scheduled the dag to run every day at 8AM
with DAG('docker-dag', start_date=datetime(2022,1,1), schedule_interval='0 8 * * *', catchup=False) as dag:
    #task to create table
    create_table = PostgresOperator(
        task_id = 'create_table',
        postgres_conn_id= 'postgres',
        sql='''
            CREATE TABLE IF NOT EXISTS test(
                time varchar(255) not null
            );
        '''
    )

    #task to insert dag execution time
    insert_execution_time = PostgresOperator(
        task_id = 'insert_execution_time',
        postgres_conn_id= 'postgres',
        sql="INSERT INTO test (time) VALUES (%s);",
        parameters=[str(datetime.now())],
    )    

    #task to retrive values
    retrive_data = PostgresOperator(
        task_id = 'retrive_data',
        postgres_conn_id= 'postgres',
        sql="select * from test;"
    )    

<<<<<<< HEAD
    create_table >> insert_execution_time >> retrieve_data
=======
    create_table >> insert_execution_time >> retrive_data
>>>>>>> 1e557f0 (add secrets)
