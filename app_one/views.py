from django.shortcuts import render
import random
import string

# Create your views here.
def home(request):
    return render(request, "index.html")

def random_word(length):
    letters = string.ascii_uppercase
    word = ''.join(random.choice(letters) for i in range(length))
    return word