from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import customUserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profiles
from articles.models import Articles
from .utils import searchProfiles


# Create your views here.


def userProfiles(request):
    profiles, search_query = searchProfiles(request)
    context = {'profiles':profiles,'search_query': search_query}

    return render(request,"userapps/profiles.html",context)

def singleProfile(request,pk):
    userObj = Profiles.objects.get(id=pk)

    
    context = {"profile":userObj,}


    return render(request, "userapps/single_profile.html",context)

def registerUser(request):
    page = 'register'
    form = customUserCreationForm()

    if request.method == "POST":
        form = customUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            
            # Check for uniqueness before saving the form
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already in use. Please choose a different one.')
            else:
                try:
                    user = form.save()
                    user.username = user.username.lower()
                    user.save()
                    messages.success(request, 'User account created successfully')
                    login(request, user)
                    return redirect("profiles")
                except:
                    pass

        else:
            messages.error(request, 'An error has occurred while creating the user.')

    context = {'page': page, 'form': form}
    return render(request, "userapps/login_register.html", context)

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')


    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'username does not exist or password incorrect')

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,"User does not exist")

    return render(request, "userapps/login_register.html")

def logoutUser(request):
    logout(request)
    messages.success(request, 'user logged out succesfully')
    return redirect('login')