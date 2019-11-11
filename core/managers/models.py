from django.db import models

optional = {
    'null': True,
    'blank': True,
}


class Position(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return(f"{self.title}")


class Employee(models.Model):
    fullname = models.CharField(max_length=200)
    emp_code = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.fullname}")
