# Jasveen Singh Kohli

## Docker Assignment
- He created a docker compose file with airflow:2.5.2 as the airflow image.
- He used a Celery executor.
- He also mounted dags folder inside the airflow container to a dags folder in his local system.
- In writing the DAG code, he used PostgresOperator to create the table and insert values into it. Here he loaded queries from some previously made SQL files.
- Finally, he used a BashOperator to log into postgres database and see the values in the table created.


## Kubernetes Assignment
- He created values.yaml file to provide values to postgres and airflow deployment.
- For postgres he setup password, user and database name in values.yaml.
- For airflow he setup webserver access port and AIRFLOW__CORE__SQL_ALCHEMY_CONN.
- He made a postgres pod by using its helm chart and gave values through his custom values.yaml.
- He made an airflow pod by using its helm chart and gave values through his custom values.yaml.
- He created an airflow-service.yaml file with service type load balancer to access webserver UI from local system.


# Aswat Singh Bisht

## Docker Assignment
- He created a Docker containers for Airflow and its components.
- He used a Dockerfile to install psycopg2 in all the containers.
- He created a DAG (Directed Acyclic Graph) with two tasks:
  - Task 1: Create a table that stores the execution date.
  - Task 2: Insert data into the table.
- He extracted the execution date using **kwargs**.

## Kubernetes Assignment
- He used the Postgres helm chart from the Bitnami repository.
- He installed the Postgres container using the helm chart and set the password to "postgres".
- He built Python and instaledl Airflow in the Postgres container.
- Hed installed Airflow version 2.5.0 with Postgres support.
- He initialized the Postgres container as Airflow's database.
- He set the environment variable AIRFLOW__DATABASE__SQL_ALCHEMY_CONN to the Postgres connection string to enable connection between the two.
- He initialized Airflow's database using the command inside the postgres container.
- He created an Airflow deployment and service, and used the Postgres service.
- He applied the Airflow deployment and service configuration from the airflow.yaml file using the command
- He added the DAG file to the Airflow scheduler.
