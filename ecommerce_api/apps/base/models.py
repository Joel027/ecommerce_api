from django.db import models

class BaseModel(models.Model):
    """Base model for all models"""
    id = models.AutoField(primary_key=True)
    state = models.BooleanField("Estado",default=True)
    created_date = models.DateTimeField('Fecha de creacion',auto_now_add=True, auto_now=False)
    modified_date = models.DateTimeField('Fecha de modificacion',auto_now_add=False, auto_now=True)
    deleted_date = models.DateTimeField('Fecha de eliminacion',auto_now_add=False, auto_now=False, null=True, blank=True)

    class Meta:
        abstract = True
        verbose_name = "Modelo base"
        verbose_name_plural = "Modelos base"
        
