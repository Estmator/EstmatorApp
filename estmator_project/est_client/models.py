from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


STATES = (
    ('Alabama', 'AL'), ('Alaska', 'AK'), ('Arizona', 'AZ'), ('Arkansas', 'AR'),
    ('California', 'CA'), ('Colorado', 'CO'), ('Connecticut', 'CT'),
    ('Delaware', 'DE'), ('Florida', 'FL'), ('Georgia', 'GA'), ('Hawaii', 'HI'),
    ('Idaho', 'ID'), ('Illinois', 'IL'), ('Indiana', 'IN'), ('Iowa', 'IA'),
    ('Kansas', 'KS'), ('Kentucky', 'KY'), ('Louisiana', 'LA'), ('Maine', 'ME'),
    ('Maryland', 'MD'), ('Massachusetts', 'MA'), ('Michigan', 'MI'),
    ('Minnesota', 'MN'), ('Mississippi', 'MS'), ('Missouri', 'MO'),
    ('Montana', 'MT'), ('Nebraska', 'NE'), ('Nevada', 'NV'),
    ('New Hampshire', 'NH'), ('New Jersey', 'NJ'), ('New Mexico', 'NM'),
    ('New York', 'NY'), ('North Carolina', 'NC'), ('North Dakota', 'ND'),
    ('Ohio', 'OH'), ('Oklahoma', 'OK'), ('Oregon', 'OR'),
    ('Pennsylvania', 'PA'), ('Rhode Island', 'RI'), ('South Carolina', 'SC'),
    ('South Dakota', 'SD'), ('Tennessee', 'TN'), ('Texas', 'TX'),
    ('Utah', 'UT'), ('Vermont', 'VT'), ('Virginia', 'VA'),
    ('Washington', 'WA'), ('West Virginia', 'WV'), ('Wisconsin', 'WI'),
    ('Wyoming', 'WY'),
)


@python_2_unicode_compatible
class Company(models.Model):
    company_name = models.CharField(max_length=256)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=256)
    address2 = models.CharField(max_length=256,
                                blank=True)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=20,
                             choices=STATES,
                             default='Washington')
    postal = models.IntegerField()
    ot_rate = models.IntegerField(default=30)
    st_rate = models.IntegerField(default=40)

    def __str__(self):
        return self.company_name


@python_2_unicode_compatible
class Client(models.Model):
    company = models.ForeignKey(Company)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    cell = models.CharField(max_length=20)
    desk = models.CharField(max_length=20,
                            blank=True)
    email = models.EmailField()

    review_intro = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name
