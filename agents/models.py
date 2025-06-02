from django.db import models

class Agent(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    title = models.CharField(max_length=200)
    api_url = models.URLField()

    def __str__(self):
        return self.title

    def iframe_code(self):
        return (
            '<div style="position:relative; width:100%; height:100%; overflow:hidden;">'
            '  <iframe src="https://vitoria.simpleway.tech/{id}/" '
            '          style="position:absolute; top:0; left:0; width:100%; height:100%; '
            '                 border:none; overflow:hidden;" '
            '          allowfullscreen>'
            '  </iframe>'
            '</div>'
        ).format(id=self.id)
    iframe_code.short_description = "Código do Iframe"
