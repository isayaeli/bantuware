import imp
from django.shortcuts import redirect, render
from .models import Project
from django.contrib import messages
# Create your views here.
def index(request):
    project = Project()
    if request.method == 'POST':
        project.name = request.POST['name']
        project.phone = request.POST['phone']
        project.email = request.POST['email']
        project.title = request.POST['title']
        project.message = request.POST['message']
        project.save()
        messages.success(request, "Your Information has been successful submited")
        return redirect('index')
        
    return render(request, 'index.html')