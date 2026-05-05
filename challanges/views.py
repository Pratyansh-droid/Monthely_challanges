from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthely_challenges = {
    "january": "No Junck food for the entire month..",
    "february": "Walk at least 20 minutes every day...",
    "march": "Learn Django for at least 20 minutes every day...",
    "april": "Do Exercise at least 10 minutes every day",
    "may": "Learn new skill and pratice every day",
    "june": "Drink sufficient amount of water",
    "july": "Build communication skill",
    "august": "Learn Django for at least 20 minutes every day...",
    "september": "Go for a walk",
    "october": "Go to a trip",
    "november": "enjoy....play",
    "december": None
}

def index(request):
    months = list(monthely_challenges.keys())
    return render(request, "challanges/index.html", {"months": months})

def monthely_challenge_by_number(request, month):
    months = list(monthely_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Credential!!!</h1>")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challange", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthely_challenge(request, month):
    try:
        challenge_text = monthely_challenges[month]
        return render(request,"challanges/challange.html", {"text": challenge_text, "month_name": month})
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
