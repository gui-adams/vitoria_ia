from django.contrib import admin
from .models import Agent
from django.utils.html import format_html

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'api_url', 'show_iframe_code')
    search_fields = ('id', 'title')
    readonly_fields = ('show_iframe_code',)

    def show_iframe_code(self, obj):
        return format_html(
            '<textarea rows="3" cols="50" readonly>{}</textarea>', 
            obj.iframe_code()
        )
    show_iframe_code.short_description = "Copie o código do iframe"
