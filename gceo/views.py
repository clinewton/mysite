from django.shortcuts import render
from django.views import View

# Create your views here.

class HomeView(View):
    # model = Home
    template_name = "gceo/index.html"

    def get(self, request):
        return render(request, self.template_name,{})

class DemoView(View):
    # model = Home
    template_name = "gceo/demo.html"

    def get(self, request):
        return render(request, self.template_name,{})
