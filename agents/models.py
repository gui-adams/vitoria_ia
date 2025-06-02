from django.db import models
from django.utils.html import format_html

class Agent(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    title = models.CharField(max_length=200)
    api_url = models.URLField()

    def __str__(self):
        return self.title

    def iframe_code(self):
        return format_html(
            '<iframe src="https://vitoria.simpleway.tech/{id}/" '
            'style="width:100%; height:100%; border:none; display:block;" '
            'allowfullscreen>'
            '</iframe>',
            id=self.id
        )
    iframe_code.short_description = "Código do Iframe"
