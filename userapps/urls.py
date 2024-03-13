from django.urls import path
from .views import userProfiles,singleProfile,registerUser,loginUser,logoutUser

urlpatterns = [ 
    path('',userProfiles,name="profiles"),
    path('profile<str:pk>/',singleProfile,name="user-profile"),
    path('register/',registerUser,name="register"),
    path("login/",loginUser,name="login"),
    path('logout/',logoutUser,name="logout")
]