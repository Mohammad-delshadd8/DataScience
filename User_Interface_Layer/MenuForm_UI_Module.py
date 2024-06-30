from tkinter import *
from tkinter import ttk
from Model_Layer.User_Model_Module import user_model_class




class MenuForm_UI_Calass:
    def MenuForm_UI_Load(self,user_object:user_model_class):
        menuForm = Tk()
        menuForm.title("Menu")
        menuForm.geometry('650x120')
        menuForm.resizable(0, 0)
        menuForm.iconbitmap("icons/menu.ico")
        x_menu = int(menuForm.winfo_screenwidth() / 2 - 650 / 2)
        y_menu = int(menuForm.winfo_screenheight() / 2 - 120 / 2)
        menuForm.geometry("+{}+{}".format(x_menu, y_menu))

        lblWelcome = Label(menuForm, text=f"Welcome {user_object.FirstName} {user_object.LastName}")
        lblWelcome.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        btnAddBook = ttk.Button(menuForm, text="Add Book", command="AddBook_menu_btn_cmd")
        btnAddBook.grid(row=1, column=0, padx=10, pady=40, sticky='w')

        btnAddEmployee = ttk.Button(menuForm, text="Add Employee", command="AddEmployee_menu_btn_cmd")
        btnAddEmployee.grid(row=1, column=1, padx=10, pady=40, sticky='w')

        btnAddJob = ttk.Button(menuForm, text="Add Job", command="AddJob_menu_btn_cmd")
        btnAddJob.grid(row=1, column=2, padx=10, pady=40, sticky='w')

        btnAddPublisher = ttk.Button(menuForm, text="Add Publisher", command="AddPublisher_menu_btn_cmd")
        btnAddPublisher.grid(row=1, column=3, padx=10, pady=40, sticky='w')

        btnAddStores = ttk.Button(menuForm, text="Add Store", command="AddStores_menu_btn_cmd")
        btnAddStores.grid(row=1, column=4, padx=10, pady=40, sticky='w')

        btnAddSales = ttk.Button(menuForm, text="Add Sales", command="AddSales_menu_btn_cmd")
        btnAddSales.grid(row=1, column=5, padx=10, pady=40, sticky='w')

        menuForm.mainloop()
