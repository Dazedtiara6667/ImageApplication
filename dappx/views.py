# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from dappx.forms import UserForm,UserProfileInfoForm,CommentForm,AlbumForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .models import UserProfileInfo,Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView
from dappx.models import Album, AlbumImage
from zipfile import ZipFile
import zipfile
@login_required
def albumupload(request):
    if request.method=='POST':
        album_form = AlbumForm(request.POST,request.FILES)
        if album_form.is_valid():
            album_form.save()
    else:
        album_form=AlbumForm()
    
    
    return render(request,'dappx/album_upload.html',{'album_form':album_form})

@login_required
def gallery(request):
        user_list = Album.objects.all()
        paginator = Paginator(user_list, 10)
        page = request.GET.get('page',1)
        try:
            albums = paginator.page(page)
        except PageNotAnInteger:
            albums = paginator.page(1) 
        except EmptyPage:
            albums = paginator.page(paginator.num_pages) 

        return render(request, 'dappx/gallery.html', { 'albums': user_list })

class AlbumDetail(DetailView):
     model = Album
     def get_context_data(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the images
        context['images'] = AlbumImage.objects.filter(album=self.object.id)
        return context
@login_required
def comments(request): 
    comments = Comment.objects.all()
    comment_form = CommentForm(data=request.POST)
    new_comment = None
    if request.method == 'POST':
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,'dappx/comments.html',{'comments':comments,'new_comment':new_comment,'comment_form': comment_form})
def index(request):
    return render(request,'dappx/index.html')
@login_required
def special(request):
    return HttpResponse("You are Logged In !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'dappx/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dappx/login.html', {})
