import mysql.connector
import os
import streamlit as st
from mysql.connector import Error


class MyDB(object):

    def __init__(self, timeout=5000) -> None:

        self.__host = os.environ.get('AWS_RDS_HOST')
        self.__db = 'LendingClub'
        self.__user = os.environ.get('AWS_RDS_LOGIN')
        self.__password = os.environ.get('AWS_RDS_PASS')
        self.__port = 3306

        
        connection = self.mysql_stablish_connection()

        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")
    
    # @st.cache
    def mysql_stablish_connection(self):

        try:
            connection = mysql.connector.connect(
                                                host     = self.__host,
                                                database = self.__db,
                                                user     = self.__user,
                                                password = self.__password,
                                                port     = self.__port
                                                )
            if connection.is_connected():
                db_info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_info)

        except Error as e:
            print("Error while connecting to MySQL Server", e)

        finally:
            return connection

    @st.cache
    def mysql_execute_query(self, query):

        connection = self.mysql_stablish_connection()

        try:
            cursor = connection.cursor()

            cursor.execute(query)

            # Get all records
            records = cursor.fetchall()
        
        except mysql.connector.Error as e:
            print("Error reading data from MySQL table ", e)
        
        finally:
            if connection.is_connected():
                connection.close()
                print("MySQL connection is closed")
            return records
    
