from django.shortcuts import render

def film_detail(request, film_id):
    return render(request, 'films-detail.html')