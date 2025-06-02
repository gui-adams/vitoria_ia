from django.contrib import admin
from django.utils.html import format_html
from .models import Agent

admin.site.site_header = "Painel de Controle Vitoria"
admin.site.site_title = "Vitoria Admin"
admin.site.index_title = "Bem-vindo ao Painel da Vitoria"

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "api_url_link",
        "preview_link",
        "show_iframe_code",
    )
    list_display_links = ("title",)
    search_fields = ("id", "title")
    list_filter = ("title",)
    ordering = ("title",)
    list_per_page = 25

    readonly_fields = ("show_iframe_code",)

    fields = (
        ("id", "title"),
        "api_url",
        "show_iframe_code",
    )

    def api_url_link(self, obj):
        """
        Exibe a api_url como um link clicável que abre em nova aba.
        """
        if obj.api_url:
            return format_html(
                '<a href="{}" target="_blank" style="text-decoration:none;">{}</a>',
                obj.api_url,
                obj.api_url,
            )
        return "-"
    api_url_link.short_description = "API URL"
    api_url_link.admin_order_field = "api_url"

    def preview_link(self, obj):
        """
        Gera um link que abre o iframe do agente em uma nova aba, para visualização rápida.
        """
        url = f"https://vitoria.simpleway.tech/{obj.id}/"
        return format_html(
            '<a href="{}" target="_blank" style="padding:4px 8px; '
            'background:#007bff;color:white;border-radius:4px;text-decoration:none;">'
            'Visualizar</a>',
            url,
        )
    preview_link.short_description = "Pré-visualizar"

    def show_iframe_code(self, obj):
        """
        Exibe o código completo do iframe dentro de um textarea para facilitar a cópia.
        """
        code = obj.iframe_code()
        return format_html(
            '<textarea rows="4" cols="60" readonly style="font-family:monospace; '
            'background:#f5f5f5;border:1px solid #ccc;padding:4px;">'
            "{}"
            "</textarea>",
            code,
        )
    show_iframe_code.short_description = "Copiar código do iframe"

    class Media:
        css = {
            "all": ("admin/css/custom_admin.css",),
        }
