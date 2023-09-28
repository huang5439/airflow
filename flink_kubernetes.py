from airflow import DAG
from airflow.providers.apache.flink.operators.flink_kubernetes import FlinkKubernetesOperator
from datetime import datetime

# Define your DAG
dag = DAG(
    'submit_flink_job',
    default_args={
        'owner': 'airflow',
        'start_date': datetime(2023, 1, 1),  # Modify this to your desired start date
    },
    schedule_interval=None,  # You can set a schedule interval if needed
    catchup=False,
)

# Define your Flink Kubernetes Operator
flink_operator = FlinkKubernetesOperator(
    task_id='submit_flink_job_task',
    namespace='flink-job',
    application_file='basic2.yaml',  # Path to your Flink job YAML file
    kubernetes_conn_id='your_k8s_conn_id',  # Connection ID to your Kubernetes cluster
    do_xcom_push=True,
    dag=dag,
)
