from django.http import HttpResponse
from django.shortcuts import render


def index(req):
    return HttpResponse('<h1>Users list</h1>')


def user(req):
    return HttpResponse('<h1>User info</h1>')

