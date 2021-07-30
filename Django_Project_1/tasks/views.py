from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label='New Task')
    priority = forms.IntegerField(label='Priority', min_value=1 ,max_value=10 )


def index(request):
    # To clear the cache (clear showing tasks)
    # request.session.clear()
    if "tasks" not in request.session:
        request.session['tasks'] = []
        request.session['priorities'] = []
    zipped = zip(request.session['tasks'], request.session['priorities'])
    return render(request, "tasks/index.html", {
        "zipped" : zipped
    } )


def add(request):
    if request.method=="POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            priority = form.cleaned_data['priority']
            request.session['tasks'] += [task]
            request.session['priorities'] += [priority]
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, 'tasks/add.html', {
                'form' : form
            })
    return render (request, 'tasks/add.html', {
        'form': NewTaskForm()
    })
