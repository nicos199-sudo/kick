from django.contrib import admin

# Register your models here.
from home.models import ContactMessage,FAQ


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject', 'update_at','status']
    readonly_fields =('name','subject','email','message','ip')
    list_filter = ['status']
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer','ordernumber','status']
    list_filter = ['status']

admin.site.register(FAQ,FAQAdmin)
admin.site.register(ContactMessage,ContactMessageAdmin)