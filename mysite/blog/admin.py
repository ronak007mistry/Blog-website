from django.contrib import admin
from blog.models import Post, BlogComment

admin.site.register((BlogComment))

class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/admin/tinyInject.js',)

admin.site.register(Post, PostAdmin)
