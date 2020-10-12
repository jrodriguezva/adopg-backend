from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from model_utils.models import TimeStampedModel


class Address(models.Model):
    address1 = models.CharField('primera dirección', max_length=100)
    address2 = models.CharField('segunda dirección', max_length=100)
    city = models.CharField('ciudad', max_length=100)
    country = models.CharField('país', max_length=50)
    postcode = models.CharField('código postal', max_length=50)
    state = models.CharField('estado', max_length=50)
    latitude = models.DecimalField('latitud', max_digits=11, decimal_places=8)
    longitude = models.DecimalField('longitud', max_digits=11, decimal_places=8)

    class Meta:
        verbose_name = "dirección"
        verbose_name_plural = "direcciones"


class SocialMedia(models.Model):
    facebook = models.CharField('facebook', max_length=50)
    instagram = models.CharField('instagram', max_length=50)
    pinterest = models.CharField('pinterest', max_length=50)
    twitter = models.CharField('twitter', max_length=50)
    youtube = models.CharField('youtube', max_length=50)

    class Meta:
        verbose_name = "redes sociales"
        verbose_name_plural = "redes sociales"


class Hour(models.Model):
    monday = models.CharField('lunes', max_length=50)
    tuesday = models.CharField('martes', max_length=50)
    wednesday = models.CharField('miércoles', max_length=50)
    thursday = models.CharField('jueves', max_length=50)
    friday = models.CharField('viernes', max_length=50)
    saturday = models.CharField('sábado', max_length=50)
    sunday = models.CharField('domingo', max_length=50)

    class Meta:
        verbose_name = "horario"
        verbose_name_plural = "horarios"


class Organization(TimeStampedModel):
    name = models.CharField('nombre', max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField("teléfono")
    url = models.CharField('url', max_length=50)
    website = models.CharField('sitio web', max_length=50)
    hours = models.OneToOneField(Hour, on_delete=models.CASCADE, verbose_name="horario")
    address = models.OneToOneField(Address, on_delete=models.CASCADE, verbose_name="dirección")
    socialMedia = models.OneToOneField(SocialMedia, on_delete=models.CASCADE, verbose_name="redes sociales")
    image = models.ImageField('imagen', upload_to="organization")

    class Meta:
        verbose_name = "organización"
        verbose_name_plural = "organizaciones"
