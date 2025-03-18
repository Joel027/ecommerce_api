from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords

# Create your models here.

class MeasureUnit(BaseModel):
    """Model to define the measure unit of the product"""
    
    description = models.CharField("Descripcion",max_length=50, unique=True, blank=False, null=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        
    def __str__(self):
        return self.description
    
    class Meta:
        db_table = 'unidades_medida'
        verbose_name = "Unidad de medida"
        verbose_name_plural = "Unidades de medida"
        
class CategoryProduct(BaseModel):
    """Model to define the category of the product"""
    
    description = models.CharField("Descripcion",max_length=50, unique=True, blank=False, null=False)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE,verbose_name="Unidad de medida")
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    def __str__(self):
        return self.description
    
    class Meta:
        db_table = 'categorias_productos'
        verbose_name = "Categoria de producto"
        verbose_name_plural = "Categorias de productos"


class Indicator(BaseModel):
    """Model to define the indicator of the product"""
    
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct,on_delete=models.CASCADE,verbose_name="Indicador de Oferta")
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
        
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        
    def __str__(self):
        return f'Oferta de la categoria {self.category_product} {self.descount_value} %'
    
    class Meta:
        db_table = 'indicadores'
        verbose_name = "Indicador de oferta"
        verbose_name_plural = "Indicadores de ofertas"


class Product(BaseModel):
    """Model to define the product"""
    
    name= models.CharField("Nombre del Producto",max_length=150, unique=True, blank=False, null=False)
    description = models.TextField("Descripcion del Producto",blank=False, null=False)
    image = models.ImageField("Imagen del Producto",upload_to="products/",blank=True, null=True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value
        
    def __str__(self):
        pass
    
    class Meta:
        db_table = 'productos'
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        
    
