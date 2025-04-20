from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product,MainPhoto
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO
from PIL import Image
# Create your tests here.

def generate_image():
    image_io = BytesIO()
    image = Image.new('RGB', (100, 100), 'white')
    image.save(image_io, format='JPEG')
    image_io.seek(0)
    return SimpleUploadedFile("test.jpg", image_io.read(), content_type="image/jpeg")

class AdminTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin = User.objects.create_superuser(username='admin',password='123',email='example@mail.ru')
        self.client.login(username='admin',password='123')

    def test_create_product(self):
        url = reverse('admin:core_product_add')
        image = generate_image()

        data ={
            'category': 'dresses',
            'name': 'Тестовое платье',
            'price': '1999.99',
            'priceafterdiscount': '1499.99',
            'size': 'M',
            'description': 'Очень красивое платье',
            'image': image,
            '_save': 'Сохранить',
        }

        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Product.objects.filter(name='Тестовое платье').exists())

        def test_edit_product(self):
            product = Product.objects.create(
            category='dresses',
            name='Старое платье',
            price='1999.99',
            priceafterdiscount='1499.99',
            size='M',
            description='Описание',
            image=generate_image()
                                            )

            url = reverse('admin:core_product_change', args=[product.pk])
            new_image = generate_image()

            data = {
        'category': 'dresses',
        'name': 'Тестовое платье эдит годжо',
        'price': '1999.99',
        'priceafterdiscount': '1499.99',
        'size': 'M',
        'description': 'Не Очень красивое платье',
        '_save': 'Сохранить',
            }

            response = self.client.post(url, data=data, files={'image': new_image}, follow=True)

            self.assertEqual(response.status_code, 200)
            self.assertTrue(Product.objects.filter(name='Тестовое платье эдит годжо').exists())



            
    
