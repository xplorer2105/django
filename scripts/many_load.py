import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, States, Region, Iso

def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)
    next(reader) # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:

        c, created = Category.objects.get_or_create(name = row[7])
        s, created = States.objects.get_or_create(name = row[8])
        r, created = Region.objects.get_or_create(name = row[9])
        i, created = Iso.objects.get_or_create(name = row[10])

        try:
            y = int(row[3])
        except:
            y = None

        try:
            lon = float(row[4])
        except:
            lon = None

        try:
            lat = float(row[5])
        except:
            lat = None

        try:
            a = float(row[6])
        except:
            a = None

        st, created = Site.objects.get_or_create(
        name = row[0],
        description = row[1],
        justification = row[2],
        year = y,
        longitude = lon,
        latitude = lat,
        area_hectares = a,
        category = c,
        states = s,
        region = r,
        iso = i
        )
