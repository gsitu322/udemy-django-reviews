from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ReviewForm
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import Review


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

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"

        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # Can Filter down the list of retrieved items
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=3)
    #     return data

class ReviewDetailView(TemplateView):
    template_name = "reviews/review_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["review"] = Review.objects.get(id=kwargs["id"])
        return context