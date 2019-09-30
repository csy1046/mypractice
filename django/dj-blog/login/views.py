from django.shortcuts import render, render_to_response
from login.verify import check_user_passwd

# Create your views here.


def login(request):
    print(22222)
    if request.method == 'POST':
        #passwd = request.POST.get('password', '')
        #user_name = request.POST.get('user_name', '')
        user_name = 'test'
        passwd = '123456'
        flag = check_user_passwd(user_name, passwd)
        
        
