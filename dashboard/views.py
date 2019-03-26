from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class PdfView(TemplateView):
    template_name = "index.html"

class PrintView(TemplateView):
    template_name = "print.html"