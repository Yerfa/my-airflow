from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def my_python_function():
    print("Hello, Airflow!")


# ========== DAG ========== #
with DAG(
    dag_id='hello_world_dag',
    start_date=datetime(2023, 8, 17),
    schedule_interval=None,  # Untuk menjalankan DAG secara manual, atur intervalnya menjadi None
    catchup=False,
) as dag:

    # Menambahkan tugas ke dalam DAG
    task = PythonOperator(
        task_id='my_task',
        python_callable=my_python_function,
    )

# Tugas lain dapat ditambahkan dengan blok 'with DAG()'.

# Berikan ketergantungan antar tugas jika diperlukan.
# task.set_upstream(another_task)
