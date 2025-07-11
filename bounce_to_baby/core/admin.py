from django.contrib import admin
from .models import User,FAQ,JournalEntry

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('username','email','pregnacy_start_date','age','location')
    search_fields=('username','email')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display=('question','topic')
    search_fields=('question','topic')

@admin.register(JournalEntry)
class JournalAdmin(admin.ModelAdmin):
    list_display=('user','mood','created_at')
    list_filter=('mood','created_at')