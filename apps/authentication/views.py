from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def authentication(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Ricardao')

