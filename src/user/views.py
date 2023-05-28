from django.shortcuts import render, redirect


def index(requests):
    """Displaying the start page"""
    if not requests.user.is_anonymous:
        return redirect('profile')

    else:
        return render(requests, template_name='user/html/index.html')
