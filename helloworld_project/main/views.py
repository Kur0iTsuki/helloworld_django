from django.shortcuts import render
from django.http import JsonResponse

def hello_world(request):
    if request.GET.get('format') == 'json':
        return JsonResponse({"Message": "Hello World!"})
    else:
        return render(request, 'main/hello.html')
