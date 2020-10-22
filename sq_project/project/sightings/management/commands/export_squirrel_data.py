import csv
from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import datetime

class Command(BaseCommand): 
    help='export data to a csv file' 
    
    def add_arguments(self, parser): 
        parser.add_argument('new_file',help='/path/to/file.csv') 
        
    
    def handle(self,*args,**options): 
        
        with open('new_file','w') as f: 
            iwriter = csv.writer(f,delimiter=' ', quotechar='|') 
            fields = Squirrel._meta.fields 
            for item in Squirrel.objects.all(): 
                iwriter.writerow(getattr(item, part.name)for part in fields)
