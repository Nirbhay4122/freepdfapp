from django.shortcuts import render
from pdfapp.models import pdfinfo

# Create your views here.


def index(request):
    return render(request, 'index.html')

# Here starts Engineering colleges requests


def bhu(request):
    years = list(pdfinfo.objects.order_by().filter(
        college='bhu').values('year').distinct())
    if request.GET:
        req_year = request.GET.get('year')
        data = list(pdfinfo.objects.filter(year=req_year).values(
            'course', 'section', 'year', 'file'))
    else:
        data = list(pdfinfo.objects.all().values(
            'course', 'section', 'year', 'file'))
    return render(request, 'bhu.html', {'data': data, 'years': years})


# Here starts other colleges requests

def jam(request):
    years = list(pdfinfo.objects.order_by().filter(
        section='jam').values('year').distinct())
    if request.GET:
        req_year = request.GET.get('year')
        data = list(pdfinfo.objects.filter(year=req_year).values(
            'course', 'section', 'year', 'file'))
    else:
        data = list(pdfinfo.objects.all().values(
            'course', 'section', 'year', 'file'))
    return render(request, 'jam.html', {'data': data, 'years': years})


def gate(request):
    years = list(pdfinfo.objects.order_by().filter(
        section='gate').values('year').distinct())
    if request.GET:
        req_year = request.GET.get('year')
        data = list(pdfinfo.objects.filter(year=req_year).values(
            'course', 'section', 'year', 'file'))
    else:
        data = list(pdfinfo.objects.all().values(
            'course', 'section', 'year', 'file'))
    return render(request, 'gate.html', {'data': data, 'years': years})


def nimcet(request):
    years = list(pdfinfo.objects.order_by().filter(
        section='nimcet').values('year').distinct())
    if request.GET:
        req_year = request.GET.get('year')
        data = list(pdfinfo.objects.filter(year=req_year).values(
            'course', 'section', 'year', 'file'))
    else:
        data = list(pdfinfo.objects.all().values(
            'course', 'section', 'year', 'file'))
    return render(request, 'nimcet.html', {'data': data, 'years': years})


def aimcet(request):
    years = list(pdfinfo.objects.order_by().filter(
        section='aimcet').values('year').distinct())
    if request.GET:
        req_year = request.GET.get('year')
        data = list(pdfinfo.objects.filter(year=req_year).values(
            'course', 'section', 'year', 'file'))
    else:
        data = list(pdfinfo.objects.all().values(
            'course', 'section', 'year', 'file'))
    return render(request, 'aimcet.html', {'data': data, 'years': years})


def neet(request):
    years = list(pdfinfo.objects.order_by().filter(
        section='neet').values('year').distinct())
    if request.GET:
        req_year = request.GET.get('year')
        data = list(pdfinfo.objects.filter(year=req_year).values(
            'course', 'section', 'year', 'file'))
    else:
        data = list(pdfinfo.objects.all().values(
            'course', 'section', 'year', 'file'))
    return render(request, 'neet.html', {'data': data, 'years': years})


def jee(request):
    years = list(pdfinfo.objects.order_by().filter(
        section='jee').values('year').distinct())
    if request.GET:
        req_year = request.GET.get('year')
        data = list(pdfinfo.objects.filter(year=req_year).values(
            'course', 'section', 'year', 'file'))
    else:
        data = list(pdfinfo.objects.all().values(
            'course', 'section', 'year', 'file'))
    return render(request, 'jee.html', {'data': data, 'years': years})


# Here starts iit colleges requests
