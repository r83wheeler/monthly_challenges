from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 1 hour every day!",
    "april": "Run 5 miles every other day!",
    "may": "Excercise everyother day!",
    "june": "Read for 45 minutes every day!",
    "july": "Learn MySQL for at least 1 hour every day!",
    "august": "Learn Scientific Python for at least 1 hour every day!",
    "september": "Train for a marathon",
    "october": "Learn React.js for at least 1 hour every day!",
    "november": "Make at least 1 commit to GitHub every day!",
    "december": "build a responsive website"
}
# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
    
