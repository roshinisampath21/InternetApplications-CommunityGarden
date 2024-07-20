from django.contrib import admin

# Register your models here.
from django.contrib import admin
from garden_app.models  import CommunityGarden, Post


admin.site.register(CommunityGarden)
admin.site.register(Post)
