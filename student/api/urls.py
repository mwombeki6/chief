from django.urls import path
from .views import (
    registerView,
 
    get_csrf,
    loginView,
    WhoAmIView,
    StudentOnlyView,
    check_auth,
    logoutView,
    getSession
)

urlpatterns = [
    path("sessionId", getSession.as_view()),
    path("csrf_cookie", get_csrf),
    path("check_auth", check_auth),
    path("register", registerView),
    path("login", loginView),
    path("get_user", WhoAmIView.as_view()),
    path("student_dashboard", StudentOnlyView.as_view()),
    path("logout", logoutView),
]
