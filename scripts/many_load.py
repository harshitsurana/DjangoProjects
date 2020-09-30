import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript unesco_load

from unesco.models import Category, States, Region, Iso, Site

def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)
    next(reader) # Advance past the header

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:
        print(row)

        r, created= Region.objects.get_or_create(name = row[9])
        s, created= States.objects.get_or_create(name = row[8])
        i, created= Iso.objects.get_or_create(name = row[10])
        c, created= Category.objects.get_or_create(name = row[7])

        try:
            y=int(row[3])
        except:
            y=None

        try:
            lon=float(row[4])
        except:
            lon=None

        try:
            lat=float(row[5])
        except:
            lat=None

        try:
            area=float(row[6])
        except:
            area=None


        # state = States(name=row[8])
        # state.save()

        # region = Region(name=row[9])
        # region.save()

        # c= Category(name=row[7],region=r, state=s, iso=i)
        # c.save()

        # iso = Iso(name=row[10])
        # iso.save()

        site = Site(name=row[0], year=y, description=row[1], justification=row[2], longitude=lon, latitude=lat, area_hectares=area,category=c, states=s, region=r, iso=i)
        site.save()


