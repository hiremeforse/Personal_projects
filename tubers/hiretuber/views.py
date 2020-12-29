from django.shortcuts import render
from .models import Hiretuber

# Create your views here.


#   first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     tuber_id = models.CharField(max_length=100)
#     tuber_name = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     message = models.CharField(max_length=100, blank=True)
#     user_id = mode


def hiretuber(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    tuber_id = request.POST['tuber_id']
    tuber_name = request.POST['tuber_name']
    city = request.POST['city']
    phone = request.POST['phone']
    state = request.POST['state']
    message = request.POST['message']
    user_id = request.POST['user_id']

    hiretuber = Hiretuber(first_name=first_name, last_name=last_name,tuber_id=tuber_id,tuber_name=tuber_name,
                        city=city, phone=phone,state=state,message=message,user_id=user_id)
    hiretuber.save()
    message.success(request, 'Thnaks')
    return redirect('youtubers')