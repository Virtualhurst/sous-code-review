from django.db import models

class DataRecord(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"DataRecord({self.name})"
