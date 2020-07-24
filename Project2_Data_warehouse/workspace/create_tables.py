import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
        Drop tables if been created before
    """
    for query in drop_table_queries:
        try:
            cur.execute(query)
            conn.commit()
            print("Executed query: {}".format(query))
        except Exception as e:
            print(e)
        
    print("###")


def create_tables(cur, conn):
    """
        Create tables for staging and creating the star schema
    """
    for query in create_table_queries:
        try:
            cur.execute(query)
            conn.commit()
            print("Executed query {}".format(query))
        except Exception as e:
            print(e)
        
    print("###")


def main():
    """
    Get the necessary credentials from config file, retrieve cluster.
    Tables will be dropped (if exist) and created. 
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()