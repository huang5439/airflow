from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Define your DAG with a unique ID and a default_args dictionary
dag_id = 'simple_airflow_eks_test'
default_args = {
    'owner': 'jim',
    'start_date': datetime(2023, 9, 28),
    'depends_on_past': False,
    'retries': 1,
}

dag = DAG(
    dag_id=dag_id,
    default_args=default_args,
    schedule_interval=None,  # Set to None to trigger manually
    catchup=False,  # Set to False to ignore historic runs
)

# Define a simple task
start_task = DummyOperator(task_id='start', dag=dag)

def print_hello():
    print("Hello from the Airflow task!")

hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=print_hello,
    dag=dag,
)

# Define the task dependencies
start_task >> hello_task
