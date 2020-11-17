import json
import requests
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from .models import Profil, Localisation
from django.http import HttpResponse

# Create your views here.
class myLoginView(LoginView):
    template_name="time_app/login.html"

class myLogoutView(LogoutView):
    pass

@login_required(login_url="login")
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

def get_location_data(request, location_id):
    location = Localisation.objects.get(pk=location_id)
    url = "http://worldtimeapi.org/api/timezone/{continent}/{city}".format(continent=location.continent, city=location.city)
    response = requests.get(url)
    return HttpResponse(response.text)
