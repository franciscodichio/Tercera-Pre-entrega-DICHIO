from django.db import models

# Create your models here.



# Create your models here.


# class Animal(models.Model):
#     nombre = models.CharField(max_length=20)
#     edad = models.IntegerField()
    
    
# class persona(models.Model):
#     nombre = models.CharField(max_length=20)
#     apellido = models.CharField(max_length=20)
#     fecha_nacimiento = models.DateField()
    
# class auto(models.Model):
#     marca = models.CharField(max_length=15)
#     velocidad = models.IntegerField()
#     fecha_creacion = models.DateField()


# class Contact(models.Model):
#     # Definición de campos del modelo

#     class Meta:
#         app_label = 'contact'

options = [
    [0, 'Pedido de informacion'],
    [1, 'Queja por un producto'],
    [2, 'Felicitaciones']
]


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre y Apellido')
    email = models.EmailField(verbose_name='Correo Electronico')
    message = models.TextField(verbose_name='Mensaje')
    contact_type = models.IntegerField(choices=options, verbose_name='Tipo de contacto')
    subscription = models.BooleanField(default=False, verbose_name='Subscribirme a correos informativos')
    crated_add = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envio')
    
    class Meta:
        app_label = 'contact'
       

# options = [
#     [0, 'Pedido de informacion'],
#     [1, 'Queja por un producto'],
#     [2, 'Felicitaciones']
# ]

# class Contact(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Nombre y Apellido')
#     email = models.EmailField(verbose_name='Correo Electronico')
#     message = models.TextField(verbose_name='Mensaje')
#     contact_type = models.IntegerField(choices=options, verbose_name='Tipo de contacto')
#     subscription = models.BooleanField(default=False, verbose_name='Subscribirme a correos informativos')
#     crated_add = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envio')
    