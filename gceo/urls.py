from django.urls import include,path
from gceo.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home")
]
