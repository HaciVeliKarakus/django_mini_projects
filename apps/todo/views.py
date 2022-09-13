from django.contrib import messages
from django.shortcuts import render, redirect

from apps.todo.forms import TodoModelForm
from apps.todo.models import Todo


def index(request):
    item_list = Todo.objects.order_by("-created_date")
    if request.method == "POST":
        form = TodoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoModelForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')
