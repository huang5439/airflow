from airflow import DAG
from airflow.providers.apache.flink.operators.flink_kubernetes import FlinkKubernetesOperator
from datetime import datetime

# Define your DAG
dag = DAG(
    'submit_flink_job',
    start_date=datetime(2023, 9, 26),
    schedule_interval=None,  # You can set a schedule interval if needed
    catchup=False,
)

# Define your Flink Kubernetes Operator
flink_operator = FlinkKubernetesOperator(
    task_id='submit_flink_job_task',
    namespace='flink-job',
    application_file='basic.yaml',  # Path to your Flink job YAML file
    do_xcom_push=True,
    dag=dag,
)
