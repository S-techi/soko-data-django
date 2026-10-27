from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import shopform
from . models import shop
# Create your views here.
def home(request):
    return HttpResponse ("Hello,Im Sienna"),

def userform(request):
    form = shopform()
    if request.method == "POST":
        form = shopform(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect("display_table")
        else:
            form = shopform()  
    context = {"box":form}
    return render(request,'sapp/forms.html',context)

def displayform(request):
    shops= shop.objects.all()
    context = {"shops":shops}
    return render(request,'sapp/display.html',context)



