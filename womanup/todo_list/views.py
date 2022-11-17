from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoList



def index(request):
    tasks = TodoList.objects.all()
    if request.method == "POST": #проверяем то что метод именно POST
        if "Add" in request.POST: #проверяем метод добавления todo
            title = request.POST["title"] #сам текст
            date = str(request.POST["date"]) #дата, до которой должно быть закончено дело
            content = request.POST["description"] # полный склеенный контент
            Todo = TodoList(title=title, content=content, finished_date=date)
            Todo.save() # сохранение нашего дела
        if "Delete" in request.POST: #если пользователь собирается удалить одно дело
            checkedlist = request.POST.getlist('checkedbox') # берем список выделенные дел, которые мы собираемся удалить
            TodoList.objects.filter(id__in=[int(_id) for _id in checkedlist]).delete()
    
    return render(request, 'index.html', {"tasks": tasks})
