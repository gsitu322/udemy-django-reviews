from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ReviewForm
from django.views import View

# Create your views here.
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            'form': form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return HttpResponseRedirect(reverse("thank_you"))

        return render(request, "reviews/review.html", {
            'form': form
        })

# Changed to use a class based view
# def review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             print(form.cleaned_data)
#             return HttpResponseRedirect(reverse("thank_you"))
#     else:
#         form = ReviewForm()
#
#     return render(request, "reviews/review.html", {
#         'form' : form
#     })

class ThankYouView(View):
    def get(self, request):
        return render(request, "reviews/thank_you.html")