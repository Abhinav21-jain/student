# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404, redirect
from .models import Poll
from news.models import News
# Create your views here.

def home(request):

    site = Poll.objects.get(pk=2)
    news = News.objects.all()

    return render(request,'front/home.html',{'site':site, 'news':news})


def about(request):

    site = Poll.objects.get(pk=2)

    return render(request,'front/about12.html',{'site':site})

def panel(request):

    return render(request,'back/home.html')

