from django.http import HttpResponse
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html", { 
        "entry": util.get_entry(title),
        "title": title
        })

def custom_page_not_found(request, exception):
    return render(request, "encyclopedia/404.html", status=404)