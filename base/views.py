from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm


'''rooms = [
    {'id':1, 'name' : 'Lets learn Python'},
    {'id':2, 'name' : 'Design with me'},
    {'id':3, 'name' : 'Frontends developpers'},
]'''



def home(request):
    rooms = Room.objects.all()
    context = {'rooms' : rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST': #check if form
        form = RoomForm(request.POST) #add data to form
        if form.is_valid():#check if valid data
            form.save() #save data
            return redirect('home') #redirect user to homepage
    
    context = {'form':form}
    return render(request,'base/room_form.html', context)


def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room) #empty form prefilled with data from the room object (the instance specify which one)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'base/room_form.html', context)
