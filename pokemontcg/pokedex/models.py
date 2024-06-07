from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField()

class Pokemon(models.Model):
    card_id = models.CharField()
    name = models.CharField()
    types = models.ManyToManyField(Type)
    rarity = models.CharField()
    image = models.CharField()
    prices = models.JSONField(default=list)
    highest_market_price = models.FloatField()

    class Meta:
        ordering = ['name']
        
    def __str__(self):
    		return self.name

class Trainer(models.Model):
    card_id = models.CharField(default=None)
    name = models.CharField()
    rarity = models.CharField()
    image = models.CharField()
    prices = models.JSONField(default=list)
    highest_market_price = models.FloatField()
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
    		return self.name

class Energy(models.Model):
    card_id = models.CharField(default=None)
    name = models.CharField()
    image = models.CharField()
    prices = models.JSONField(default=list)
    highest_market_price = models.FloatField()
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
    		return self.name

class PokemonNames(models.Model):
    name = models.CharField(max_length=100)
<<<<<<< HEAD
    
=======
    
class TrainerNames(models.Model):
    name = models.CharField(max_length=100)

class EnergyNames(models.Model):
    name = models.CharField(max_length=100)
>>>>>>> 79bbdd3e21f437b0a71f3a21fb9d969356286901
