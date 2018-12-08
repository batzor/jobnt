from django.core.management.base import BaseCommand

from catalog import models
from django.contrib.auth.models import User
import factory

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name') 
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda o: '%s@kaist.ac.kr' % o.username)
    password = factory.Faker('pystr', min_chars=10, max_chars=20)

class CompanyFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = models.Company
    
    name = factory.Faker('name')
    description = factory.Faker('catch_phrase')
    emp_number = factory.Faker('random_int', min = 1, max = 1000)

class JobFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.JobOffer
    
    name = factory.Faker('job')
    location = factory.Faker('address')
    deadline = factory.Faker('date_between', start_date="-2y", end_date="+1y")
    salary = factory.Faker('random_int', min = 1000000, max = 10000000)
    duration = factory.Faker('random_int', min = 2, max = 12)
    description = factory.Faker('catch_phrase')
    date_posted = factory.Faker('date_between', start_date="-3y", end_date="today")
    recruiter = factory.Iterator(User.objects.all()) 

class FavoriteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Favorite

    user = factory.Iterator(User.objects.all())
    job = factory.Iterator(models.JobOffer.objects.all())

class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Tag
    name = factory.Faker('name')

class JobTagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.JobTag
    job = factory.Iterator(models.JobOffer.objects.all())
    tag = factory.Iterator(models.Tag.objects.all())

class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--company',
            default=20,
            type=int,
            help='The number of fake companies to create.')
        parser.add_argument('--user',
            default = 50,
            type=int,
            help='The number of fake users to create.')
        parser.add_argument('--job',
            default=100,
            type=int,
            help='The number of fake job offers to create.')
        parser.add_argument('--favorite',
            default=100,
            type=int,
            help='The number of fake favorites to create.')
        parser.add_argument('--tag',
            default=50,
            type=int,
            help='The number of fake tags to create.')
        parser.add_argument('--jobtag',
            default=100,
            type=int,
            help='The number of fake jog tags to create.')

    def handle(self, *args, **options):
        for _ in range(options['user']):
            UserFactory.create()
        for _ in range(options['company']):
            CompanyFactory.create()
        for _ in range(options['job']):
            JobFactory.create()
        for _ in range(options['favorite']):
            FavoriteFactory.create()
        for _ in range(options['tag']):
            TagFactory.create()
        for _ in range(options['jobtag']):
            JobTagFactory.create()

