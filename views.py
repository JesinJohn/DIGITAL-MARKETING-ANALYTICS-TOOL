from django.shortcuts import render
from django.http import HttpResponse

from django.template.loader import get_template
from django.template import Context


# Create your views here.
def home(request):
        t = get_template('Visitor/home.html')
        html = t.render()
        return HttpResponse(html)
def about(request):
        t = get_template('Visitor/about.html')
        html = t.render()
        return HttpResponse(html)
def login(request):
        t = get_template('Visitor/login.html')
        html = t.render()
        return HttpResponse(html)
def index(request):
        t = get_template('Visitor/index.html')
        html = t.render()
        return HttpResponse(html)
def indexx(request):
        t = get_template('Visitor/indexx.html')
        html = t.render()
        return HttpResponse(html)
def blank(request):
        t = get_template('Visitor/blank.html')
        html = t.render()
        return HttpResponse(html)
def monthlybar(request):
        t = get_template('Visitor/monthlybar.html')
        html = t.render()
        return HttpResponse(html)
def employeepie(request):
        t = get_template('Visitor/employeepie.html')
        html = t.render()
        return HttpResponse(html)
def progressline(request):
        t = get_template('Visitor/progressline.html')
        html = t.render()
        return HttpResponse(html)
