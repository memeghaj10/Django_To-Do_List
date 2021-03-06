from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
	if request.method == "POST":
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
		else:
			pass
		all_items = List.objects.all
		messages.success(request,('Item has been Added to list!'))
		return render(request,'home.html',{'todo_items':all_items})
		
	else:
		all_items=List.objects.all
		return render(request,'home.html',{'todo_items':all_items})



def delete(request,item_id):
	item=List.objects.get(pk=item_id)
	item.delete()
	messages.success(request,('Item has been deleted!'))
	return redirect('home')


def about(request):
    my_name = "Anthony Bonello"
    number = 2 + 2
    context = {'name': my_name, 'number': number}
    return render(request, 'about.html', context)

def cross_off(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = True
    item.save()
    messages.success(request, ('Item has been marked as completed.'))
    return redirect('home')

def uncross(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = False
    item.save()
    messages.success(request, ('Item has been marked as not completed.'))
    return redirect('home')

def edit(request, item_id):
    if request.method == 'POST':
        item = List.objects.get(pk=item_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been successfully edited.'))
            return redirect('home')
    else: 
        item = List.objects.get(pk=item_id)
        return render(request, 'edit.html', {'item': item})