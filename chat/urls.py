from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_page, name="login_page"),
    path("history/", views.history_page, name="history_page"),
    path("api/all_users/", views.all_users, name="all_users"),
    path("api/create_user/", views.create_user, name="create_user"),
    path("api/logout_user/", views.logout_user, name="logout_user"),
    path("api/all_messages/", views.all_messages, name="all_messages_api"),
    path("get_message/<int:message_id>/", views.get_message, name="get_message"),
    path("api/post_message/", views.post_message, name="post_message_api"),
]
