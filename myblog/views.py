from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse

from myblog.forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
from .filter import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import json
from.models import *
from django.db.models import Q
from myproject.models import *
from django.core.mail import BadHeaderError, send_mail
from django.contrib import messages


# Create your views here.

def home(request):
    posts=Post.objects.filter(active=True,featured=True)[0:3]
    explore_project=ExploreProject.objects.filter(active=True,featured=True)[0:3]
    context={'posts':posts,'tags':Tag.objects.all().order_by('-timestamp'),
             'explore_project':explore_project,
             }
    return render(request,'index.html',context)


def posts(request):
    posts=Post.objects.filter(active=True).order_by('-timestamp')
    tag=Tag.objects.all().order_by('-timestamp')
    myFilter=PostFilter(request.GET,queryset=posts)
    posts=myFilter.qs
    page = request.GET.get('page')
    paginator = Paginator(posts, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context={
        'posts':posts,
        'myFilter':myFilter,
        'tag':tag,
    }
    return render(request,'myblog/posts.html',context)


def privacy_policy(request):
    return render(request,'myblog/privacy_policy.html')

def post(request,id):
    post=Post.objects.get(id=id)
    context={
        'post':post
    }
    return render(request, 'myblog/post.html',context)

def sendEmail(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone_no')
        message=request.POST.get('message')
        from_email='allbakchodofindia@gmail.com'


        # client_key=request.POST['g-recaptcha-response']
        # secret_key='6Le8s2waAAAAAGG2fougSuYQPDdOv6nNdrMwjx-B'
        client_ip = request.META['REMOTE_ADDR']
        form_name=str(name).upper()
        # captchadata={
        #     'secret':secret_key,
        #     'response':client_key
        # }
        # r = request.POST('https://www.google.com/recaptcha/api/siteverify', data=captchadata)
        # response = json.loads(r.text)
        # if response['success']==False:
        #     messages.error(request,'Captcha Invalid')

        if name and subject and message and phone_no and email:
            try:
                send_mail(
                    subject,
                    f''' Thanks for contacting us {form_name}.We will be in touch with you shortly

                                Regards
                                Code With Rohit
                                ''',
                    from_email,
                    [email],
                    fail_silently=False,
                )
            except BadHeaderError:
                messages.error(request,'Message Form Not Successfully Submited')
                # return HttpResponse('Invalid header found.')
        contact = Contact(name=name, phone_no=phone_no, email=email, subject=subject,message=message,ip_address=client_ip)
        messages.success(request,f'Thanks for Contacting {form_name}')
        contact.save()
        return render(request,'index.html')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))







def disclaimer(request):
    return render(request,'myblog/disclaimer.html')

def tag(request,id):
    posts=Post.objects.filter(tags=id)
    tag_name=Tag.objects.get(id=id)
    page = request.GET.get('page')
    paginator = Paginator(posts, 4)
    try:
        pro = paginator.page(page)
    except PageNotAnInteger:
        pro = paginator.page(1)
    except EmptyPage:
        pro = paginator.page(paginator.num_pages)

    return render(request,'myblog/tag.html',context={'posts':posts,'tag':tag_name,'pro':pro})

def createPost(request):
    form=PostForm()
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts')



    context={'form':form}
    return render(request,'myblog/post_form.html',context)


@login_required(login_url='home')
def updatePost(request,id):
    post_update=Post.objects.get(id=id)
    form=PostForm(instance=post_update)
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=post_update)
        if form.is_valid():
            form.save()
        return redirect('posts')



    context={'form':form}
    return render(request,'myblog/post_form.html',context)



@login_required(login_url='home')
def deletePost(request,id):
    post=Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')

    context={'item':post}
    return render(request,'myblog/delete.html',context)


def search(request):
    query=request.GET['search']
    if len(query) > 78:
        post=Post.objects.none()
        project=ExploreProject.objects.none()
        allproject=post.union(project)

    else:
        allpostquery = Post.objects.filter(Q(title__contains=query)|Q(tags__name__icontains=query))
        allprojectquery = ExploreProject.objects.filter(Q(title__contains=query)|Q(type__name__icontains=query))
        allproject=allpostquery.union(allprojectquery)

    if allproject.count() == 0:
        messages.warning(request,'No Search Result Found')
    context={'posts':allproject,'query':query}
    return render(request,'myblog/search.html',context)

