from .models import UserSetting
def  get_user_settings(request):
    # Default settings for unauthorized users
    num_question = 10

    if request.user.is_authenticated:
        settings = UserSetting.objects.get(user=request.user)
        num_question = settings.number_of_questions
    settings = {
        "num_question": num_question
    }

    return settings