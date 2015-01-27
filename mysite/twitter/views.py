# coding=utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from twitter.models import User
class UserFormLogin(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput())
class UserForm(forms.Form): 
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    fullname = forms.CharField(label='fullname', max_length=50)
    email = forms.CharField(label='email', max_length= 50)

def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            fullname = uf.cleaned_data['fullname']
            email = uf.cleaned_data['email']
            User.objects.create(username=username,
                                password=password,
                                fullname=fullname,
                                email=email)
            return HttpResponse('regist success!! <a href="http://127.0.0.1:8000/twitter/login/">login</a>')
    else:
        uf = UserForm()
    return render_to_response('regist.html', {'uf':uf}, context_instance=RequestContext(req))

def login(req):
    if req.method == 'POST':
        uf = UserFormLogin(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                response = HttpResponseRedirect('/twitter/index/')
                response.set_cookie('username', username, 3600)
                return response
            else:
                return HttpResponse('login error! username or password is wrong! <a href="http://127.0.0.1:8000/twitter/login/">login again</a>')
    else:
        uf = UserFormLogin()
    return render_to_response('login.html', {'uf':uf}, context_instance=RequestContext(req))

def index(req):
    username = req.COOKIES.get('username', '')
    return render_to_response('index.html' , {'username':username})

def logout(req):
    response = HttpResponse('logout !!')
    response.delete_cookie('username')
    return response
