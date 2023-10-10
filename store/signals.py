from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# receiver for ssending mail to user after registration, but avoid update on user when user is updated

@receiver(post_save, sender=User)
def mail(sender, instance, created, **kwargs):
    if created:
        instance.email_user(f"{instance.username.capitalize()}, welcome to Anystore", """Thank you for signing up for Anystore. Enjoy! \r https://www.anystoreweb.com \r You can also download it from Play Store and App Store.""")
                            
                            
                            
