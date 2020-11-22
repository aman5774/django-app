from django.shortcuts import render, redirect


def home_view(request):
    """
    Home view to display welcome message(landing page).
    :param request: request object
    :return:
    home.html template
    """
    try:
        return render(request, 'home.html')
    except Exception as e:
        # Todo: change this to redirect at error page
        print(e)
        return redirect('accounts:login')