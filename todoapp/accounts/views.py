from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


def login_view(request):
    """
    Login view to display login form and authenticate user.
    :param request: request object
    :return:
    For GET, login.html template
    For POST, authenticate and redirect the user to corresponding view
    """
    try:
        if request.method == "POST":
            # serialize form data from the request
            form = AuthenticationForm(data=request.POST)

            # check for valid form
            if form.is_valid():
                # get user from the form
                user = form.get_user()

                # login user
                login(request, user)

                # checking if user need to redirect to some other route
                if "next" in request.POST:
                    return redirect(request.POST.get("next"))
                return redirect('tasks:list')
        else:
            # create authentication form and send the instance to template for rendering
            form = AuthenticationForm()
            return render(request, 'accounts/login.html', {'form': form})
    except Exception as e:
        # Todo: change this to redirect at error page
        print(e)
        # return redirect('accounts:login')


def logout_view(request):
    """
    Logout view to close the user session.
    :param request: request object
    :return:
    For POST, logout and redirect the user to login page.
    """
    try:
        if request.method == "POST":
            logout(request)
            return redirect('accounts:login')
    except Exception as e:
        # Todo: change this to redirect at error page
        print(e)
        return redirect('accounts:login')
