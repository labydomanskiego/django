from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import News
from .models import News
from .forms import NewsForm, NewsModifyForm
from django.utils import timezone

def view_news(request):
    news = News.objects.order_by('-create_time')
    context = {'news': news}
    return render(request, 'news.html', context)

def add(request):
    if request.method == 'POST':
        news = NewsForm(request.POST)
        if news.is_valid():
            news = news.save(commit=False)
            news.create_time = timezone.now()
            news.last_edit_time = timezone.now()
            news.save()
            return redirect('view_news')
        else:
            context = {'form': news}
        return render(request, 'add.html', context)
    else:
        news = NewsForm()
    context = {'form': news}
    return render(request, 'add.html', context)

def get(request, id):
    news = get_object_or_404(News, id=id)
    context = {'news': news}
    return render(request, 'view.html', context)

def modify(request):
    if request.method == 'GET':
        news = NewsModifyForm()
        context = {'newsModifyForm': news}
        return render(request, 'modify.html', context)
    elif request.method == 'POST':
        news_form = NewsModifyForm(request.POST)
        if news_form.is_valid():
            news = news_form.cleaned_data['choice']
            news.text = news_form.cleaned_data['text']
            news.last_edit_time = timezone.now()
            news.save()
            return redirect('view_news')
        else:
            context = {'form': news_form}
        return render(request, 'modify.html', context)
    else:
        news = NewsForm()
    context = {'form': news}
    return render(request, 'modify.html', context)



