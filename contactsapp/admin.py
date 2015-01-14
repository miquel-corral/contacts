from django.contrib import admin

import contactsapp.models


# admin.site.register(contactsapp.models.Contact)


class TagAdmin(admin.ModelAdmin):
    list_filter = ('name',)


admin.site.register(contactsapp.models.Tag, TagAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'email1', 'telephone1', 'email1')
    list_filter = ('name', 'organization', 'email1', 'country', 'tags')
    fieldsets = (
        (None, {
            'fields': ('name', 'first_name', 'last_name', 'organization', 'department', 'position', 'telephone1',
                       'mobile1', 'mobile2', 'email1', 'email2', 'website')
        }),
        ('Address', {
            'classes': ('collapse',),
            'fields': ('state', 'country', 'city', 'street', 'zip_code')
        }),
    )


admin.site.register(contactsapp.models.Contact, ContactAdmin)