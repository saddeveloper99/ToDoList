from django.urls import path
from users.views import SignUpView

urlpatterns = [
    path('', SignUpView.as_view(), name='sign_up_view'),

]
