from login.models import get_user_info

def check_user_passwd(user_name, passwd):
    result = {'flag':flag,
              'msg':msg}
    user_info = get_user_info(user_name)
    if user_info:
        if passwd == user_info['password']:
            flag = True
            msg = ''
        else:
            flag = False
            msg = '' 
    else:
        flag = False
        msg = '没有这个人'
    return result
