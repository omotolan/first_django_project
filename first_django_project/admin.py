from django.contrib import admin


class FirstDjangoProjectAdminSite(admin.AdminSite):
    site_title = "First Django Project Admin Site"
    site_header = "Welcome to the First Django Project Admin Interface"
    index_title = "First Django Project Index"