import pyodbc
from Model_Layer.Employee_Model_Module import Employee_model_class
from DB_connection.DB_Connection_Module import DB_Connection_Calss

class EmployeeCRUD_DAL_Class:
    def Add_Employee(Employee_Object:Employee_model_class):
        connection_Object = DB_Connection_Calss()
        connectionString = connection_Object.DB_Connection()
        commandText = 'EXEC [pubs_Delshad].[dbo].[AddEmployee] ?,?,?,?,?,?'
        prams = (Employee_Object.EMP_ID, Employee_Object.EMP_FirstName,
                 Employee_Object.EMP_LastName, Employee_Object.EMP_JobID,
                 Employee_Object.EMP_Publisher, Employee_Object.EMP_HireDate)

        with pyodbc.connect(connectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandText)
            cursor.commit()