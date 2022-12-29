from django.shortcuts import render

# Create your views here.
def kupi(request):
    dict={'c':'views'}
    return render(request,'frrd.html',context=dict)