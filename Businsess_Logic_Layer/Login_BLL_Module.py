from Data_Access_Layer.Login_DAL_module import Login_DAL_Class
class Login_BLL_Class:
    def loginCheck(self,Username,Password):
        Login_DAL_Object = Login_DAL_Class()
        return Login_DAL_Object.loginCheck(Username,Password)
