from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import myText

# Create your views here.
def home_list(request):
    texts = myText.objects.filter()
    print(texts)
    return render(request, 'inflearn_lecture/home_list.html',{'texts':texts})

def lecture_list(request):
    texts = myText.objects.filter()

    hot_lecture = myText.objects.filter(category="인기")
    print(texts)
    return render(request, 'inflearn_lecture/lecture_list.html',
                {'texts':texts, 'hot_lecture':hot_lecture})

def login(request):

    print("로그인")

    if request.method  == 'POST':

        print("로그인 success")

        email = request.POST['email']
        pwd = request.POST['pwd']

        user = auth.authenticate(request, username=email, password=pwd)

        if user is None:
            print("가입된 회원이 아닙니다.")
            return redirect('/join')
        else:
            auth.login(request, user)
            return redirect('/')

    return render( request, 'inflearn_lecture/login.html')
 
def join(request):

    print("join 실행")
    if request.method =="POST":
        print("포스팅 요청")

        email = request.POST['email']
        pwd = request.POST['pwd'] 
        User.objects.create_user(username=email, password=pwd)          #User 오브젝트에 추가
 
        return redirect('/')

    print("join 마지막 부분") 
    return render( request, 'inflearn_lecture/join.html')


def logout(request):

    auth.logout(request)
    return redirect('/')


def lecture_list_info(request, pk):
    
   board_contents = get_object_or_404(myText, pk = pk)

   print(board_contents)
