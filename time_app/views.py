import json
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.forms.models import model_to_dict
from .models import Profil
from django.http import HttpResponse

# Create your views here.
class myLoginView(LoginView):
    template_name="time_app/login.html"

def index(request):
    return render(request, "time_app/index.html")

def get_user_data(request):
    user = request.user
    profil = Profil.objects.get(user=user)
    locations = profil.localisations.all()
    result = []
    for local in locations:
        result.append(model_to_dict(local))
    return HttpResponse(json.dumps(result))