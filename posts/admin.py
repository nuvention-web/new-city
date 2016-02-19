from django.contrib import admin

# Register your models here.
from .models import Post, City, Tag, House, UserProfile, Tenant, Subletter

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["user", "house", "title", "last_updated", "created_timestamp"]
    list_filter = ["user", "house", "tags"]

    search_fields = ["user", "house", "tags"]
    class Meta:
        model = Post

class CityModelAdmin(admin.ModelAdmin):
    list_display = ["name", "last_updated", "created_timestamp"]
    list_editable = ["name"]
    list_filter = ["last_updated", "created_timestamp"]

    search_fields = ["name"]
    class Meta:
        model = City

class TagModelAdmin(admin.ModelAdmin):
    list_display = ["name", "content"]
    list_editable =["name", "content"]
    list_filter = ["name"]

    search_fields = ["name", "content"]
    class Meta:
        model = Tag

class HouseModelAdmin(admin.ModelAdmin):
    list_display = ["subletter", "address", "created_timestamp", "last_updated"]
    list_filter = ["address", "created_timestamp"]

    search_fields = ["subletter", "address"]
    class Meta:
        model = House

class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ["user", "address", "created_timestamp", "last_updated", "last_active"]
    list_filter = ["user", "address"]

    search_fields = ["user", "address"]
    class Meta:
        model = UserProfile

class TenantModelAdmin(admin.ModelAdmin):
    list_display = ["profile"]
    class Meta:
        model = Tenant

class SubletterModelAdmin(admin.ModelAdmin):
    list_display = ["profile"]
    class Meta:
        model = Subletter

admin.site.register(City, CityModelAdmin)
admin.site.register(Tag, TagModelAdmin)
admin.site.register(House, HouseModelAdmin)
admin.site.register(UserProfile, UserProfileModelAdmin)
admin.site.register(Tenant, TenantModelAdmin)
admin.site.register(Subletter, SubletterModelAdmin)
admin.site.register(Post, PostModelAdmin)



