import pendulum
import logging

from airflow import DAG, Dataset
from airflow.operators.python import PythonOperator
from datetime import timedelta
from db_access.postgresql_access import postgresSQuery

"""
Notes

This DAG is not efficient, it's just an example
"""

def get_data_full_name():
    sql = """
        SELECT name FROM test.fullname;
    """
    return postgresSQuery('postgresdb.study', 'get', sql)


def insert_data_split(data_full_name):
    split_name_list = []
    for data in data_full_name:
        if " " in data[0]:
            split_name = data[0].replace("'", "''").split(" ")
            first_name = split_name[0]
            last_name = " ".join(split_name[1:])
            split_name_list.append(f"('{first_name}', '{last_name}')")
        else:
            data = data[0].replace("'", "''")
            split_name_list.append(f"('{data}', '')")
    
    sql = f"""
        INSERT INTO test.split_name(first_name, last_name)
        VALUES
        {",".join(split_name_list)}
        ON CONFLICT (first_name, last_name) DO NOTHING;
    """
    postgresSQuery('postgresdb.study', 'insert', sql)


def run_task():
    data_full_name = get_data_full_name()
    insert_data_split(data_full_name)



# ========== DAG ========== #
with DAG(
    dag_id="hourly_process_data_name",
    description="Split Full Name",
    default_args= {
        "owner": "Muhmmad Audri I",
        "email": ["marimo8696@gmail.com"],
        "email_on_failure": True,
        "retries": 1,
        "retry_delay": timedelta(minutes=2),
        "schedule_interval": "@hourly",
    },
    catchup=False,
    start_date=pendulum.datetime(2023, 10, 1, tz="UTC"),
    schedule_interval='@hourly',
    tags=["postgresql"],
) as dag:
    PythonOperator(
        task_id='Operator1',
        python_callable=run_task,
        dag=dag,
        op_args={},
    )