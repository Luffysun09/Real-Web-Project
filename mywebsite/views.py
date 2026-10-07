import json
import os
import urllib.request

from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST


def home(request):
    return render(request, "index.html")


def success(request):
    return render(request, "success.html")


@require_POST
def contact(request):
    data = {
        "access_key": os.environ.get("WEB3FORMS_ACCESS_KEY"),
        "name": request.POST.get("name"),
        "email": request.POST.get("email"),
        "message": request.POST.get("message"),
    }

    request_data = json.dumps(data).encode("utf-8")

    web3forms_request = urllib.request.Request(
        "https://api.web3forms.com/submit",
        data=request_data,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(web3forms_request) as response:
            result = json.loads(response.read().decode("utf-8"))

        if result.get("success"):
            return redirect("success")

    except Exception:
        pass

    return redirect("home")
