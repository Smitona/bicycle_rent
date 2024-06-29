from django.db import models
import datetime as dt

from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import CustomUser


class Bicycle(models.Model):
    """Модель велосипедов под аренду."""
    number = models.AutoField(primary_key=True)
    hour_cost = models.PositiveSmallIntegerField(
        blank=False,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ],
    )

    class Meta:
        verbose_name = 'Bicycle'
        verbose_name_plural = 'Bicycles'
        ordering = ('number',)

    def __str__(self):
        return 'Bike number {} costs {} per hour'.format(
            self.number, self.hour_cost,
        )


class Rental(models.Model):
    """Модель аренды."""
    bike = models.ForeignKey(Bicycle, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rented_at = models.DateTimeField(default=dt.datetime.now())

    class Meta:
        verbose_name = 'Rental'
        verbose_name_plural = 'Rentals'
        ordering = ('user',)

    def __str__(self):
        return 'Bike number {} rented by {} at {}'.format(
            self.bike, self.user, self.rented_at
        )
