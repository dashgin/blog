# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.urls import reverse_lazy
# from django.views.generic import TemplateView, DeleteView, DetailView
#
# from accounts.models import CustomUser
#
#
# class LoginSignupView(TemplateView):
#     template_name = 'account/signup_login.html'
#
#
# class ProfileView(DetailView):
#     model = CustomUser
#     template_name = 'account/profile.html'
#
#
# class ProfileSettingsView(DetailView):
#     model = CustomUser
#     template_name = 'account/profile_settings.html'
#
#
# class AccountDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = CustomUser
#     template_name = 'account/account_delete.html'
#     success_url = reverse_lazy('home')
#
#     def test_func(self):
#         user = self.get_object()
#         if self.request.user == user:
#             return True
#         return False