from django.shortcuts import render, redirect

from . import util
from .forms import CreatePageForm
from .util import get_entry, save_entry


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, titles):
    body = get_entry(titles)
    return render(request, 'encyclopedia/entry.html', {
        "Ttitle": titles,
        'body': body
    })


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
    
