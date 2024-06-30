import pyodbc
from DB_connection.DB_Connection_Module import DB_Connection_Calss
class Login_DAL_Class:

    def loginCheck(self, username:str, password:str):
        connection_Object = DB_Connection_Calss()
        connectionString = connection_Object.DB_Connection()
        commandText = 'EXEC [pubs_Delshad].[dbo].[CheckLogin] ?,?'
        params = (username, password)
        with pyodbc.connect(connectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandText, params)
            rows = cursor.fetchall()
            #print(rows)
            return rows

#Login_DAL_Class().loginCheck(username="m", password="0")
