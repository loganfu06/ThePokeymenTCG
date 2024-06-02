from django.shortcuts import render

# Create your views here.

from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login

class CoreLoginView(LoginView):
    template_name = "core/login.html"
    def form_valid(self, form):
        """Security check complete. Log the user in."""
        user = form.get_user()
        auth_login(self.request, user)
        if user_need_to_go_to_otp:
            return redirect('otp_url')
        else:
            return else_where