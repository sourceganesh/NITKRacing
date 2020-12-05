from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from .models import *


class BannerAdmin(admin.ModelAdmin):
    list_display = ['small_text', 'large_text', 'page_to_display']


def mail_pitstop(modeladmin, request, queryset):
    mail_pitstop.short_description = "Email Selected pitstop edition"
    email_list = [subscriber.email for subscriber in Subscribers.objects.all()]
    message = "Greetings from NITKRacing Electric, \n enclosed below is a copy of Pitstop our monthly newsletter" \
              "\n%s\nRegards,\nNITKRacing Electric"
    for ps in queryset:
        send_mail('Pitstop Newsletter', message % ps.link, settings.EMAIL_HOST_USER, email_list, fail_silently=False)


class PitstopAdmin(admin.ModelAdmin):
    list_display = ['edition']
    actions = [mail_pitstop]


# Register your models here.
admin.site.register(Sponsor)
admin.site.register(Image)
admin.site.register(Member)
admin.site.register(Blog)
admin.site.register(Document)
admin.site.register(Subscribers)
admin.site.register(Pitstop, PitstopAdmin)
admin.site.register(Banner, BannerAdmin)
