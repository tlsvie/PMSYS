from django.db import models


class Mood(models.Model):
    status = models.CharField(max_length=10,null=False)

    def __str__(self):
        return self.status


class Post(models.Model):
    mood = models.ForeignKey('mood',on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10,default="不愿透漏身份的人")
    message = models.TextField(null= False)
    def_pass = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now=True)
    enable = models.BooleanField(default=False)

    def __str__(self):
        return self.message


class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('M', 'Large'),
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)

    def __str__(self):
        return self.name


class Maker(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class PModel(models.Model):
    maker = models.ForeignKey(Maker,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField(default="http://www.baidu.com")

    def __str__(self):
        return self.name


class Product1(models.Model):
    pmodel = models.ForeignKey(PModel,on_delete=models.CASCADE, verbose_name="型号")
    nickname = models.CharField(max_length=15,default="二手机",verbose_name="摘要")
    description = models.TextField(default="暂无说明")
    year = models.PositiveIntegerField(default=2018, verbose_name="出厂年份")
    price = models.PositiveIntegerField(default=0, verbose_name="价格")

    def __str__(self):
        return self.nickname


class PPhoto(models.Model):
    product = models.ForeignKey(Product1,on_delete=models.CASCADE)
    description = models.CharField(max_length=20,default="产品图片")
    url = models.URLField(default="http://www.baidu.com")

    def __str__(self):
        return self.description
