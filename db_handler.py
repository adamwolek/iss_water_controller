from datetime import time

import psycopg2

class DBHandler:


    def save_to_db(self, water_leveL, set_level):
        # print ("Starting " + self.name)
        # self.execute()
        # print ("Exiting " + self.name)
        # self.connect()

        """ Connect to the PostgreSQL database server """
        params = psycopg2.connect(
            host="192.168.0.120",
            port="49153",
            database="postgres",
            user="postgres",
            password="ooL9aif2cooZa5da")
        try:
            # read connection parameters
            # params = config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)

            # create a cursor
            cur = conn.cursor()

            # execute a statement
            # print('PostgreSQL database version:')
            sql = "INSERT INTO water_data (water_level, set_level, time) "
            cur.execute(sql, (water_leveL, set_level, time.time()))

            # display the PostgreSQL database server version
            id = cur.fetchone()[0]
            print(id)

            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')


