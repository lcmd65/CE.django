from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    form = AuthenticationForm()
    return render(request, "templates/base.html", {'form': form})