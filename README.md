# my-airflow-env
Trying to create my airflow

## How To Install Airflow
- Install requirement
- Install broker and SQL database
- Set installed broker and SQL database to airflow.cfg
- Run in daemon mode if airflow's logs not important. If want to see airflow's logs, run them in different terminal
```
airflow celery worker
airflow webserver -p 8081
airflow scheduler
```