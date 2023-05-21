from allauth.socialaccount.models import SocialAccount
from django.shortcuts import render


def index(requests):

    if not requests.user.is_anonymous:
        user_social_account = SocialAccount.objects.get(user_id=requests.user.id)

        context = {'first_name': user_social_account.user.first_name,
                   'avatar': user_social_account.get_avatar_url()
                   }
        return render(requests, template_name='user/html/profile.html', context=context)

    else:
        return render(requests, template_name='user/html/index.html')



def profile(requests):
    user_social_account = SocialAccount.objects.get(user_id=requests.user.id)

    context = {'first_name': user_social_account.user.first_name,
               'avatar': user_social_account.get_avatar_url()
               }

    return render(requests, template_name='user/html/profile.html', context=context)
