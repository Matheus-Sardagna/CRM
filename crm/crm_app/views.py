from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def clientes(request):
    return render(request, 'pages/clientes.html')