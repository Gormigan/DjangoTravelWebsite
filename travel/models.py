from django.db import models

class Continent(models.Model):
    name = models.CharField(max_length=100)

    REQUIRED_FIELDS = ['name', ]

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)
    continent = models.ForeignKey(Continent,null=True,on_delete=models.SET_NULL)
    REQUIRED_FIELDS = ['name', ]

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country,null=True,on_delete=models.SET_NULL)
    REQUIRED_FIELDS = ['name',]

    def __str__(self):
        return self.name


class Airport(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City,null=True,on_delete=models.SET_NULL)
    REQUIRED_FIELDS = ['name',]

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    standard = models.CharField(null=True,max_length=50,choices=(("1","1-star"),("2","2-star"),("3","3-star"),("4","4-star"),("5","5-star")))
    city = models.ForeignKey(City,null=True,on_delete=models.SET_NULL)
    description = models.TextField(null=True)
    REQUIRED_FIELDS = ['name',]

    def __str__(self):
        return self.name


class Travel(models.Model):
    name = models.CharField(max_length=100)
    city_from = models.ForeignKey(City,on_delete=models.CASCADE,related_name="city_from")
    airport_from = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="airport_from")

    city_to = models.ForeignKey(City, on_delete=models.CASCADE,related_name="city_to")
    airport_to = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name="airport_to")

    hotel = models.ForeignKey(Hotel, null=True,on_delete=models.CASCADE,related_name="hotel")

    promoted = models.BooleanField(default=False)
    description = models.TextField(null=True)
    image = models.ImageField(null=True,upload_to="travel/", height_field=None, width_field=None, max_length=100)
    departure_date = models.DateField()
    return_date  = models.DateField()
    number_days =models.IntegerField(null=True)

    price_adult = models.IntegerField(null=True)
    price_child = models.IntegerField(null=True)

    type = models.CharField(choices=(("1","BB"),("2","HB"),("3","FB"),("4","AI")),max_length=50,null=True)

    number_places_adults = models.IntegerField(null=True)
    number_places_children = models.IntegerField(null=True)

    REQUIRED_FIELDS = ['name',"departure_date","return_date","price_adult","price_child","number_places_adults",
                       "number_places_children"]

    def __str__(self):
        return self.name


class Order(models.Model):
    adult_count = models.IntegerField()
    children_count = models.IntegerField()
    travel = models.ForeignKey(Travel,null=True,on_delete=models.CASCADE,)
    price = models.IntegerField()

    first_name = models.CharField(null=True,max_length=100)
    last_name = models.CharField(null=True,max_length=100)

    email = models.EmailField(null=True,max_length=200)
    REQUIRED_FIELDS = ['travel',"email","first_name","last_name","adult_count","children_count","price"]

    def __str__(self):
        return self.travel.name
# Create your models here.
