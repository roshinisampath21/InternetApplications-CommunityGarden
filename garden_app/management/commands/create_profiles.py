# garden_app/management/commands/create_profiles.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from garden_app.models import Profile

class Command(BaseCommand):
    help = 'Create profiles for existing users who do not have one'

    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            profile, created = Profile.objects.get_or_create(user=user)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created profile for user: {user.username}'))
            else:
                self.stdout.write(self.style.WARNING(f'Profile already exists for user: {user.username}'))

