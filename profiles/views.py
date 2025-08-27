from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView

# Create your views here.

# Don't need this anymore as ProfileForm will save it for
# def store_file(file):
#     with open("temp/image.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)

class CreateProfileView(CreateView):
    template_name = 'profiles/create_profile.html'
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

    # Used for regular view
    # def get(self, request):
    #     return render(request, "profiles/create_profile.html", {
    #         "form" : ProfileForm()
    #     })
    #
    # def post(self, request):
    #     submitted_form = ProfileForm(request.POST, request.FILES)
    #
    #     if submitted_form.is_valid():
    #         profile = UserProfile(user_image=request.FILES['user_image'])
    #         profile.save()
    #
    #         return HttpResponseRedirect("/profiles")
    #
    #     return render(request, "profiles/create_profile.html", {
    #         "form" : submitted_form
    #     })