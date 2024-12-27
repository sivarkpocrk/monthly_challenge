from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

challenge_dict = {
    "january": "Eat no meat for entire month",
    "febuary": "walk 20 minutes every day",
    "march": "learn django 20 minutes every day",
    "April": "learn C++ 20 minutes every day", 
    "May": "learn azure 20 minutes every day", 
    "June": "learn Automation python 20 minutes every day", 
    "July": "swim 20 minutes every day", 
    "August": "jogg 20 minutes every day", 
    "September": "weight training 20 minutes every day", 
    "October": "pillates training 20 minutes every day", 
    "November":"lessmills training 20 minutes every day", 
    "December": "party XMAS and New Year Celebration"
}

def monthly_challenge_by_number(request, month):
    months = list(challenge_dict.keys())

    # Handle invalid month
    if 1 <= month <= len(months):
        redirect_month = months[month - 1]
        return HttpResponseRedirect(f"/challenges/{redirect_month}")
    else:
        # Redirect to a custom 404 page
        return render(request, '404.html', {'message': f"Month {month} doesn't exist!"}, status=404)

def monthly_challenge(request, month):
    try:
        challenge_text = challenge_dict[month]
        return HttpResponse(challenge_text)
    except KeyError:
        return render(request, '404.html', {'message': f"Challenge for {month} does not exist!"}, status=404)
