from django.shortcuts import render
from .models import Chat


def index(request):
    return render(request, 'index.html')


def room(request):
    room_no = request.POST['room_no']
    name = request.POST['name']
    messages = Chat.objects.filter(room_no=room_no)
    content = {'room': room_no,
               'name': name,
               'messages': messages}
    return render(request, 'room.html', content)
