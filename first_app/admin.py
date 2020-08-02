from django.contrib import admin
from first_app.models import  Topic, WebPage,Access_Record,Employee, UserProfileInfo,Post

class PostInline(admin.StackedInline):
    model = Post
    extra = 4

class TopicAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Topic Description', {'fields': ['top_name']}),
        ('Topic information', {'fields': ['top_desc']}),
    ]
    inlines = [PostInline]

# Register your models here.

#admin.site.register(AccessRecord)
admin.site.register(Topic, TopicAdmin)
admin.site.register(WebPage)
admin.site.register(Access_Record)
admin.site.register(Employee)
admin.site.register(UserProfileInfo)
admin.site.register(Post)
