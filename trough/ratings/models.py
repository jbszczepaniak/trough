from django.db import models


class RatingCategory(models.Model):
    name = models.CharField(max_length=255, null=True)
