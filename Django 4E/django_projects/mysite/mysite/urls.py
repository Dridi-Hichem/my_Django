"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import pathlib

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path, re_path
from django.views.generic.base import TemplateView
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    re_path(r"^oauth/", include("social_django.urls", namespace="social")),
    # application urls
    path("", TemplateView.as_view(template_name="home/main.html")),
    path("polls/", include("polls.urls")),
    path("hello/", include("hello.urls")),
    path("autos/", include("autos.urls")),
    path("cats/", include("cats.urls")),
    path("ads/", include("ads.urls")),
]

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

# serve the static html files
urlpatterns += [
    re_path(
        r"^site/(?P<path>.*)$",
        serve,
        {"document_root": BASE_DIR / "site", "show_indexes": True},
        name="site",
    ),
]

# serve the favicon
urlpatterns += [
    path(
        "favicon.ico",
        serve,
        {"path": "favicon.ico", "document_root": BASE_DIR / "home/static"},
    ),
]

# switch to social login if it is configured
try:
    from . import github_settings
    social_login = "registration/login_social.html"
    urlpatterns.insert(
        0,
        path(
            "accounts/login/",
            auth_views.LoginView.as_view(template_name=social_login),
        ),
    )
    print(f"Using {social_login} as the login template")

except:
    print("Using registration/login.html as the login template")
