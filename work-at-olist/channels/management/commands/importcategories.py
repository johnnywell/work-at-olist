from django.core.management.base import BaseCommand, CommandError
from channels.models import Channel, Category
import csv


class Command(BaseCommand):
    help = 'Import all categories from a csv file and does a full update on a channel'

    def add_arguments(self, parser):
        parser.add_argument('channel', type=str)
        parser.add_argument('categories_csv', type=str)

    def handle(self, *args, **options):
        try:
            csvfile = open(options['categories_csv'])
        except:
            raise CommandError("Can't open the csv file")
        try:
            csvreader = csv.reader(csvfile)
        except:
            raise CommandError("The file isn't a valid csv.")
        try:
            channel, created = Channel.objects.get_or_create(
                name=options['channel'], defaults={'name': options['channel']})
            channel.categories.all().delete()
            lines = []
            for row in csvreader:
                categories_in_row = row[0].split(' / ')
                lines.append(categories_in_row)
                # channel.create_categories_from_list(categories_in_row)
            import pdb; pdb.set_trace()
            print("Done!")
        except Exception as e:
            raise CommandError("Sorry Dave I can't do that.\n {}".format(e))
