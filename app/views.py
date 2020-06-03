from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'welcomeperson':['Jagadeesh','ashu'],'guest':'harshad'}
    return render(request,'jinja.html',context=d)