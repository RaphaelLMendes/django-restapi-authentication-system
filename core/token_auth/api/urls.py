from knox import views as knox_views
from core.token_auth.api.views import LoginView
from dj_rest_auth.views import UserDetailsView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ResendEmailVerificationView
from django.urls import path, re_path
from django.views.generic import TemplateView
from allauth.account.views import ConfirmEmailView

urlpatterns = [
    path(r"login/", LoginView.as_view(), name="knox_login"),
    path("password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    path(
        "password/reset/confirm/",
        PasswordResetConfirmView.as_view(),
        name="rest_password_reset_confirm",
    ),

    # URLs that require a user to be logged in with a valid session / token.
    path(r"logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path(r"logoutall/", knox_views.LogoutAllView.as_view(), name="knox_logoutall"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
    path("password/change/", PasswordChangeView.as_view(), name="rest_password_change"),

    # registration views

    path('registration/', RegisterView.as_view(), name='rest_register'),
    path('registration/verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('registration/resend-email/', ResendEmailVerificationView.as_view(), name="rest_resend_email"),

    # This url is used by django-allauth and empty TemplateView is
    # defined just to allow reverse() call inside app, for example when email
    # with verification link is being sent, then it's required to render email
    # content.

    # account_confirm_email - You should override this view to handle it in
    # your API client somehow and then, send post to /verify-email/ endpoint
    # with proper key.
    # If you don't want to use API on that step, then just use ConfirmEmailView
    # view from:
    # django-allauth https://github.com/pennersr/django-allauth/blob/master/allauth/account/views.py
    re_path(
        r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(),
        name='account_confirm_email',
    ),
    path(
        'registration/account-email-verification-sent/', ConfirmEmailView.as_view(),
        name='account_email_verification_sent',
    ),

    path(
        'registration/account-email-verification-sent/test/', TemplateView.as_view(),
        name='account_email',
    ),
    path(
        'registration/account-email-verification-sent/test/', TemplateView.as_view(),
        name='account_logout',
    ),

    path(
        'registration/account-email-verification-sent/test/', TemplateView.as_view(),
        name='account_login',
    ),

    path(
        'registration/account-email-verification-sent/test/', TemplateView.as_view(),
        name='account_signup',
    ),
]
