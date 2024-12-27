from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

challenge_dict = {
    "january": "Eat no meat for entire month",
    "febuary": "walk 20 minutes every day",
    "march": "learn django 20 minutes every day",
    "april": "learn C++ 20 minutes every day", 
    "may": "learn azure 20 minutes every day", 
    "june": "learn Automation python 20 minutes every day", 
    "july": "swim 20 minutes every day", 
    "august": "jogg 20 minutes every day", 
    "september": "weight training 20 minutes every day", 
    "october": "pillates training 20 minutes every day", 
    "november":"lessmills training 20 minutes every day", 
    "december": None
}

def index(request):
    #list_items = ""
    months = list(challenge_dict.keys())

    """
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>" 
    response_data  = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data) """

    return render(request, "challenges/index.html", {
        "months":months
        })


def monthly_challenge_by_number(request, month):
    months = list(challenge_dict.keys())

    # Handle invalid month
    if 1 <= month <= len(months):
        redirect_month = months[month - 1]
        redirect_url = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_url)
    else:
        # Redirect to a custom 404 page
        return render(request, '404.html', {'message': f"Month {month} doesn't exist!"}, status=404)

def monthly_challenge(request, month):
    try:
        challenge_text = challenge_dict[month]
        #response_data = f"<h1>{challenge_text}</h1>"
        #response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {"text":challenge_text, "month_name": month})
    
    except KeyError:
        return render(request, '404.html', {'message': f"<h2>Challenge for {month} does not exist!</h2>"}, status=404)
