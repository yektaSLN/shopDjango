from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Create default admin user'

    def handle(self, *args, **kwargs):
        username = "admin"
        email = "admin@example.com"
        password = "admin12345"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Default admin created: {username}"))
        else:
            self.stdout.write(self.style.WARNING("Admin already exists"))
