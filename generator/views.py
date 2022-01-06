from django.shortcuts import render
import random 
import string

# Create your views here.
def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')


def password(request):
    characters = list(string.ascii_lowercase)
    generater_password = ''    
    length = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('special'):
        characters.extend(list(string.punctuation))
    if request.GET.get('numbers'):
        characters.extend(list(string.digits))

    for char in range(length):
        generater_password += random.choice(characters)

    return render(request, 'password.html', {'password' : generater_password})