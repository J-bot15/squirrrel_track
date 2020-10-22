import csv
from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import datetime


class Command(BaseCommand):
    help='import data from the 2018 census file'

    def add_arguments(self,parser):
        parser.add_argument('squirrel_file',help='file containing squirrel details')

    def handle(self,*args,**options):
        file_=options['squirrel_file']

        with open(file_,encoding='utf-8') as fp:
            reader=csv.DictReader(fp)

            for item in reader:
                obj=Squirrel()
                obj.X=item['X']
                obj.Y=item['Y']
                obj.unique_id=item['Unique Squirrel ID']
                obj.shift=item['Shift']
                obj.date=datetime.date(int(item['Date'][-4:]),int(item['Date'][:2]),int(item['Date'][2:4]))
                obj.age=item['Age']
                obj.save()
        msg = f'You are importing from {file_}'
        self.stdout.write(self.style.SUCCESS(msg))
