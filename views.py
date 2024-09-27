from django.shortcuts import render,redirect
from laamar.models import laamar
from laamar.forms import laamarForm
def home(request):
    return render(request,'home.html')

def contact(request):
    laamarform=laamarForm(request.POST or None)
    if laamarform.is_valid():
        laamarform.save()
        return redirect('home')

    return render(request,'contact.html',{"forms":laamarform})
