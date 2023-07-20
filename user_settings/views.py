from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ApplicationSettingForm
from .models import *
def user_settings(request):
    settings = UserSettings.objects.get(user=request.user)
    initial_data = {
        'autoplay_sound': settings.autoplay_sound,
        'number_of_questions': settings.number_of_questions
    }
    app_form = ApplicationSettingForm(initial=initial_data)
    context = {"user": request.user, "settings": settings, "app_form": app_form}
    return render(request, "user_settings/user_settings.html", context)


def application_settings(request):
    if request.method == 'POST':
        form = ApplicationSettingForm(request.POST)
        if form.is_valid():
            settings = UserSettings.objects.get(user=request.user)
            settings.autoplay_sound = form.cleaned_data['autoplay_sound']
            settings.number_of_questions = form.cleaned_data['number_of_questions']
            settings.save()
            print("SETTINGS UPDATED")
    return redirect(user_settings)