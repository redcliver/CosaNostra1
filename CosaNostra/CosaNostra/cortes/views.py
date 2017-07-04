from django.shortcuts import render

# Create your views here.

def cortes(request):
    return render(request, 'cortes.html')