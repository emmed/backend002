from django.db import models
from django.contrib.auth.models import User
# class User(models.Model):
#     id_user = models.DecimalField(max_digits=10, decimal_places=2, null=True)
#     def __str__(self):
#        return self.id_user

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

class Location(models.Model):
    LOCATION_CHOICES = [
        ('Brussel','Brussel'),
        ('Leuven','Leuven'),
        ('Gent','Gent'),
        ('Antwerpen','Antwerpen'),
    ]
    location = models.CharField(max_length=200,choices=LOCATION_CHOICES, null=True)
    def __str__(self):
        return self.location

class Product(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
   # state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    major = models.ForeignKey(Major, null=True, on_delete=models.SET_NULL)
    condition = models.ForeignKey(Condition, null=True, on_delete=models.SET_NULL)
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=800, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    #image = models.ImageField(upload_to='post_image', blank=True, width_field=None, height_field=None, max_length=100,)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        unique_together = (('user','title'),)
        index_together = (('user','title'),) 
    
    
    SCHOOL_CHOICES = (
        ('Erasmushogeschool | EHB',(
            ('CampusKaai', 'CampusKaai'),
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
    
    # MAJOR_CHOICES = (
    #     ('IT','IT'),
    #     ('Marketing','Marketing'),
    #     ('DIFF','DIFF'),
    # )
    # major = models.CharField(max_length=200,choices=MAJOR_CHOICES, null=True)
   
    # SUBJECT_CHOICES = [
    #     ('Mathematics','Mathematics'),
    #     ('Algoritmes','Algoritmes'),
    #     ('Analyses','Analyses'),
    # ]
    # subject = models.CharField(max_length=200,choices=SUBJECT_CHOICES, null=True)
    
    # CONDITION_CHOICES = [
    #     ('New','New'),
    #     ('Used','Used'),
    # ]
    # condition = models.CharField(max_length=200,choices=CONDITION_CHOICES, null=True)
    
    # LOCATION_CHOICES = [
    #     ('Brussel','Brussel'),
    #     ('Leuven','Leuven'),
    #     ('Gent','Gent'),
    #     ('Antwerpen','Antwerpen'),
    # ]
    # location = models.CharField(max_length=200,choices=LOCATION_CHOICES, null=True)
    

    def __str__(self):
        return self.title

  
class ProductOrder(models.Model):

    STATE_CHOICES = [('Ordered', 'Ordered'), ('Pending', 'Pending'),
        ('Placed', 'Placed')
    ]
    buyer = models.ForeignKey(User,related_name="+", null=True,blank=True, on_delete=models.SET_NULL)
    seller = models.ForeignKey(User,related_name="+", null=True,blank=True, on_delete=models.SET_NULL)
   # product moet hier de FK zijn anders zal de POST an ad functie fout geven
    product = models.ForeignKey(Product, null=True,blank=True, on_delete=models.SET_NULL)
    state = models.CharField(max_length = 200, null = True,
    choices = STATE_CHOICES)

    def __str__(self):
       return self.state

