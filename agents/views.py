from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Agent
import requests
import json
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/login/')
def dashboard(request):
    agents = Agent.objects.all()
    return render(request, "agents/dashboard.html", {"agents": agents})

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Agent
import requests

@csrf_exempt
def agent_proxy(request, id):
    agent = Agent.objects.get(pk=id)
    if request.method == "POST":
        question = request.POST.get("question")
        file = request.FILES.get("file")
        
        files = None
        data = {}
        if question:
            data["question"] = question
        if file:
            files = {'file': (file.name, file.read(), file.content_type)}
        
        try:
            r = requests.post(agent.api_url, data=data, files=files)
            return JsonResponse(r.json(), status=r.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Only POST allowed"}, status=405)


def agent_page(request, id):
    agent = get_object_or_404(Agent, pk=id)
    return render(request, "agents/agent.html", {"agent": agent})
