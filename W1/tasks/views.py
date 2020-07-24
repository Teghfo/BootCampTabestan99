from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .models import Todo


@csrf_exempt
def create_todo(request):
    """
    create a todo task

    input: json ----> {'title': title, 'desc': description, 'due_date': due_date}

    output: success or failed
    """
    if request.method == "POST":
        data = request.body
        todo_data = json.loads(data)
        try:
            todo_data_title = Todo.objects.get(title = todo_data['title'])
            flag = True
        except:
            flag = False

        if not flag:
            try:
                todo_obj = Todo(title=todo_data["title"], description= todo_data['desc'], due_date=todo_data['due_date'])
                todo_obj.save()
                json_res = {'status': 'Ok'}
            except Exception as e:
                json_res = {'status': 'failed', 'error': str(e)}
    
        else:
             json_res = {'status': 'tasks hastesh!'}
        
        return JsonResponse(json_res)
    return JsonResponse({"status" : "bad reqwuest"})

@csrf_exempt
def update_todo(request, id):
    """
    """
    
    if request.method == 'PUT':
        data = request.body
        todo_data = json.loads(data)

        try:

            todo = Todo.objects.get(id = id)
            todo.title = todo_data["title"]
            todo.save()
            json_res = {'status': 'ba khubi khosi update shod'}
        except Exception as e:
            json_res = {'status': str(e)}

        return JsonResponse(json_res)

    return JsonResponse({'status': 'bad request'})


@csrf_exempt
def delete_todo(request, id):
    """
    """
    if request.method == 'DELETE':


        try:
            todo = Todo.objects.get(id = id)
            todo.delete()
            json_res = {'status': 'ba khubi khosi hazf shod'}
        except:
            json_res = {'status': 'ini ke mikhay nadaram'}

        return JsonResponse(json_res)

    return JsonResponse({'status': 'bad request'})


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

    return JsonResponse({"status": "bad request"})



def todo(request, id):
    """

    """

    pass