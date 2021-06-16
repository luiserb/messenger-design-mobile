from django.shortcuts import render
from django.views.generic.base import TemplateView


class FrontpageView(TemplateView):
    template_name = 'frontpage.html'
