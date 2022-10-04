from django.contrib.admin.apps import AdminConfig


class FirstDjangoProjectConfig(AdminConfig):
    default_site = 'first_django_project.admin.FirstDjangoProjectAdminSite'
