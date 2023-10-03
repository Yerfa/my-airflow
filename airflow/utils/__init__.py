import configparser
import logging
import json


def get_config(conf):
    try:
        config = configparser.ConfigParser()
        config.read('configurationFile.ini')

        conf_values = dict(config.items(conf))
        
        return conf_values
    except Exception as err:
        logging.info("Error get config:", err)
        raise err