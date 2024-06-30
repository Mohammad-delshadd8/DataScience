from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from Businsess_Logic_Layer.Login_BLL_Module import Login_BLL_Class


def Login_btn_cmd():
    UserName = txtUserName.get()
    Password = txtPassword.get()
    login_BLL_Object = Login_BLL_Class()
    result = login_BLL_Object.loginCheck(UserName,Password)

    for widget in LoginForm.winfo_children():
        if isinstance(widget, ttk.Entry):
            widget.delete(0, END)

    if len(result) == 1:
        LoginForm.destroy()
        from User_Interface_Layer.MenuForm_UI_Module import MenuForm_UI_Calass
        from Model_Layer.User_Model_Module import user_model_class
        user_object = user_model_class(userName=result[0][0], password=result[0][1], firstName=result[0][2], lastName=result[0][3], isAdmin=result[0][4])
        MenuForm_UI_Object = MenuForm_UI_Calass()
        MenuForm_UI_Object.MenuForm_UI_Load(user_object)
        #msg.showinfo(title="Done", message=f"Welcome {result[0][2]} {result[0][3]}")

    else:
        msg.showwarning(title="Failed", message="Invalid Username or Password")





LoginForm = Tk()
LoginForm.title("Menu")
LoginForm.geometry('400x150')
LoginForm.resizable(0, 0)
LoginForm.iconbitmap("icons/menu.ico")
x_Login = int(LoginForm.winfo_screenwidth() / 2 - 400 / 2)
y_Login = int(LoginForm.winfo_screenheight() / 2 - 150 / 2)
LoginForm.geometry("+{}+{}".format(x_Login, y_Login))

txtUserName= StringVar()
lblUserName = Label(LoginForm, text="User Name: ")
lblUserName.grid(row=0, column=0, padx=10, pady=10, sticky='w')
entUserName = ttk.Entry(LoginForm, width=30, textvariable=txtUserName)
entUserName.grid(row=0, column=1, padx=10, pady=10, sticky='w')

txtPassword= StringVar()
lblPassword = Label(LoginForm, text="Password: ")
lblPassword.grid(row=1, column=0, padx=10, pady=10, sticky='w')
entPassword = ttk.Entry(LoginForm, width=30, textvariable=txtPassword)
entPassword.grid(row=1, column=1, padx=10, pady=10, sticky='w')

btnLogin = ttk.Button(LoginForm, text="Login", width=20, command=Login_btn_cmd)
btnLogin.grid(row=3, column=0, padx=10, pady=20, sticky='w')

LoginForm.mainloop()