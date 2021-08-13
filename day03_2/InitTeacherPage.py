class InitTeacherPage:
    # 成功用例的数据
    login_sucess_data=[
        {"username":"jason","password":"admin","expect":"Teacher manager"}
    ]
    #失败的数据
    login_error_data=[
        {"username":"jason","password":"admin1","expect":"账户名错误或密码错误!别瞎弄!"}
    ]