from django.shortcuts import render,redirect


from . models import clothes
from . forms import userform

# Create your views here.

def formy(request):
    input = userform()
    if request.method == "POST":
        input = userform(request.POST)
        if input.is_valid():
          input.save()
          return redirect("home")
        else:
            input = userform()
    context = {"kits":input}
    return render(request,'forms.html',context)
    

def displayinput(request):
    items = clothes.objects.all()
    context= {"items":items}
    return render(request,'display.html',context)
        
def one(request,pk):
    items = clothes.objects.get(id=pk)
    context= {"items":items}
    return render(request,'one.html',context)


def update(request):
    input = userform()
    if request.method == "POST":
        input = userform(request.POST)
        if input.is_valid():
          input.save()
          return redirect("home")
        else:
            input = userform()
    context = {"kits":input}
    return render(request,'update.html',context)











