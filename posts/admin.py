from django.contrib import admin

# Register your models here.
from .models import Post, City, Tag, House, UserProfile, Tenant, Subletter, PostTag, Address

class PostTagInline(admin.TabularInline):
    model = PostTag
    #what is extra?
    extra = 1

class PostModelAdmin(admin.ModelAdmin):
    #tags cannot be included because many to many
    list_display = ["title", "user", "house", "get_tags", "created_timestamp",
                    "last_updated"]

    list_filter = ["user", "house", "tags"]

    search_fields = ["user", "house", "tags"]

    inlines = (PostTagInline,)

    class Meta:
        model = Post


class CityModelAdmin(admin.ModelAdmin):
    list_display = ["name", "last_updated", "created_timestamp"]
    list_editable = ["name"]
    list_filter = ["last_updated", "created_timestamp"]

    search_fields = ["name"]
    class Meta:
        model = City

class AddressModelAdmin(admin.ModelAdmin):
    list_display = ["street", "city", "created_timestamp", "last_updated"]
    list_editable = ["street", "city"]
    list_filter = ["street", "city", "created_timestamp", "last_updated"]

    search_fields = ["street", "city", "created_timestamp", "last_updated"]
    class Meta:
        model = Address

class TagModelAdmin(admin.ModelAdmin):
    list_display = ["name", "content"]
    list_editable =["name", "content"]
    list_filter = ["name"]

    search_fields = ["name", "content"]
    class Meta:
        model = Tag

class HouseModelAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "title", "content", "address",
                    "price", "beds", "baths", "pet_allowed",
                    "has_parking", "has_laundry", "has_pool",
                    "created_timestamp", "last_updated"]

    list_filter = ["address", "created_timestamp"]

    search_fields = ["address"]
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
admin.site.register(Address, AddressModelAdmin)
admin.site.register(Tag, TagModelAdmin)
admin.site.register(House, HouseModelAdmin)
admin.site.register(UserProfile, UserProfileModelAdmin)
admin.site.register(Tenant, TenantModelAdmin)
admin.site.register(Subletter, SubletterModelAdmin)
admin.site.register(Post, PostModelAdmin)



