from importlib_resources import files

from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator


# Import custom functions
from clean import pre_process
from filter import filter_function

# DAG Default Arguments
default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 2, 14),
    "retries": 2,
    "retry_delay": timedelta(seconds=15),
}

# Define DAG
with DAG(dag_id="test_dag", default_args=default_args, schedule_interval="@daily") as dag:

    # Task 1 - Check file
    check_file = BashOperator(
        task_id="check_file",
        bash_command="shasum /usr/local/airflow/ip_files/countries.csv",
    )

    # Task 2 - Pre-process
    pre_process_task = PythonOperator(  # Renamed to avoid conflicts
        task_id="pre_process",
        python_callable=pre_process,
    )

    # Task 3 - Filter data
    filter_task = PythonOperator(
        task_id="filter_data",
        python_callable=filter_function,
    )

    # Task 4 - send Email
    email = EmailOperator(
        task_id = 'send_email',
        to='charansainettam@gmail.com',
        subject='Daily report Generated',
        html_content='<h1>Hello, Nettam your report are generated successfully, Thanks !',
        files=['/usr/local/airflow/op_files/countries_filtered.csv'],
        cc=['charansainettam@gmail.com']
    )
    # Define Task Dependencies
    check_file >> pre_process_task >> filter_task >> email
