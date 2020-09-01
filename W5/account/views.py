from django.shortcuts import render, HttpResponse


def hello(request):
    print('dakhele view')

    return HttpResponse('Salam')


def goodbye(request):
    print('dakhele view goodbye')

    return HttpResponse('bye')
