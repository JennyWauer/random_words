from django.shortcuts import render, redirect
import random
import string


# Create your views here.
def generate(request, length):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] +=1
    letters = string.ascii_uppercase
    word = ''.join(random.choice(letters) for i in range(length))
    return word


def random_word(request):
    context = generate(request, 16)
    return render(request, "index.html", {'context': context})

def reset(request):
    if 'counter' in request.session:
        request.session['counter'] = 0
    return redirect('/random_word')