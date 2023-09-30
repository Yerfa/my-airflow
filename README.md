# my-airflow-env
Trying to create my local airflow without Docker

## How To Install Airflow
- Install requirement
- Install broker and SQL database
- Create folder "airflow" in an environment and set it path as "AIRFLOW_HOME"
- Run at environment terminal in "airflow" folder path
```
airflow db init
```
- Set configuration as needed
- Set installed broker and SQL database in airflow.cfg
- Create folder dags and linked that path in airflow.cfg
- Create airflow's user
- Run in daemon mode if airflow's logs not important. If want to see airflow's logs, run them in different terminal
```
airflow celery worker
airflow webserver -p 8081
airflow scheduler
```
- Try run any example job, if success then airflow ready