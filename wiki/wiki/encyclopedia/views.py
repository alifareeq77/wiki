import random

from django.shortcuts import render, redirect

from . import util
from .forms import CreatePageForm
from .util import get_entry, save_entry


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, titles):
    if titles in util.list_entries():
        body = get_entry(titles)
        return render(request, 'encyclopedia/entry.html', {
            "my_title": titles,
            'body': body
        })
    elif titles not in util.list_entries():
        return render(request, 'encyclopedia/error.html')


def create_new_page(request):
    if request.method == 'POST':
        form = CreatePageForm(request.POST)
        if form.is_valid():
            my_title = form.cleaned_data['title']
            my_content = form.cleaned_data['body']
            save_entry(title=my_title, content=my_content)
            return redirect('index')

    return render(request, 'encyclopedia/create.html', {
        'my_form': CreatePageForm()

    })


def random_page(request):
    random_item = random.choice(util.list_entries())
    body = get_entry(random_item)
    return render(request, 'encyclopedia/entry.html', {
        "my_title": random_item,
        'body': body
    })
