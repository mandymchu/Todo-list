from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
import datetime
from todolist.models import Todo

def index(request):
	message = "Current time: {}".format(datetime.datetime.now())
	return HttpResponse(message)

# create a class for testing
# class Todo:
# 	def __init__(self, title, completed):
# 		self.title = title
# 		self.completed = completed

def todo_list(request):
	# for testing
	# list = []
	# for value in range(10):
	# 	list.append(Todo("task" + str(value), False))
    
    if request.method == 'POST':  # POST 方法要大写字母
    	action = request.POST.get('action')
    	if action == 'add':
    		t = request.POST.get('title')
    		Todo.objects.create(title=t)

    list = Todo.objects.all()
    return render(request, 'todolist.html', locals()) # locals()将上面的打包

def complete(request, pk):
	todo_item = get_object_or_404(Todo, id=pk)
	todo_item.completed = True
	todo_item.save()
	return HttpResponseRedirect('/')

def delete(request, pk):
	todo_item = get_object_or_404(Todo, id=pk)
	todo_item.delete()
	return HttpResponseRedirect('/')

	