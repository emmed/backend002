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
    SUBJECT_CHOICES=[
        ('Wiskunde','Wiskunde'),
        ('Algoritmes','Algoritmes'),
        ('Analyses','Analyses'),
        ('Informatica','Informatica'),
        ('Fysica','Fysica'),
        ('Wijsbegeerte','Wijsbegeerte'),
        ('Geologie','Geologie'),
        ('Psychologie','Psychologie'),
        ('Godsdienst','Godsdienst'),
        ('Frans','Frans'),
        ('Engels','Engels'),
        ('Duits','Duits'),
        ('Biologie','Biologie'),
        ('Toerisme','Toerisme'),
        ('Economie','Economie'),
        ('Toneel','Toneel'),
        ('Audiovisuele vorming','Audiovisuele vorming'),
]
    subject=models.CharField(max_length=200,null=True,choices=SUBJECT_CHOICES)
    def __str__(self):
        return self.subject

class Major(models.Model):
    MAJOR_CHOICES = (
        ('Handelsingenieur','Handelsingenieur'),
        ('Industriële wetenschappen Energie','Industriële wetenschappen Energie'),
        ('Biowetenschappen','Biowetenschappen'),
        ('Architectuur','Architectuur'),
        ('International Business','International Business'),
        ('Fysica','Fysica'),
        ('Wiskunde','Wiskunde'),
        ('Wijsbegeerte','Wijsbegeerte'),
        ('Kunstwetenschappen','Kunstwetenschappen'),
        ('Taal- en letterkunde','Taal- en letterkunde'),
        ('Geologie','Geologie'),
        ('Informatica','Informatica'),
        ('Rechten','Rechten'),
        ('Geschiedenis','Geschiedenis'),
        ('Beeldende kunsten','Beeldende kunsten'),
        ('Visual Arts','Visual Arts'),
        ('Drama','Drama'),
        ('Muziek','Muziek'),
        ('Chemie','Chemie'),
        ('Biomedische laboratoriumtechnologie','Biomedische laboratoriumtechnologie'),
        ('Bedrijfsmanagement','Bedrijfsmanagement'),
        ('Journalistiek','Journalistiek'),
        ('Office management','Office management'),
        ('Transport en logistiek','Transport en logistiek'),
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

class School(models.Model):
    SCHOOL_CHOICES = (
        ('Odisee','Odisee'),
        ('LUCA School of Arts','LUCA School of Arts'),
        ('Erasmushogeschool Brussel','Erasmushogeschool Brussel'),
        ('Artesis Plantijn Hogeschool','Artesis Plantijn Hogeschool'),
        ('Karel de Grote-Hogeschool','Karel de Grote-Hogeschool'),
        ('Thomas More','Thomas More'),
        ('UC Leuven','UC Leuven'),
        ('Hogeschool PXL','Hogeschool PXL'),
        ('UC Limburg','UC Limburg'),
        ('Hogeschool West-Vlaanderen','Hogeschool West-Vlaanderen'),
        ('Katholieke Hogeschool Vives','Katholieke Hogeschool Vives'),
        ('Hogeschool Gent Geraard','Hogeschool Gent	Geraard'),
        ('Arteveldehogeschool','Arteveldehogeschool'),
        ('Vrije Universiteit Brussel','Vrije Universiteit Brussel'),
        ('Universiteit Antwerpen','Universiteit Antwerpen'),
        ('Katholieke Universiteit Leuven','Katholieke Universiteit Leuven'),
        ('Universiteit Hasselt','Universiteit Hasselt'),
        ('Universiteit Gent','Universiteit Gent'),
    )
    school = models.CharField(max_length=200,choices=SCHOOL_CHOICES, null=True)
    def __str__(self):
        return self.school


class Product(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL, blank=True)
    major = models.ForeignKey(Major, null=True, on_delete=models.SET_NULL, blank=True)
    condition = models.ForeignKey(Condition, null=True, on_delete=models.SET_NULL)
    school = models.ForeignKey(School, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=800, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    image = models.ImageField(upload_to='post_image', blank=True, width_field=None, height_field=None, max_length=250, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    class Meta:
        unique_together = (('user','title'),)
        index_together = (('user','title'),) 
    
    
    # SCHOOL_CHOICES = (
    #     ('Erasmushogeschool | EHB',(
    #         ('Campus Kaai', 'Campus Kaai'),
    #         ('Campus Bloemberg', 'Campus Bloemberg'),
    #     )),
    #     ('Vrije Universiteit Brussel | VUB',(
    #         ('Campus Jette', 'Campus Jette'),
    #         ('Campus Schaarbeek', 'Campus Schaarbeek'),
    #     )),
    #     ('Katholieke universiteit leuven | KUL',(
    #         ('KUL Gent', 'KUL Gent'),
    #         ('Campus Antwerpen', 'Campus Antwerpen'),
    #     )),
    # )
    # school = models.CharField(max_length=50, choices=SCHOOL_CHOICES, null=True)

    def __str__(self):
        return self.title

  
class ProductOrder(models.Model):
    buyer = models.ForeignKey(User,related_name="+", null=True,blank=True, on_delete=models.SET_NULL)
    seller = models.ForeignKey(User,related_name="+", null=True,blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True,blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.product)

       