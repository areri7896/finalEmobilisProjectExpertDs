from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def team(request):
    return render(request, 'team.html', {})