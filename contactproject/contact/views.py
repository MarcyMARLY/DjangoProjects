from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http import Http404
from .models import Person
from django.urls import reverse
from .serializers import PersonSerializer2


@csrf_exempt
def person_list(request):
  if request.method == "GET":
    persons = Person.objects.all()
    ser = PersonSerializer2(persons, many=True)
    return JsonResponse(ser.data, safe=False)
  elif request.method == "POST":
    data = JSONParser().parse(request)
    ser = PersonSerializer2(data=data)
    if ser.is_valid():
      ser.save()
      return JsonResponse(ser.data, status=201)
    return JsonResponse(ser.errors, status=400)
@csrf_exempt
def person_detail(request, person_id):

  try:
    person = Person.objects.get(pk=person_id)
  except Exception as e:
    return JsonResponse({"error": str(e)}, status=404)

  if request.method == "GET":
    ser = PersonSerializer2(person)
    return JsonResponse(ser.data)
  elif request.method == "PUT":
    data = JSONParser().parse(request)
    ser = PersonSerializer2(person, data)
    if ser.is_valid():
      ser.save()
      return JsonResponse(ser.data)
  elif request.method == "DELETE":
    person.delete()
    ser = PersonSerializer2(person)
    return JsonResponse(ser.data)


def index(request):
    person_list = Person.objects.all
    return render(request,'contact/index.html',{'person_list':person_list})
def newperson(request):
    return render(request,'contact/newpersonform.html')
def add(request):
    name = request.POST['person_name']
    phone = request.POST['person_phone']
    photo = request.POST['person_photo']

    p = Person(person_name = name, person_phone = phone, person_photo = photo)
    p.save()
    return HttpResponseRedirect(reverse('contact:index'))
def edit(request,person_id):
    name = Person.objects.get(pk = person_id).person_name
    phone = Person.objects.get(pk = person_id).person_phone
    photo = Person.objects.get(pk = person_id).person_photo

    return render(request, 'contact/edit.html',{'name':name,'phone':phone,'photo':photo,'id':person_id})
def save(request, person_id):
    name = request.POST['person_name']
    phone = request.POST['person_phone']
    photo = request.POST['person_photo']
    Person.objects.filter(pk = person_id).update(person_name = name, person_phone = phone, person_photo = photo)
    return HttpResponseRedirect(reverse('contact:index'))

def delete(request, person_id):
    Person.objects.filter(pk = person_id).delete()
    return HttpResponseRedirect(reverse('contact:index'))
