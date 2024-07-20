from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProfileEditForm, UserEditForm
from .models import Profile


@login_required
def profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    context = {"profile": profile}
    return render(request, "accounts/profile.html", context)


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, "Profile updated successfully")

            return redirect("accounts:profile")
        else:
            messages.error(request, "Error updating your profile")

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {"user_form": user_form, "profile_form": profile_form}
    return render(request, "accounts/edit.html", context)
