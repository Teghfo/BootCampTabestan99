from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from .models import Todo

def create_todo(request):
    """

    """
    pass


def update_todo(request, id):
    """
    """

    pass


def delete_todo(request, id):
    """
    """

    return HttpResponse("<div> <h1>hello </h1></div>")


def all_todos(request):
    """
    get all todo task in system!

    input:

    output: all todos
    """
    if request.method == "GET":
        todos = Todo.objects.all()

        json_res = []
        for todo in todos:
            temp = {
                'title': todo.title, 
                'des': todo.description,
                'due_date': todo.due_date,
                'status': todo.done
            }
            json_res.append(temp)

        return JsonResponse(json_res, safe=False)

    return HttpResponse("Bad request")



def todo(request, id):
    """
    """

    pass