from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse, QueryDict
from django.template import loader
from django.http import Http404
from .models import Status,TodoItem
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def todo_list(request):
    if request.method == "GET":
        todo_list = TodoItem.objects.all()
        todo_list_json = [t.to_json() for t in todo_list]
        return JsonResponse(todo_list_json, safe=False)

    elif request.method == "POST":
        data = request.POST
        todo = TodoItem()
        todo.todo_text = data.get('todo_text','')
        todo.todo_status = data.get('todo_status','')
        todo.save()
        return JsonResponse(todo.to_json(), status = 201)
@csrf_exempt
def todo_detail(request, todo_id):

  try:
    todo = TodoItem.objects.get(pk=todo_id)
  except Exception as e:
    return JsonResponse({"error": str(e)}, status=404)

  if request.method == "GET":
    return JsonResponse(todo.to_json())
  elif request.method == "PUT":
    data = QueryDict(request.body)
    todo.todo_text = data.get('todo_text', todo.todo_text)
    todo.todo_status = data.get('todo_status', todo.todo_status)
    todo.save()
    return JsonResponse(todo.to_json())
  elif request.method == "DELETE":
    todo.delete()
    return JsonResponse(todo.to_json())

def index(request):
    todo_list = TodoItem.objects.all
    return render(request,'todo_demo/index.html',{'todo_list':todo_list})

def TodoItemFunc(request):
    return render(request,'todo_demo/TodoItem.html',{'statusList':Status.objects.all})

def add(request):
    text = request.POST['todo_text']
    status = request.POST['status']
    s = Status.objects.get(pk = status)
    todoItem = s.todoitem_set.create(todo_text = text)
    return HttpResponseRedirect(reverse('todo_demo:index'))

def edit(request, todo_id):
    text = TodoItem.objects.get(pk = todo_id).todo_text
    status = TodoItem.objects.get(pk = todo_id).todo_status
    return render(request, 'todo_demo/edit.html',{'text':text,'status':status,'id':todo_id,'statusList':Status.objects.all})

def save(request):
    text = request.POST['todo_text']
    status = request.POST['status']
    todoItem = TodoItem.objects.create(todo_text = text, todo_status = status)
    return HttpResponseRedirect(reverse('todo_demo:index'))
def delete(request,id):
    TodoItem.objects.get(pk = id).delete()
    return HttpResponseRedirect(reverse('todo_demo:index'))
