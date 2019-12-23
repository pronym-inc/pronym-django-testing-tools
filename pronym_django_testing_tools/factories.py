import factory

from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user{0}".format(n))
    email = factory.Sequence(lambda n: "user{0}@test.com".format(n))
    first_name = "Test"
    last_name = factory.Sequence(lambda n: "User{0}".format(n))
