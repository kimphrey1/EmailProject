from django.shortcuts import render, redirect
from django.http import FileResponse
from django.conf import settings
import os
import openpyxl
from .models import Recipient, CCRecipient
# from .forms import EmailForm
import win32com.client as win32

# Create your views here.

def home_view(request):
    return render (request, 'test.html')

