from django.contrib import admin
from .models import Project, Contact, Register, Blogs, BlogComment

admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(Register)
admin.site.register((Blogs, BlogComment))
