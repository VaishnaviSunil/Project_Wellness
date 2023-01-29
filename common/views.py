from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'common_folder/index.html')

def consumerlogin(request) :
    return render (request,'common_folder/consumerlogin.html')

def sellerlogin(request) :
    return render (request,'common_folder/sellerlogin.html')
