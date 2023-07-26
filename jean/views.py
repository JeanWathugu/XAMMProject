from django.shortcuts import render
from jean.forms import learners_form
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
def insert(request):
    learner = learners_form()
    return render(request, 'index.html', {'form':learner})

# Create your views here.
