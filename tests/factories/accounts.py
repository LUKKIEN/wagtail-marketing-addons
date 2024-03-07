import factory
from django.contrib.auth import get_user_model


class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.LazyAttributeSequence(lambda user, n: f'{user.first_name}{user.last_name}_{n}')
    email = factory.LazyAttributeSequence(lambda user, n: f'{user.username}{n}@example.com')
    password = 'supersecret'

    is_active = True
    is_staff = False
    is_superuser = False

    class Meta:
        model = get_user_model()

    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        password = kwargs.pop('password')
        user = super()._create(target_class, *args, **kwargs)

        if password:
            user.clear_password = password
            user.set_password(password)
            user.save()

        return user
