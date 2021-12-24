from django.db import models


class Competitor(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    linkedIn = models.CharField(max_length=100)
    # competitor_entry = models.ForeignKey(Competitor, on_delete=models.CASCADE)

    Competition = models.Manager()

    # allows references to a specific competitor as the person's name, not the primary key
    # def __str__(self):
    #     return self.name + ' as a test 1'


# class CompetitorList(models.Model):
#     person = models.ForeignKey(Competitor, on_delete=models.CASCADE)
#     print(person)
#     CompetitorSingle = models.Manager()