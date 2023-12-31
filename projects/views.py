from django.shortcuts import redirect, render
# Create your views here.
def index(request):
    
    context ={
       
    }
        
    return render(request, 'home/index.html',context)