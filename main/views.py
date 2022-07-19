from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SignupForm
from django.contrib.auth import login, authenticate, logout
from .models import Projects, Account
from . import check_inn
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.core.files.storage import FileSystemStorage
import os




website_url = "http://195.161.68.192:49300"

# Create your views here.

def index(request):
    return render(request, 'main/index.html')



def pagelogout(request):
    try:
        logout(request)
        print("out")
        return HttpResponseRedirect(website_url)
    except Exception as e:
        print(e)
        return HttpResponseRedirect(website_url)


def signup(request):
    try:
        if request.POST['inn'] != 'none':
            if len(check_inn.find_INN('party', request.POST['inn'])['suggestions']) == 0:
                form = SignupForm()
                data = {
                    'username': request.POST['username'],
                    'form': form,
                    'inn_status': 'disabled'
                }
                return render(request, 'main/signup.html', data)
            else:
                data = {
                    "inn_status": "enable"
                }
    except:
        print("No POST requests yet")
        pass

    if request.user.is_authenticated:
        return HttpResponseRedirect(website_url)

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.is_active = True
            user.save()
            Account.objects.create(user_id=user.id)
            return HttpResponseRedirect(website_url + 'login' + '?loginSuccess')

    else:
        form = SignupForm()

    data = {
        'form': form,
    }

    return render(request, 'main/signup.html', data)


def login(request):
    login_status = 0
    print("tandz")
    if 'loginSuccess' in request.GET:
        login_status = 1

    data = {
        'login_status': login_status
    }
    return render(request, "main/login5.html", data)


def projects(request):
    projects = Projects.objects.all().filter(active = 'on').order_by('-id')
    if len(projects) == 0:
        projects = 0
    data = {
        'projects': projects
    }
    return render(request, "main/projects.html", data)


def profile(request):
    print(request.user.id)
    user = Account.objects.get(user_id=request.user.id)

    social = Account.objects.filter(user_id=request.user.id).values('fb', 'insta', 'ok', 'twitter', 'viber', 'vk', 'whatsapp')
    data = {
        'account': user,
        'social': social
    }
    return render(request, "main/profile.html", data)


def profile_edit(request):
    current_account = Account.objects.get(user_id=request.user.id)
    changed = 0
    if request.method == 'POST':
        print(request.POST)
        account = Account.objects.filter(user_id=request.user.id).update(
            full_name = request.POST['fname'],
            phone = request.POST['phone'],
            country = request.POST['country'],
            region = request.POST['region'],
            city = request.POST['city'],
            service_type = request.POST['type'],
            vk = request.POST['vk'],
            fb = request.POST['fb'],
            ok = request.POST['ok'],
            insta = request.POST['insta'],
            twitter = request.POST['twitter'],
            viber = request.POST['viber'],
            whatsapp = request.POST['whatsapp'])

        try:
            upload = request.FILES['upload']
            fss = FileSystemStorage()
            if os.path.exists(f"main/static/main/img/avatars/{request.user.id}.jpg"):
                os.remove(f"main/static/main/img/avatars/{request.user.id}.jpg")

            file = fss.save(f"main/static/main/img/avatars/{request.user.id}.jpg", upload)
        except:
            pass




        changed = 1
        # user = User.objects.get(username=request.user.username)
        # if request.POST['new_password'] == request.POST['password_confirm']:
        #     user.set_password(request.POST['new_password'])
        #     user.save()
        #     update_session_auth_hash(request, user)
        #     changed = 1


    data = {
        'changed': changed,
        'account': current_account,
    }

    return render(request, "main/profile_edit.html", data)



def add_service(request):
    added = 0
    if request.method == 'POST':
        try:
            projects = Projects(user_id = request.user.id,
            user_name = request.user.first_name,
            active = request.POST['active'],
            project_name = request.POST['service_name'],
            project_desc = request.POST['service_desc'],
            project_full_desc = request.POST['service_full_desc'],
            price = request.POST['service_price'])
            projects.save()
            added = 1
        except Exception as e:
            print(e)

    data = {
        'added': added
    }

    return render(request, "main/add_service.html", data)
