from django.contrib.auth.models import User

import factory
from faker import Faker

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    """Create a fake user."""
    class Meta:
        model = User

    username = fake.user_name()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
