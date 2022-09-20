from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse
import secrets, string
from django.utils.text import slugify
from django_countries.fields import CountryField

# Create your models here.

class ItemSender(models.Model):

    """
    Model for item sender
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin_user")
    fullname =  models.CharField(max_length=150, default='')
    company = models.CharField(max_length=150, null=True, blank=True)
    address =  models.CharField(max_length=300, blank=True, null=True)
    postal_code = models.CharField(max_length=150, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    country = CountryField(
        blank_label="(select a country)",
    )
    date_sent = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-date_sent',)

    def __str__(self):
        return f'{self.fullname}'
    
    def get_absolute_url(self):
        return reverse('user', args=[self.user.username])


class ItemReciever(models.Model):  
    """
    Model for item receiver
    """
    sender = models.ForeignKey(ItemSender, on_delete=models.CASCADE, related_name="sender_to_receiver")
    fullname = models.CharField(max_length=250, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    address =  models.CharField(max_length=300, blank=True, null=True)
    postal_code = models.CharField(max_length=150, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    country = CountryField(
        blank_label="(select a country)",
    )
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return f'{self.fullname} {self.email}'


class ItemDetail (models.Model):   
    '''
        Item details model
    '''
    item_sender = models.ForeignKey(ItemSender, on_delete=models.CASCADE, related_name="item_sender")
    item_receiver = models.ForeignKey(ItemReciever, on_delete=models.CASCADE, related_name="item_receiver")
    item_name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    quantity = models.IntegerField()
    description = models.TextField(max_length= 400, null=True, blank=True)
    weight = models.CharField(max_length=100)
    image = models.ImageField(upload_to='package_photos', default='default.jpg')
    paid = models.BooleanField(default=False)
    shipped = models.BooleanField(default=False)
    item_code = models.CharField(max_length=100)
    date_sent = models.DateTimeField(default=timezone.now)
    date_recieved = models.DateTimeField(default=timezone.now)
    date_shipped = models.DateTimeField(default=timezone.now() + timedelta(1))
    delivery_frame = models.DateTimeField(default=timezone.now() + timedelta(7))

    class Meta:
        ordering = ('-date_sent', '-date_recieved')

    def save(self, *args, **kwargs):
        while not self.item_code:
            item_code = ''.join(secrets.choice(string.digits) for i in range(12))
            items_with_similar_code = ItemDetail.objects.filter(item_code=item_code)
            if not items_with_similar_code:
                self.item_code = item_code
        self.slug = slugify(self.item_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.item_name}'


class Status(models.Model):
    STATUS= (
        ('transit', 'ON TRANSIT'),
        ('withheld', 'WITHHELD'), 
        ('sent', 'SENT'),
        ('delivered', 'DELIVERED'),       
    )

    PROBLEM = (
        ('no problem', 'No Problems'),
        ('paperwork', 'PAPERWORK_OVERLOAD'),
        ('custom clerance', 'CUSTOM CLEARANCE'),
        ('bad weather', 'BAD WEATHER'),
    )
    item = models.OneToOneField(ItemDetail, on_delete=models.CASCADE, related_name="item_status")
    status = models.CharField(choices=STATUS, default='transit', max_length=100)
    problem_type = models.CharField(choices=PROBLEM, default='no problem', max_length=100)
    country = CountryField(
        blank_label="(select a country)",
    )