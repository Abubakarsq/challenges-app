from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
all_monthly_challenges = {
    'January': 'Plan the team outing',
    'February': 'Update the website',
    'March': 'Host a webinar',
    'April': 'Prepare for the quarterly review',
    'May': 'Conduct a customer survey',
    'June': 'Launch the marketing campaign',
    'July': 'Write blog posts',
    'August': 'Organize the office space',
    'September': 'Finalize the budget',
    'October': 'Attend a conference',
    'November': 'Develop a new feature',
    'December': 'Complete the annual report'
}


def challenge_pages(request):
    months = list(all_monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_page(request, month):
    if month.capitalize() in all_monthly_challenges:
        return render(request, "challenges/challenge.html", {"month": month.capitalize(), "task": all_monthly_challenges.get(month.capitalize())})
    else:
        raise Http404("<h1>Sorry Page Not Found!</h1>")


def monthly_challenge_page_with_number(request, month):
    months = list(all_monthly_challenges.keys())
    if month <= len(months):
        redirect_url = reverse("month", args=[months[month-1]])
        return HttpResponseRedirect(redirect_url)
    else:
        raise Http404()

