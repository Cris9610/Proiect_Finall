from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Stocks(models.Model):
    produs = models.CharField(max_length=100) #pungi sau folie
    tip_produs = models.CharField(max_length=100) #macroperforat, microperforat sau neperforat

    def __str__(self):
        return f"{self.produs} - {self.tip_produs}"


class Pungi(models.Model):
    stand_up = 'Stand-Up'
    allsideseal = '3 Side Seal'
    de_cafea = 'Pentru Cafea'
    fructe_legume = 'Pentru Fructe / Legume'
    tip_punga_choice = [( stand_up, 'Stand-Up'),
                        (allsideseal, '3 Side Seal'),
                        (de_cafea, 'Pentru Cafea'),
                        (fructe_legume,'Pentru fructe/legume')
                        ]

    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    tip_punga = models.CharField(max_length=22, choices=tip_punga_choice, default=stand_up, verbose_name='Tipul Pungii')
    inaltime_punga = models.PositiveBigIntegerField(verbose_name='Inaltime Punga(mm)')
    latime_punga = models.PositiveBigIntegerField(verbose_name='Latime Punga(mm)')
    inaltime_pliu = models.PositiveBigIntegerField(verbose_name='Inaltime Pliu(mm)')
    grosime_folie_p =models.PositiveBigIntegerField(verbose_name='Grosime Folie(um)')
    zipper = models.BooleanField()
    eurohole = models.BooleanField()
    ciupitura = models.BooleanField()
    cantitate = models.PositiveBigIntegerField(null=True, verbose_name="Nr. Bucati(min. 10.000 buc)")
    active = models.BooleanField(default=1)
    # creat = models.DateTimeField()


    def __str__(self):
        return f"{self.tip_punga} - " \
               f"{self.inaltime_punga} - " \
               f"{self.latime_punga} - " \
               f"{self.inaltime_pliu} - " \
               f"{self.grosime_folie_p}"\
               f"{self.zipper} - " \
               f"{self.eurohole} - " \
               f"{self.ciupitura}"\
               f"{self.cantitate}"


class Folie(models.Model):
    microperforata = 'MICRO'
    macroperforata = 'MACRO'
    neperforata = 'SIMPLU'
    tip_punga_choice = [(microperforata, 'Microperforata'),
                        (macroperforata, 'Macroperforata'),
                        (neperforata, 'Neperforata')
                        ]

    id= models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    tip_folie= models.CharField(max_length=6, choices=tip_punga_choice, default=neperforata, verbose_name='Tipul foliei')
    grosime_folie = models.PositiveBigIntegerField(verbose_name='Grosime Folie(um)')
    latime_folie = models.PositiveBigIntegerField(verbose_name='Latime Folie(mm)')
    cantitate = models.PositiveBigIntegerField(null=True, verbose_name='Nr. kilograme')
    active = models.BooleanField(default=1)
    # creat = models.DateTimeField()

    def __str__(self):
        return f"{self.tip_folie} - {self.grosime_folie} - {self.latime_folie} - {self.cantitate}"