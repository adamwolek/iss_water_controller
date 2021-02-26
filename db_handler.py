import time

import psycopg2

class DBHandler:


    def save_to_db(self, water_level, set_level):
        # print ("Starting " + self.name)
        # self.execute()
        # print ("Exiting " + self.name)
        # self.connect()
        conn = None
        """ Connect to the PostgreSQL database server """

        try:
            # read connection parameters
            # params = config()
            conn = psycopg2.connect(
                host="192.168.0.120",
                port="49153",
                database="iss",
                user="postgres",
                password="ooL9aif2cooZa5da")

            # connect to the PostgreSQL server
            #print('Connecting to the PostgreSQL database...')
            #conn = psycopg2.connect(params)

            # create a cursor
            cur = conn.cursor()

            # execute a statement
            # print('PostgreSQL database version:')
            sql = "INSERT INTO water_data (water_level, set_level) VALUES(%s,%s)"
            cur.execute(sql, (str(water_level), str(set_level)))
            conn.commit()
            # display the PostgreSQL database server version

            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: " + str(error))
        finally:
            if conn is not None:
                conn.close()

