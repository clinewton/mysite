from django.urls import include,path
from gceo.views import HomeView, DemoView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("demo", DemoView.as_view(), name="demo")
]
