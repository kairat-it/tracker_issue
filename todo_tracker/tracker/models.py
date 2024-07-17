from django.db import models

class Status(models.Model):
    objects = None
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Type(models.Model):
    objects = None
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Issue(models.Model):
    summary = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.summary
