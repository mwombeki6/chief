from django.urls import path
from .views import (
    registerView,
    get_csrf,
    loginView,
    WhoAmIView,
    StaffOnlyView,
    check_auth,
    logoutView,
    update_account,
    delete_account
)

urlpatterns = [
    path("csrf_cookie", get_csrf),
    path("check_auth", check_auth),
    path("register", registerView),
    path("login", loginView),
    path("get_user", WhoAmIView.as_view()),
    path("staff_dashboard", StaffOnlyView.as_view()),
    path("logout", logoutView),
    path("update", update_account),
    path("delete", delete_account),
]
