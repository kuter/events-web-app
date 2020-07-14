from django.contrib.auth import get_user_model

import factory


class UserFactory(factory.DjangoModelFactory):
    """User factory."""

    username = factory.Faker('user_name')
    email = factory.Faker('email')

    class Meta:
        model = get_user_model()
