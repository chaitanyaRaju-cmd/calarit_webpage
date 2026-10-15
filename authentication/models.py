from django.db import models


class OTPVerification(models.Model):

    username = models.CharField(
        max_length=150,
        default=""
    )

    email = models.EmailField()

    password = models.CharField(
        max_length=255,
        default=""
    )

    otp = models.CharField(
        max_length=6
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_verified = models.BooleanField(
        default=False
    )

    def __str__(self):

        return self.email