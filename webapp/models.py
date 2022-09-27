from django.db import models

CHOICES = (
    ('new', 'новое'),
    ('moderated', 'модерированная'),
)


class Quote(models.Model):
    text = models.TextField(max_length=3000, verbose_name='text')
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name='author')
    email = models.EmailField(max_length=254, blank=False)
    rating = models.IntegerField(default=0)
    status = models.CharField(max_length=50, null=False, blank=False, verbose_name='status', default=CHOICES[0][0],
                              choices=CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

    def __str__(self):
        return f'{self.id}.{self.text}.{self.author}'

    class Meta:
        db_table = 'quotes'
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'
        permissions = [('moderator', 'модератор')]
