import random

from django.shortcuts import render, redirect

from . import util
from .forms import CreatePageForm, EditForm
from .util import get_entry, save_entry


def index(request):
    if request.method == 'POST':
        q = request.POST.get('q')
        for i in util.list_entries():
            if q.casefold() == i.casefold():
                body = get_entry(title=q)
                return render(request, 'encyclopedia/entry.html', {
                    "my_title2": q,
                    'body': body
                })
        else:
            lists = []
            for j in util.list_entries():
                if q.casefold() in j.casefold():
                    lists.append(j)
        return render(request, "encyclopedia/index.html", {
            "entries": lists
        })

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, titles):
    if titles in util.list_entries():
        body = get_entry(titles)

        if request.method == 'GET':
            return render(request, 'encyclopedia/entry.html', {
                "my_title2": titles,
                'body': body
            })

    elif titles not in util.list_entries():
        return render(request, 'encyclopedia/error.html')


def create_new_page(request):
    if request.method == 'POST':
        form = CreatePageForm(request.POST)
        if form.is_valid():
            my_title2 = form.cleaned_data['title']
            my_content = form.cleaned_data['body']
            save_entry(title=my_title2, content=my_content)
            return redirect('index')

    return render(request, 'encyclopedia/create.html', {
        'my_form': CreatePageForm()

    })


def random_page(request):
    rando_page = random.choice(util.list_entries())
    body = get_entry(rando_page)
    return render(request, 'encyclopedia/entry.html', {
        "my_title2": rando_page,
        'body': body
    })


def edit(request, titl):
    form = EditForm(request.POST)
    if request.method == 'GET':
        body = get_entry(titl)
        return render(request, 'encyclopedia/edit.html', {
            'formy': EditForm(initial={"body": body, 'title': titl})
        })
    elif request.method == "POST" and form.is_valid():
        n_title = form.cleaned_data['title']
        titl = n_title
        n_body = form.cleaned_data['body']
        save_entry(n_title, n_body)
        body = get_entry(titl)
        return render(request, 'encyclopedia/entry.html', {
            "my_title2": titl,
            'body': body
        })
