from django.db import models

# Create your models here.
class WordList(models.Model):

    GENDERS = [
        ('der', 'Der'),
        ('die', 'Die'),
        ('das', 'Das'),
 ]

    word = models.CharField(verbose_name= 'Word', max_length=100)
    gender = models.CharField(verbose_name= 'Gender', max_length=3, choices=GENDERS)


    def __str__(self):
        return self.gender + ' ' + self.word


    class Meta:

        verbose_name ='WordList'
        verbose_name_plural = "WordList's"