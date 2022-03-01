from django.db import models

class RisingStock(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    curprice = models.BigIntegerField()
    diff = models.BigIntegerField()
    ratio = models.FloatField()
    volume = models.BigIntegerField()
    per = models.FloatField()
    roe = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass


class NewsOfRisingStock(models.Model):
    code = models.ForeignKey(RisingStock, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    url = models.URLField()
    written_at = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
