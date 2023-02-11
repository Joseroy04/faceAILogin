from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    # path("", views.homepage, name="homepage"),
    path("", views.signup, name="register"),
    path('/signupaction',views.signupaction, name="sa")
]