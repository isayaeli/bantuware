from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        request.POST['name']
        request.POST['email']
        request.POST['title']
        request.POST['message']
    return render(request, 'index.html')