from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'main/index.html')

def login_index(request):
    if request.method == 'POST':
        account = request.POST.get('account')

        if account == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')

            userObject = authenticate(username = username, password = password)

            if userObject is not None:

                login(request, userObject)

            
            else:
                print('fail')

        else:
            return redirect('users:JoinUrl')
    else:
        pass

    return render(request, 'user/login.html', { })

def logout_index(request):
    logout(request)
    return redirect('users:LoginUrl')

def join_index(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        print(account)

        if account == 'create':
            new_username = request.POST.get('username')
            new_password = request.POST.get('password')
            new_password_check = request.POST.get('password_check')
            print(new_username)
            print(new_password)

            if not new_username or not new_password:
                return render(request, 'user/join.html', {'error_msg' : '아이디 또는 비밀번호를 입력하세요.'})
            
            elif new_password != new_password_check:
                return render(request, 'user/join.html', {'error_msg':'비밀번호가 서로 같지 않습니다.'})
            
            elif User.objects.filter(username=new_username).exists():
                return render(request, 'user/join.html', {'error_msg':'이미 사용중인 아이디입니다.'})
            
            new_users = User.objects.create_user(username=new_username, password=new_password)
            new_users.save()
            
        
        else:
            pass

        return redirect('users:LoginUrl')

    return render(request, 'user/join.html', {})
                
        