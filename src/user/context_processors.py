from allauth.socialaccount.models import SocialAccount


def get_avatar_and_username(requests):
    user_social_account = SocialAccount.objects.filter(user_id=requests.user.id)
    if user_social_account.exists():
        context = {'first_name': user_social_account.first().user.first_name,
                   'avatar': user_social_account.first().get_avatar_url(),
                   }

        return context
    return {}
