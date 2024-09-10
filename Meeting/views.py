from django.shortcuts import render

# View for the index page
def index(request):
    return render(request, 'index.html')

# View for the home page
def home(request):
    return render(request, 'home.html')
# View for the planner page
def planner(request):
    return render(request, 'planner.html')


