import psycopg2
import configparser
import logging

from utils import get_config


def postgresSQuery(postgresdb, action, sql):
    """
    This function used for single query on postgresql
    action list
    1. "get" -> for get data, ex: select method
    2. "insert" -> for insert or update data

    This function will always updated query method
    """

    dbconf = get_config(postgresdb)

    with psycopg2.connect(**dbconf) as conn:
        with conn.cursor() as cursor:
            logging.info(f"Execute query:\n{sql}")
            try:
                cursor.execute(sql)
                if action == 'get':
                    return cursor.fetchall()
                else:
                    conn.commit()
            except Exception as err:
                logging.info(f"Error execute query: {err}")
                if action == 'insert':
                    conn.rollback()
                raise err
            

sql = "SELECT first_name, last_name FROM test.split_name;"
print(postgresSQuery('postgresdb.study', 'get', sql))