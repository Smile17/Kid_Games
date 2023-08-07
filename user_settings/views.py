from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ApplicationSettingForm, CustomPasswordChangeForm, UserEditForm
from .models import *


def user_settings(request):
    settings = UserSetting.objects.get(user=request.user)
    initial_data = {
        'number_of_questions': settings.number_of_questions,
        'default_game_query': settings.default_game_query
    }
    app_form = ApplicationSettingForm(initial=initial_data)
    form_change_password = CustomPasswordChangeForm(user=request.user)
    form_user_edit = UserEditForm(instance=request.user)
    #games = settings.games
    games = GameType.objects.all()
    for game in games:
        game.is_active = settings.games.filter(id=game.id).exists()

    context = {"app_form": app_form, "form_change_password": form_change_password, "form_user_edit": form_user_edit, "games": games}
    return render(request, "user_settings/user_settings.html", context)


def game_selection(request):
    if request.method == 'POST':
        arr = request.POST["selected_games"]
        arr = json.loads(arr)
        settings = UserSetting.objects.get(user=request.user)
        settings.games.clear()
        for key in arr:
            if arr[key] == True:
                settings.games.add(key)
        settings.save()
    return redirect(user_settings)


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


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect(user_settings)
        else:
            messages.error(request, 'Please correct the error below.')
    return redirect(user_settings)


def user_edit(request):
    if request.method == 'POST':
        user = request.user
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            print("USER INFO UPDATED")
            return redirect(user_settings)
    return redirect(user_settings)


