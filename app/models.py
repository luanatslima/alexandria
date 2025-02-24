from django.db import models

class MeuModelo(models.Model):
    image = models.ImageField(upload_to='images/')

class Material(models.Model):
    SLIDE = 'SL'
    VIDEO = 'VD'
    DOCUMENTO = 'DC'
    TIPO_CHOICES = [
        (SLIDE, 'Slide'),
        (VIDEO, 'Vídeo'),
        (DOCUMENTO, 'Documento'),
    ]
    
    autor = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(max_length=100)
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(
        max_length=2,
        choices=TIPO_CHOICES,
        default=DOCUMENTO,
    )
    arquivo = models.FileField(upload_to='meus_materiais/')

    def __str__(self):
        return self.titulo
    
