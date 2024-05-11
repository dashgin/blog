from django.contrib import admin

from .models import PostNewsletter, SubscribedUser


@admin.action(description="Send selected Newsletters to all subscribers")
def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)


@admin.register(PostNewsletter)
class NewsletterAdmin(admin.ModelAdmin):
    actions = [send_newsletter]


admin.site.register(SubscribedUser)
