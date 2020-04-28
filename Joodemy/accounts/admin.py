from django.contrib import admin
from .models import User, Student, Instructor


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        'username',
        'email',
        'date_joined',
    )

    list_display_links = (
        'username',
        'email',
    )


admin.site.register(Student)
admin.site.register(Instructor)
