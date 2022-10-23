from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from jedzenie.forms import JedzenieForm, JedzenieModifyForm
from jedzenie.models import Jedzenie


def view_jedzenie(request):
    jedzenie = Jedzenie.objects.order_by('-create_time')
    context = {'jedzenie': jedzenie}
    return render(request, 'jedzenie/jedzenie.html', context)

def add_jedzenie(request):
    if request.method == 'POST':
        jedzenie = JedzenieForm(request.POST)
        if jedzenie.is_valid():
            jedzenie = jedzenie.save(commit=False)
            jedzenie.create_time = timezone.now()
            jedzenie.last_edit_time = timezone.now()
            jedzenie.save()
            return redirect('view_jedzenie')
        else:
            context = {'form': jedzenie}
        return render(request, 'jedzenie/add.html', context)
    else:
        jedzenie = JedzenieForm()
    context = {'form': jedzenie}
    return render(request, 'jedzenie/add.html', context)

def delete_jedzenie(request, id):
    if request.method == 'POST':
        jedzenie = get_object_or_404(Jedzenie, id=id)
        jedzenie.delete()
    return redirect('view_jedzenie')

def get_jedzenie(request, id):
    jedzenie = get_object_or_404(Jedzenie, id=id)
    context = {'jedzenie': jedzenie}
    return render(request, 'jedzenie/view.html', context)


def modify_jedzenie(request):
    if request.method == 'GET':
        jedzenie_form = JedzenieModifyForm()
        context = {'jedzenieModifyForm': jedzenie_form}
        return render(request, 'jedzenie/modify.html', context)
    elif request.method == 'POST':
        jedzenie_form = JedzenieModifyForm(request.POST)
        if jedzenie_form.is_valid():
            jedzenie = jedzenie_form.cleaned_data['choice']
            jedzenie.kcal = jedzenie_form.cleaned_data['kcal']
            jedzenie.smaczne = jedzenie_form.cleaned_data['smaczne']
            jedzenie.last_edit_time = timezone.now()
            jedzenie.save()
            return redirect('view_jedzenie')
        else:
            context = {'form': jedzenie_form}
        return render(request, 'modify.html', context)
    else:
        jedzenie = JedzenieForm()
    context = {'form': jedzenie}
    return render(request, 'jedzenie/modify.html', context)
