from django.shortcuts import render 
from django.http import JsonResponse
from django.http import HttpResponse
from django.db import models

def index(request):
    return render(request,'index.html')


def index2(request):
    return render(request,'index2.html')

def ma_vue(request):
      data = {
        'username': 'Overlord',
        'fistname': 'Clément',
        'lastname': 'Abs',
        'age': 28,
        'myinput': 'an input'
             }
      dump = JsonResponse(data)
      return HttpResponse(dump, content_type='application/json')
    
def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        myinput = request.POST['myinput']

        # User.objects.create(
        #     username = username,
        #     firstname = firstname,
        #     lastname = lastname,
        #     age = age,
        #     myinput = myinput
        # )

        return HttpResponse('')


    


# def register(request):
#         if request.method == 'POST':
#             form = UserCreationForm(request.POST)
#             if form_is_valid():
#                 form.save()
#                 return redirect('/index2')

#         else:
#             form=UserCreationForm()
#             args = {'form': format}
#             return render(request, 'index.html')

