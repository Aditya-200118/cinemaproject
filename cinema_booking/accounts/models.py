from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Create a default address for the superuser
        default_address = Address.objects.create(
            billing_address='Default Address',
            city='Default City',
            state='Default State',
            zip_code='00000'
        )
        extra_fields['address'] = default_address

        return self.create_user(email, password, **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email=email)


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True, null=False, unique=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=15, default="N/A")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["first_name", "last_name"]
    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        abstract = True


class Customer(User):
    address = models.OneToOneField(
        "Address", on_delete=models.CASCADE, related_name="customer"
    )
    reset_token = models.CharField(max_length=100, blank=True, null=True)
    promotions = models.BooleanField(default=False)
    # def clean(self):
    #     if self.address and self.address.customer != self:
    #         raise ValidationError('A customer can only have one address.')


class Address(models.Model):
    billing_address = models.CharField(max_length=255, default="N/A")
    city = models.CharField(max_length=100, default="N/A")
    state = models.CharField(max_length=100, default="N/A")
    zip_code = models.CharField(max_length=10, default="N/A")

    def clean(self):
        if self.pk and hasattr(self, 'customer'):
            if self.customer and self.customer.pk != self.pk:
                raise ValidationError("A customer can only have one address.")


class Card(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="cards"
    )
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=4)

    # def clean(self):
    #     if self.customer.cards.count() >= 4:
    #         raise ValidationError('A customer can only have up to four payment methods.')