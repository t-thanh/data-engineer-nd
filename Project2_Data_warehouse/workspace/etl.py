import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """ Load data from S3 into staging tables
    """
    print("=== Loading data from S3 into staging tables...")
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()
        print ("Loading ...")


def insert_tables(cur, conn):
    """ Insert staging data into main tables.
    """
    print("=== Inserting staging data into main tables...")
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()
        print ("Inserting ...")
        
def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    print ("Loading successed!")
    insert_tables(cur, conn)
    print ("Inserting successed!")

    conn.close()
    print("Finished!")


if __name__ == "__main__":
    main()