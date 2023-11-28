from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField('Category name', max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'




class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category')
    name = models.CharField('Category name', max_length=60)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'




class Brand(models.Model):

    subcategory = models.ManyToManyField(SubCategory, related_name='brand_subcategory')
    name = models.CharField('Brand name', max_length=30)
    image = models.ImageField('Brand name', upload_to='media/brands/')

    def __str__(self):
        return self.name


class ProductDisplay(models.Model):

    name = models.CharField('ProductDisplay name', max_length=50)

    def __str__(self):
        return self.name


class ProductCPU(models.Model):

    name = models.CharField('ProductCPU name', max_length=50)

    def __str__(self):
        return self.name




class ProductGPU(models.Model):

    name = models.CharField('ProductGPU name', max_length=50)

    def __str__(self):
        return self.name




class ProductRam(models.Model):

    name = models.CharField('ProductRam name', max_length=50)

    def __str__(self):
        return self.name



class ProductMemory(models.Model):

    name = models.CharField('ProductMemory name', max_length=50)

    def __str__(self):
        return self.name




class Product(models.Model):

    brand = models.ManyToManyField(Brand, related_name='product_brand')
    cpu = models.ManyToManyField(ProductCPU, related_name='cpu_code')
    gpu = models.ManyToManyField(ProductGPU, related_name='gpu_code')
    ram = models.ManyToManyField(ProductRam, related_name='ram_code')
    memory = models.ManyToManyField(ProductMemory, related_name='memory_code')
    display = models.ManyToManyField(ProductDisplay, related_name='display_code')

    name = models.CharField('Product name', max_length=60)
    price = models.PositiveIntegerField('Product price')
    desc = models.TextField('product text')
    audio = models.CharField('Audio name', max_length=50)
    input_out = models.CharField('Input/Output', max_length=60)
    camera = models.CharField('Camera', max_length=20)
    usb_count = models.PositiveIntegerField('Usb count')
    keboard_light = models.BooleanField('Keboard light')
    image = models.ImageField('Product image', upload_to='media/products/')


    def __str__(self):
        return self.name