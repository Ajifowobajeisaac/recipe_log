from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model


class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves users with email, password and date of birth
        """
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, date_of_birth, password=None):
       """
        Creates and saves a superuser with email, password and date of birth
        """

       user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth
        )
       
       user.is_admin = True
       user.save(using=self._db)
       return user
    
       


class User(AbstractBaseUser):
    """Defines a custom user model to enable email authentication"""
    email = models.EMAIL_FIELD(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()

    """To be used as the primary identifier"""
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True
    
    def has_module_perms(self, recipe_log):
        "Does the user have permissions to view the app `recipe_log`?"
        return True

    def is_staff(self):
        "Is the user a member of staff"
        return self.is_admin

class Recipe(models.Model):
    """The name of the recipe the user entered"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        """Return the string representation of the model"""
        return self.text
    
class RecipeDetails(models.Model):
    """The conntent of a recipe"""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'recipe_details'

    def __str__(self):
        """Returns the string representaion of the entry"""
        return f"{self.text[:50]}..."

class Ingredients(models.Model):
    """The conntent of a recipe"""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'ingredients'

    def __str__(self):
        """Returns the string representaion of the entry"""
        return f"{self.text[:50]}..."
