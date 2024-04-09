from django.db import models

class Tuman(models.Model):
    Nomi = models.CharField(max_length=300)
    Masul = models.CharField(max_length=300)
    def __str__(self):
        return self.Nomi

class Maktab(models.Model):
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)
    Nomi = models.CharField(max_length=300)
    Masul = models.CharField(max_length=300)
    def __str__(self):
        return self.Nomi
    
class Shaxs(models.Model):
    maktab = models.ForeignKey(Maktab, on_delete=models.CASCADE)
    Ismi = models.CharField(max_length=300)
    Familyasi = models.CharField(max_length=300)
    statuses = {
        ('tugallangan', 'tugallangan'),
        ('tugallanmagan', 'tugallanmagan')
    }
    horida = models.CharField(max_length=15, verbose_name='Status', choices=statuses)

