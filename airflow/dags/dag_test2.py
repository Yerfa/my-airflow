from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Fungsi yang akan dijalankan oleh PythonOperator
def my_python_function():
    print("Hello, Airflow!")

# Mendefinisikan DAG dengan 'with DAG()'
with DAG(
    dag_id='my_dag_with_with',
    start_date=datetime(2023, 8, 17),
    schedule_interval=None,  # Untuk menjalankan DAG secara manual, atur intervalnya menjadi None
    catchup=False,
) as dag:

    # Menambahkan tugas ke dalam DAG
    task = PythonOperator(
        task_id='my_task',
        python_callable=my_python_function,
    )

# Jika Anda ingin menambahkan tugas lain, Anda dapat menambahkannya dalam blok 'with DAG()'.

# Berikan ketergantungan antar tugas jika diperlukan.
# task.set_upstream(another_task)
