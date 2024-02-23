from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,"index.html")

def sell(request):
    return render(request,"sell-property.html")

def signin(request):
        
    return render(request,"signin.html")

def signup(request):
    return render(request,"signup.html")
def connect(request):
    dic={}
    try:
            if request.method == 'POST':
                 
                n1=int(request.POST.get('num1'))
                
                dic={
                    'n1':n1
                }
                url="/signin/?output={}".format(n1) 
                return HttpResponseRedirect(url)
#print("username",n['uname'])
    except:
        pass
    else:
        return render(request,"userform.html",dic)

    # return HttpResponseRedirect('/signin/')  

