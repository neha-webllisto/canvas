from django.shortcuts import render
from django.http import HttpResponse
import kronos

# Create your views here.
def demo(request):
	return render(request,'demo1.html')

def canvas(request):
	return render(request,'demo.html')

def image(request):
	return render(request, 'image.html')

def clock(request):
	return render(request,  'clock.html')

def card(request):
	return render(request,  'card3.html')

def loader(request):
	return render(request,  'loader.html')

