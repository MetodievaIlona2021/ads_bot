from django.contrib import admin
from .models import User, Articles, Videos


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'name', 'username', 'created_at')


@admin.register(Articles)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'created_at')


@admin.register(Videos)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'thumb_url', 'url', 'created_at')
