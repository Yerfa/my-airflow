import configparser
import logging
import json
import os

airflow_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def get_config(conf):
    try:
        config = configparser.ConfigParser()
        config.read(f'{airflow_path}/conf/airflowconf.ini')

        conf_values = dict(config.items(conf))
        
        return conf_values
    except Exception as err:
        logging.info("Error get config:", err)
        raise err