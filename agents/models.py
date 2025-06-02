from django.db import models

class Agent(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    title = models.CharField(max_length=200)
    api_url = models.URLField()

    def __str__(self):
        return self.title

    def iframe_code(self):
        return f'<iframe src="https://SEU_DOMINIO/agent/{self.id}/" width="400" height="600"></iframe>'
    iframe_code.short_description = "Código do Iframe"
