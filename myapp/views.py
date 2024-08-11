from django.shortcuts import render

# Create your views here.

# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 登録後自動的にログイン
            return redirect('home')  # ログイン後のリダイレクト先
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})  # ここが重要です



# def home(request):
#     return render(request, 'home.html')


# myapp/views.py
from django.shortcuts import render

# def home(request):
#     # 実際にはデータベースから資格とユーザー情報を取得するロジックが必要です。
#     # ここでは例として仮のデータを使用します。
#     user_list = [
#         {"name": "ユーザーA"},
#         {"name": "ユーザーB"},
#         {"name": "ユーザーC"},
#     ]
#     context = {
#         "qualification": "基本情報技術者",
#         "users": user_list
#     }
#     return render(request, 'home.html', context)



# myapp/views.py
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import QualificationForm

def home(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = QualificationForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QualificationForm(instance=profile)

    context = {
        'form': form,
        'qualification': profile.qualification,
        'users': UserProfile.objects.all()  # 仮に全ユーザーのプロファイルを取得
    }
    return render(request, 'home.html', context)




# myapp/views.py
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    messages.info(request, "ログアウトしました。")
    return redirect('home')
