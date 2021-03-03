from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse

from myproject.form import *
from django.contrib.auth.decorators import login_required
# Create your views here.
from .filter import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import json
from.models import *
from django.db.models import Q
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.contrib import messages


# Create your views here.
def type(request,id):
    ep=ExploreProject.objects.filter(type=id)
    type_name=Type.objects.get(id=id)
    page = request.GET.get('page')
    paginator = Paginator(ep, 1)
    try:
        pro = paginator.page(page)
    except PageNotAnInteger:
        pro = paginator.page(1)
    except EmptyPage:
        pro = paginator.page(paginator.num_pages)
    return render(request,'myproject/type.html',context={'explore_project':ep,'type':type_name,'pro':pro})


def all_project(request):
    project=ExploreProject.objects.filter(active=True)
    type=Type.objects.all().order_by('-timestamp')
    myFilter=ExploreProjectFilter(request.GET,queryset=project)
    project=myFilter.qs
    page = request.GET.get('page')
    paginator = Paginator(project, 1)
    try:
        project = paginator.page(page)
    except PageNotAnInteger:
        project = paginator.page(1)
    except EmptyPage:
        project = paginator.page(paginator.num_pages)
    context={
        'projects':project,
        'myFilter':myFilter,
        'type':type
    }
    return render(request,'myproject/allproject_explore.html',context)


def project_by_slug(request,id):
    ep=ExploreProject.objects.get(id=id)
    context={
        'ep':ep
    }
    return render(request,'myproject/all_project_slug.html',context)

@login_required(login_url='home')
def CreateExploreProject(request):
    form=ExploreProjectForm()
    if request.method=='POST':
        form=ExploreProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('all_project')



    context={'form':form,'verfiy':True}
    return render(request,'myproject/post_form.html',context)


@login_required(login_url='home')
def UpdateExploreProject(request,id):
    explore_project=ExploreProject.objects.get(id=id)
    form=ExploreProjectForm(instance=explore_project)
    if request.method=='POST':
        form=ExploreProjectForm(request.POST,request.FILES,instance=explore_project)
        if form.is_valid():
            form.save()
        return redirect('all_project')



    context={'form':form,'verfiy':True}
    return render(request,'myproject/post_form.html',context)

@login_required(login_url='home')
def DeleteExporeProject(request,id):
    explore_project=ExploreProject.objects.get(id=id)
    if request.method == 'POST':
        explore_project.delete()
        return redirect('all_project')

    context={'item':explore_project,'verfiy':True}
    return render(request,'myproject/delete.html',context)

