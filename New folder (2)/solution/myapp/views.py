from django.shortcuts import render,redirect
from .models import MyModel
from .forms import ImageForm,UserCreationForm
from django.urls import reverse
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import openai
from django.views.decorators.csrf import csrf_exempt
import json
import os
from django.http import JsonResponse
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
# @login_required(login_url='login')
def index(request):
    myitems = MyModel.objects.all()
    return render(request,'index.html',{"myitems": myitems})


# @csrf_exempt
# def contact_api(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         name = data.get('name')
#         email = data.get('email')
#         message = data.get('message')
#         subject = f"New Contact from {name}"

#         full_message = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"

#         try:
#             send_mail(
#                 subject,
#                 full_message,
#                 'your_email@gmail.com',            # From
#                 ['receiver_email@gmail.com'],      # To
#                 fail_silently=False,
#             )
#             return JsonResponse({'message': 'Message sent successfully!'})
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)

#     return JsonResponse({'error': 'Invalid request method'}, status=400)
# from django.shortcuts import render
# # from django.http import HttpResponse
# from django.http import JsonResponse
# # from .models import MyModel
# from django.views.decorators.csrf import csrf_exempt
# import json
# # from .models import ImageModel

# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib.auth.models import User

# # Create your views here.
# # def index(request):
# #     return render(request,'index.html')
# # views.py
# # def index(request):
# #     return render(request, 'index.html', {
# #         'image_url': '/media/unnamed.jpg'
# #     })

# def image_gallery(request):
#     images = MyImage.objects.all()
#     return render(request, 'myapp/gallery.html', {'images': images})

# # def index(request):
# #     myitems = MyModel.objects.all()
# #     return render(request,'index.html',{"myitems": myitems})

# # @csrf_exempt
# # def contact_form(request):
# #     if request.method == 'POST':
# #         try:
# #             data = json.loads(request.body)
# #             name = data.get('name')
# #             email = data.get('email')
# #             message = data.get('message')

# #             # Aapke mobile email ke liye (e.g., Airtel: 91XXXXXXXXX@airtelmail.com)
# #             send_mail(
# #                 subject=f"New Contact from {name}",
# #                 message=f"Name: {name}\nEmail: {email}\nMessage: {message}",
# #                 from_email=settings.DEFAULT_FROM_EMAIL,
# #                 recipient_list=['your-email@gmail.com'],  # 👈 Yahan apna email/mobile email likho
# #                 fail_silently=False,
# #             )

# #             return JsonResponse({'message': 'Message sent successfully.'})
# #         except Exception as e:
# #             return JsonResponse({'error': str(e)}, status=400)
# #     return JsonResponse({'error': 'Invalid request method.'}, status=405)