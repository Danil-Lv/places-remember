from django.shortcuts import render, redirect


def index(requests):
    """Displaying the home page"""
    if not requests.user.is_anonymous:
        return redirect('profile')

    else:
        return render(requests, template_name='user/html/index.html')


def profile(requests):
    """Displaying the profile page"""
    return render(requests, template_name='user/html/profile.html')




