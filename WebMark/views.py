
from django.http import HttpResponse,HttpResponseRedirect
from addwebsite.models import Addweb
from django.db.models import Q
from django.shortcuts import render

def home(request):
    # data={
    #     'title' : 'HomePage',
    #     'clist' : ['php','java',45],
    #     'sdata' : [{'name':'abc','sid':10},{'name':'xyz','sid':20}]
    # }
     
    
    # for i in webdata:
    #     print(i.web_name)
    webdata = Addweb.objects.all()[:6]
    data={}
    if request.method == "GET":
        st=request.GET.get('websitename')

        if st!=None:
           webdata = Addweb.objects.filter(Q(web_name__icontains=st) | Q(web_description__icontains=st))
    
        
    data = {
                 'webdata':webdata 
               }
   
    return render(request,"index.html",data)

def addwebsite(request):

    try:
        if request.method == "POST":
        # name=request.GET['name']
        # description=request.GET['description']
        # url=request.GET['url']
        # name=request.GET.get('name')
        # description=request.GET.get('description')
        # url=request.GET.get('url')
        
            name=request.POST.get('name')
            description=request.POST.get('description')
            url=request.POST.get('url')
            en=Addweb(web_name=name,web_description=description,web_url=url)
            en.save()
            return HttpResponseRedirect('/')

    except:
         pass

    return render(request,"addwebsite.html")

def aboutUs(request):
    return HttpResponse("about WebMark")

def productInfo(request,pinfo):
    return HttpResponse(pinfo)

def delete(request,id):

    tep = Addweb.objects.get(id=id)
    tep.delete()

    return HttpResponseRedirect('/')

def update(request,id):
    data = Addweb.objects.get(id=id)
    return render(request,"edit.html",{'data':data})

def edit(request,id):

    name=request.POST.get('name')
    description=request.POST.get('description')
    url=request.POST.get('url')
    # up=Addweb(id=id,web_name=name,web_description=description,web_url=url)
    # up.save()
    up=Addweb.objects.filter(id=id).update(web_name=name,web_description=description,web_url=url)
    return HttpResponseRedirect('/')