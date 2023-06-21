# DOCKER ASSIGNMENT

Created a postgres connection with below configurations

![image](https://github.com/shishir474/docker_kubernetes_assignment/assets/57223710/eb5aada9-dff1-451d-ac31-e7493ed0cd03)


- The first task, named "create_table" was created. This task utilizes the Python Operator with PostgresHook, a component that interacts with a Postgres database. The task is responsible for creating a table in the database. The connection to the Postgres database is established using the "postgres_conn_id" parameter, which is set to "postgres".
- The second task, named "insert_execution_time" was created. This task also uses the Python Operator and PostgresHook. Its purpose is to insert values into the table previously created in the database.
- The third task, named "retrieve_data" was created. This task retrieves the data from the table
- Finally, the dependencies between the tasks were established. This means that the tasks were linked in a specific order to ensure they are executed sequentially. For example, "create_table" task must be completed before "insert_execution_time" task. These dependencies ensure that the tasks are executed in the desired sequence to achieve the intended workflow.

<img width="1440" alt="Screenshot 2023-06-19 at 7 00 09 PM" src="https://github.com/shishir474/docker_kubernetes_assignment/assets/57223710/1728032a-6587-496c-9bea-2c1d4f919da4">


 current timestamp inserted successfully into my test table.
 
 <br>
<img width="461" alt="Screenshot 2023-06-19 at 7 01 30 PM" src="https://github.com/shishir474/docker_kubernetes_assignment/assets/57223710/bd8c06fe-5188-442e-afdc-eaf4ac4d615b">

 
 
# KUBERNETES ASSIGNMENT
- Installed minikube. <br>
` brew install minikube ` <br>
`minikube start`

- Created a postgres-deployment.yaml and made a pod using kubectl. <br>
`kubectl apply -f postgres-deployment.yaml`

- Added dependencies of python and airflow in a postgres image by using the following commands inside the postgres pod. <br>
`apt-get -y update`<br>
`apt-get  -y install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget`<br>
`wget https://www.python.org/ftp/python/3.7.12/Python-3.7.12.tgz`
`tar -xf Python-3.7.12.tgz`<br>
`cd /Python-3.7.12`<br>
`./configure --enable-optimizations` <br>
`make -j $(nproc)` <br>
`make altinstall` <br>
`apt-get install libpq-dev` <br>
`pip3.7 install "apache-airflow[postgres]==2.5.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"` <br>
`airflow db init` <br>
`airflow users create -u airflow -p airflow -f arin -l arora -e xyz@gmail.com -r Admin` <br>

- Made a postgres-service.yaml and created a service using <br>
`kubectl apply -f postgres-service.yaml`

- Made a airflow-deployment.yaml and created a deployment using <br>
`kubectl apply -f airflow-deployment.yaml`

- Made a airflow-service.yaml and created a service using <br>
`kubectl apply -f airflow-service.yaml`

- Created a DAG and postgres connection and ran it to get the entries in a postgres table.
  ![image](https://github.com/shishir474/docker_kubernetes_assignment/assets/57223710/35983016-3bba-4b25-889a-db03ff4bc6c1)

- Results in table : <br>
<img width="398" alt="Screenshot 2023-06-19 at 7 05 51 PM" src="https://github.com/shishir474/docker_kubernetes_assignment/assets/57223710/28f44580-e613-49cf-8489-26bdfbc059e9">

