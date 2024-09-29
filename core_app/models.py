from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=254, blank=True, null=True)
    excerpt = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id} - {self.title}"
    
class FooterVragenModel(models.Model):
    CATEGORY_CHOICES = [
        ('vraag-1', 'Vraag 1'),
        ('vraag-2', 'Vraag 2'),
        ('vraag-3', 'Vraag 3'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    question = models.TextField(max_length=250, help_text="Vul hier je vraag of opmerking in.")

    def __str__(self):
        return f"Inquiry about {self.category}"