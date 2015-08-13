from django.contrib.auth.models import User
from est_quote.models import (Category, Product, Quote, QuoteModifiers)
from est_client.models import Company, Client
from faker import Faker
import factory

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    """Create a fake user."""
    class Meta:
        model = User

    username = fake.user_name()
    password = fake.password()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    company_name = fake.company()
    phone = fake.phone_number()
    address = fake.street_address()
    address2 = fake.building_number()
    city = fake.city()
    state = fake.state()
    postal = fake.zipcode()


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    company = factory.SubFactory(CompanyFactory)
    first_name = fake.first_name()
    last_name = fake.last_name()
    title = fake.job()
    cell = fake.phone_number()
    desk = fake.phone_number()
    email = fake.email()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = fake.word()


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    category = factory.SubFactory(CategoryFactory)
    name = fake.word()
    mins_piece = fake.pyfloat()
    mult_dollies = fake.pyfloat()
    m_cart = fake.pyfloat()
    l_cart = fake.pyfloat()
    p_cart = fake.pyfloat()
    s_pack = fake.pyfloat()


class QuoteModsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = QuoteModifiers

    street_load = fake.pyfloat()
    midrise_elev_std = fake.pyfloat()
    midrise_elv_frt = fake.pyfloat()
    highrise = fake.pyfloat()
    stairs = fake.pyfloat()
    lng_psh = fake.pyfloat()


class QuoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Quote

    user = factory.SubFactory(UserFactory)
    client = factory.SubFactory(ClientFactory)
    name = fake.words()
    date = fake.date()
    sub_total = fake.random_number()
    travel_time = fake.random_number()
    org_street_load = fake.boolean()
    org_midrise_elev_std = fake.boolean()
    org_midrise_elv_frt = fake.boolean()
    org_highrise = fake.boolean()
    org_stairs = fake.boolean()
    org_lng_psh = fake.boolean()
    dest_street_load = fake.boolean()
    dest_midrise_elev_std = fake.boolean()
    dest_midrise_elv_frt = fake.boolean()
    dest_highrise = fake.boolean()
    dest_stairs = fake.boolean()
    dest_lng_psh = fake.boolean()
    grand_total = fake.random_number()
