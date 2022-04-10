from django.db import models

class Logo(models.Model):
    image = models.ImageField(upload_to='Logo/')

class Slider(models.Model):
    image = models.ImageField(upload_to='Slider/')
    title1 = models.CharField(max_length=60)
    title2 = models.CharField(max_length=60)
    text = models.CharField(max_length=220)

class Info(models.Model):
    image1 = models.ImageField(upload_to='Info/')
    image2 = models.ImageField(upload_to='Info/')
    title1 = models.CharField(max_length=60)
    title2 = models.CharField(max_length=60)
    text = models.TextField()

class Video(models.Model):
    title = models.CharField(max_length=30)
    video = models.FileField(upload_to='Video/')


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    products = models.CharField(max_length=300)
    image = models.ImageField(upload_to='Food/')
    title1 = models.CharField(max_length=60)
    title2 = models.CharField(max_length=60)
    stars = models.IntegerField()

    def __str__(self):
        return self.name

class Advertisement(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)


class Client(models.Model):
    name = models.CharField(max_length=200)
    debt = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()

class Reservation(models.Model):
    date = models.DateField()
    time = models.CharField(max_length=20)
    reserv = models.CharField(max_length=100)

class AboutUs(models.Model):
    text = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()

class Cash(models.Model):
    cash = models.IntegerField()