from django.shortcuts import redirect, render
from .models import Deadline, Project
from django.contrib import messages
# Create your views here.
def index(request):
    deadline =  Deadline.objects.all().last()
    
    project = Project()
    if request.method == 'POST':
        project.name = request.POST['name']
        project.phone = request.POST['phone']
        project.email = request.POST['email']
        project.title = request.POST['title']
        project.message = request.POST['message']
        project.save()
        messages.success(request, "Your Information has been successful submited, You will be contacted shortly")
        return redirect('index')
    context ={
        'deadline':deadline
    }
        
    return render(request, 'index.html',context)