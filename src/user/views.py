from django.shortcuts import render, redirect


def index(requests):
    if not requests.user.is_anonymous:
        return redirect('profile')

    else:
        return render(requests, template_name='user/html/index.html')


def profile(requests):
    return render(requests, template_name='user/html/profile.html')


