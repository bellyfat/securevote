from django.conf.urls import url, include
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import views as auth_views

from .views import IndexPageView

admin_required = user_passes_test(
    lambda u: u.is_superuser,
    login_url='/accounts/login/'
)

urlpatterns = [
    url(r'^$',
    IndexPageView.as_view(),
    name='index_page'),
]
