from django.shortcuts import render, redirect
from .form import RegistrationForm
from .models import UserProfile
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(user=user, bio=form.cleaned_data['bio'])
            profile.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})


class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'user/profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user.userprofile

