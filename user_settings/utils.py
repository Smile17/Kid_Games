from .models import UserSetting
def  get_user_settings(request):
    # Default settings for unauthorized users
    num_question = 10
    default_game_query = ""

    if request.user.is_authenticated:
        settings = UserSetting.objects.get(user=request.user)
        num_question = settings.number_of_questions
        default_game_query = settings.default_game_query
    settings = {
        "num_question": num_question,
        "default_game_query": default_game_query
    }

    return settings