from django.contrib.auth.models import User
from est_quote.models import (
    Company, Client, Category, Product, Quote, QuoteModifiers)

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


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    company = fake.company()
    first_name = fake.first_name()
    last_name = fake.last_name()
    title = fake.job()
    cell = fake.phone_number()
    desk = fake.phone_number()
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


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = fake.word()


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    category = fake.word()
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

    user = fake.username
    client = fake.name()
    name = fake.words()
    date = fake.date()
    sub_total = fake.random_number()
    products = None
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
