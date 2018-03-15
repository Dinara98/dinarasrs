from django.db import models

# Create your models here.

class Eating(models.Model):
    """
    Model representing a menu eating (e.g. Food time, lunch.).
    """
    name = models.CharField(max_length=200, help_text="Enter a menu eating (e.g. Food time, lunch.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Menu(models.Model):
    """
    Model representing a menu (but not a specific copy of a menu).
    """
    name = models.CharField(max_length=200)
    guest = models.ForeignKey('Guest', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because menu can only have one guest, but guest can have multiple menus
    # Guest as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the resept')
    price = models.CharField(' ',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn"> number</a>')
    eating = models.ManyToManyField(Eating, help_text='Select a eating food')
    # ManyToManyField used because eating can contain many menus. Menus can cover many eatings.
    # Eating class has already been defined so we can specify the object above.
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this menu.
        """
        return reverse('menu-detail', args=[str(self.price)])
 
class Guest(models.Model):
 """
 Model representing an guest.
"""
 first_name = models.CharField(max_length=100)
 last_name = models.CharField(max_length=100)
 time_of_order = models.DateField(null=True, blank=True)

class Meta:
        ordering = ["last_name","first_name"]
    
        def get_absolute_url(self):
          """
         Returns the url to access a particular guest instance.
        """
          return reverse('guest-detail', args=[str(self.id)])
    
        def __str__(self):
          """
        String for representing the Model object.
        """
          return '{0}, {1}'.format(self.last_name,self.first_name)