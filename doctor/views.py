from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
# def home(request):
#     return HttpResponse("It's working")


class HomeTemplateView(TemplateView):
    template_name = "index.html"
