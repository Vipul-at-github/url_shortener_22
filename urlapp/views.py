from django.shortcuts import render, redirect
from django.http import request
import uuid
from .models import Urls
from django.http import HttpResponse, HttpRequest
# Create your views here.

def mainfn(request):
    return render(request, 'index.html')

def udhar(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Urls(inputlink=url, myid=uid)
        new_url.save()
        funcc = str(new_url.myid)
        sending = str('http://127.0.0.1:8000/'+funcc)
        return render(request, 'index.html', {'sending' : sending} )

def send(request, pk):
    url_01 = Urls.objects.get(myid = pk)
    mainlink = url_01.inputlink
    return redirect(mainlink)


    # return redirect('http://127.0.0.1:8000/'+slug)
# def newf(request, slug):
#     return HttpResponse(slug)