# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from models import PostModel

def post_model_list_view(request):
    qs = PostModel.objects.all()
    template = 'blog/list-view.html'
    context = {
        'object_list': qs
    }
    return render(request, template, context)

