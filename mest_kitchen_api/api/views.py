from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def print_hello_world(request):
    return HttpResponse(
        "<h1 style='color: red'>Hello World</h1>"
    )


def print_json(request):
    return JsonResponse(
        {
            "name": "Dafe",
            "profession": "Body builder"
        }
    )