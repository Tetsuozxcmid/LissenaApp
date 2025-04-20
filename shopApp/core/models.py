from django.db import models

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('dresses', 'Платья'),
        ('skirts', 'Юбки'),
        ('shirts', 'Рубашки'),
        ('blooses','Блузки'),
        ('pants', 'Брюки'),
        ('jackets', 'Куртки'),
        ('complects','Комплекты'),
        ('upper','Верхняя одежда'),
        ('toonics','Туники')
    ]
    
    category = models.CharField(
        "Категория",
        max_length=20,
        choices=CATEGORY_CHOICES,
        
    )

    name = models.CharField("Название",max_length=100)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    priceafterdiscount = models.DecimalField(
        "Цена со скидкой", max_digits=10, decimal_places=2, null=True, blank=True
    )
    size = models.CharField("Размер", max_length=20, blank=True)
    image = models.ImageField("Изображение", upload_to="products/")
    image2 = models.ImageField("Изображение", upload_to="products/", null=True, blank=True)
    image3 = models.ImageField("Изображение", upload_to="products/", null=True, blank=True)
    image4 = models.ImageField("Изображение", upload_to="products/", null=True, blank=True)
    image5 = models.ImageField("Изображение", upload_to="products/", null=True, blank=True)
    image6 = models.ImageField("Изображение", upload_to="products/", null=True, blank=True)
    description = models.TextField("Описание", blank=True)
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class MainPhoto(models.Model):
    name = models.CharField("Название", max_length=20, blank=True)
    image = models.ImageField("Изображения",upload_to="pagephotos/")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Фотка сайта"
