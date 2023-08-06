from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm
from django.contrib import messages


class CustomLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class CustomPasswordResetView(PasswordResetView):
    success_url = reverse_lazy("password_reset_done")
    template_name = 'registration/custom_password_reset_form.html'
    email_template_name = 'registration/custom_password_reset_email.html'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "registration/custom_password_reset_done.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy("custom_password_reset_complete")
    template_name = "registration/custom_password_reset_confirm.html"


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    pass
    #template_name = "registration/my_password_reset_complete.html"


