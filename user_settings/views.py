from django.shortcuts import render
from .forms import ApplicationSettingForm
from .models import *
def user_settings(request):
    settings = UserSettings.objects.get(user=request.user)
    app_form = ApplicationSettingForm()
    context = {"user": request.user, "settings": settings, "app_form": app_form}
    print(context)
    return render(request, "user_settings/user_settings.html", context)


