from django.db import models

# Create your models here.
#ENUM
VOID_CHOICES = (
    ("0", "0"),
    ("1", "1")
)


class movie(models.Model):
    UID = models.UUIDField  # Computer fields

    # Business fields
    movie_id = models.CharField(max_length=20)
    movie_name = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    genre = models.CharField(max_length=15)

    class Meta:
        ordering = ['movie_id']

    def __str__(self):
        return self.movie_id + '  ' + self.movie_name


class Attend(models.Model):
    UID = models.UUIDField #Computer fields

    # Business fields
    attn_number = models.CharField(max_length=20)
    movie_name = models.CharField(max_length=200)
    seat_number = models.CharField(max_length=4)
    show_time = models.CharField(max_length=15)
    attend_info = models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)




    class Meta:
        ordering = ['attn_number']

    def __str__(self):
        return self.attn_number + '  Seat' + self.seat_number

