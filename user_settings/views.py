from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ApplicationSettingForm
from .models import *
def user_settings(request):
    settings = UserSetting.objects.get(user=request.user)
    initial_data = {
        'number_of_questions': settings.number_of_questions,
        'default_game_query': settings.default_game_query
    }
    app_form = ApplicationSettingForm(initial=initial_data)
    context = {"app_form": app_form}
    print(context)
    return render(request, "user_settings/user_settings.html", context)


def application_settings(request):
    if request.method == 'POST':
        form = ApplicationSettingForm(request.POST)
        if form.is_valid():
            settings = UserSetting.objects.get(user=request.user)
            settings.default_game_query = form.cleaned_data['default_game_query']
            settings.number_of_questions = form.cleaned_data['number_of_questions']
            settings.save()
            print("SETTINGS UPDATED")
    return redirect(user_settings)