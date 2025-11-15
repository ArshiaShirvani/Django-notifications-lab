from django.shortcuts import render, redirect
from django.contrib import messages
import json

def index(request):
    return render(request, 'notifications.html')

def send_notification(request):
    if request.method == "POST":
        title = request.POST.get("title", "پیام")
        text = request.POST.get("message", "")
        footer = request.POST.get("footer", "")
        msg_type = request.POST.get("message_type", "info")

        # پیام را در قالب دیکشنری JSON می‌سازیم
        msg_content = json.dumps({
            "title": title,
            "text": text,
            "footer": footer,
            "type": msg_type
        })

        messages.add_message(request, messages.INFO, msg_content)

    return redirect('website:index')
