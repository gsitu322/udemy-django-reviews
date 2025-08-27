from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ReviewForm

# Create your views here.

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return HttpResponseRedirect(reverse("thank_you"))
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        'form' : form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")