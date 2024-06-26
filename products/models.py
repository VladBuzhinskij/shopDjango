from django.db import models

# Create your models here.
class Categories (models.Model):
    name=models.CharField( max_length=150, unique=True,verbose_name="Названее")
    slug=models.SlugField(max_length=200,blank=True,unique=True,verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"
        verbose_name="Категорию"
        verbose_name_plural="Категории"
    

class SubCategories (models.Model):
    name=models.CharField( max_length=150, unique=False,verbose_name="Названее")
    slug=models.SlugField(max_length=200,blank=True,unique=True,verbose_name="URL")
    category=models.ForeignKey(to=Categories, verbose_name=("Категория"), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "subcategory"
        verbose_name="Податегория"
        verbose_name_plural="Подкатегории"

class Products(models.Model):
    name=models.CharField( max_length=150, unique=True
                          ,verbose_name="Названее")
    slug=models.SlugField(max_length=200,blank=True,unique=True,verbose_name="URL")
    discription=models.TextField(blank=True,null=True, verbose_name="Описание")
    image=models.ImageField(upload_to="goods",blank=True,null=True, verbose_name="Изображение")
    price=models.DecimalField(default=0.00, max_digits=7, decimal_places=2,verbose_name="Цена")
    quantity=models.PositiveIntegerField(default=0,verbose_name="Количество")
    subcategory=models.ForeignKey(to=SubCategories, verbose_name=("Категория"), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Product"
        verbose_name="Товар"
        verbose_name_plural="Товары"
        ordering=("id",)