from django.shortcuts import render, redirect
from .models import User
from .models import Place
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

def index(request):
    places = Place.objects.filter(category = '명소').order_by('?')[:5]
    cafes = Place.objects.filter(category = '카페').order_by('?')[:5]
    restaurants = Place.objects.filter(category = '식당').order_by('?')[:5]
    return render(request, 'main/index.html', {'places' : places,
                                               'cafes' : cafes,
                                               'restaurants' : restaurants})

def login_index(request):
    if request.method == 'POST':
        account = request.POST.get('account')

        if account == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')

            userObject = authenticate(request, username = username, password = password)

            if userObject is not None:

                login(request, userObject)

            
            else:
                return render(request, 'user/login.html', {'error_msg' : '아이디 또는 비밀번호가 올바르지 않습니다.'})

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

def update_index(request):
    if request.method == 'POST':
        account = request.POST.get('account')

        if account == 'update':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            try:
                user = User.objects.get(username = username)
            except:
                return render(request, 'user/update.html', {'error_msg':'아이디 혹은 비밀번호가 잘못되었습니다.'})
            
            if check_password(password, user.username):
                newusername = request.POST.get('new_username')
                newpassword = request.POST.get('new_password')
                confirm = request.POST.get('new_password_confirm')
                
                if(newpassword == confirm):
                    user.username = newusername
                    user.set_password(newpassword)
                    user.save()
                else:
                    return render(request, 'user/update.html', {'error_msg':'비밀번호가 일치하지 않습니다.'})
                
            else:
                return render(request, 'user/update.html', {'error_msg':'아이디 혹은 비밀번호가 잘못되었습니다.'})
            
        else:
            return redirect('users:LoginUrl')
    else:
        pass

    return render(request, 'user/update.html', {})

@csrf_exempt
def delete_index(request):
    request.user.delete()
    logout(request)
    return redirect('users:LoginUrl')