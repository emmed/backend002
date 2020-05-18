from django.db import models
from django.contrib.auth.models import User
from cities_light.models import City


class Category(models.Model):
    name = models.CharField(max_length = 200, null = True,)
    def __str__(self):
       return self.name

class Faq(models.Model):
    question = models.TextField(max_length=200, null=True)
    answer = models.TextField(max_length=800, null=True)
    def __str__(self):
       return self.question

class Subject(models.Model):
    SUBJECT_CHOICES=[('Mathematics','Mathematics'),('Algoritmes','Algoritmes'),('Analyses','Analyses'),('Informatica','Informatica'),]
    subject=models.CharField(max_length=200,null=True,choices=SUBJECT_CHOICES)
    def __str__(self):
        return self.subject

class Major(models.Model):
    MAJOR_CHOICES = (
        ('IT','IT'),
        ('Marketing','Marketing'),
        ('DIFF','DIFF'),
    )
    major = models.CharField(max_length=200,choices=MAJOR_CHOICES, null=True)
    def __str__(self):
        return self.major

class Condition(models.Model):
    CONDITION_CHOICES = [
        ('New','New'),
        ('Used','Used'),
    ]
    condition = models.CharField(max_length=200,choices=CONDITION_CHOICES, null=True)
    def __str__(self):
        return self.condition


class Product(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    major = models.ForeignKey(Major, null=True, on_delete=models.SET_NULL)
    condition = models.ForeignKey(Condition, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=800, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    image = models.ImageField(upload_to='post_image', blank=True, width_field=None, height_field=None, max_length=250, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    class Meta:
        unique_together = (('user','title'),)
        index_together = (('user','title'),) 
    
    
    SCHOOL_CHOICES = (
        ('Erasmushogeschool | EHB',(
            ('Campus Kaai', 'Campus Kaai'),
            ('Campus Bloemberg', 'Campus Bloemberg'),
        )),
        ('Vrije Universiteit Brussel | VUB',(
            ('Campus Jette', 'Campus Jette'),
            ('Campus Schaarbeek', 'Campus Schaarbeek'),
        )),
        ('Katholieke universiteit leuven | KUL',(
            ('KUL Gent', 'KUL Gent'),
            ('Campus Antwerpen', 'Campus Antwerpen'),
        )),
    )
    school = models.CharField(max_length=50, choices=SCHOOL_CHOICES, null=True)

    def __str__(self):
        return self.title

  
class ProductOrder(models.Model):

    STATE_CHOICES = [('Ordered', 'Ordered'), ('Pending', 'Pending'),
        ('Placed', 'Placed')
    ]
    buyer = models.ForeignKey(User,related_name="+", null=True,blank=True, on_delete=models.SET_NULL)
    seller = models.ForeignKey(User,related_name="+", null=True,blank=True, on_delete=models.SET_NULL)
   # product moet hier de FK zijn, anders zal de POST an ad functie fout geven
    product = models.ForeignKey(Product, null=True,blank=True, on_delete=models.SET_NULL)
    state = models.CharField(max_length = 200, null = True,
    choices = STATE_CHOICES)

    def __str__(self):
       return self.state

