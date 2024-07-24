from django.db import models

class Base(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Type(Base):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(Base):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name
    

class PaymentMethod(Base):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name