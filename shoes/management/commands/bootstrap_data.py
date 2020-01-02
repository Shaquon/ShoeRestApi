from django.core.management.base import BaseCommand
from shoes.models import ShoeColor, ShoeType


class Command(BaseCommand):
    help="This command populates tables for shoetype and shoescolor"
    
    def handle(self, *args, **options):
        ShoeType.objects.bulk_create(
            [
            ShoeType(style = 'cleats'),
            ShoeType(style = 'sneaker'),
            ShoeType(style = 'boot'),
            ShoeType(style = 'sandal'),
            ShoeType(style = 'dress'),
            ShoeType(style = 'other')
            ])
        
        ShoeColor.objects.bulk_create(
            [
                
                ShoeColor(color_style = 'magenta'),
                ShoeColor(color_style = 'blue'),
                ShoeColor(color_style = 'orange'),
                ShoeColor(color_style = 'violet'),
                ShoeColor(color_style = 'green'),
                ShoeColor(color_style = 'red'),
                ShoeColor(color_style = 'black'),
                ShoeColor(color_style = 'indigo'),
                ShoeColor(color_style = 'yellow')
            ])
        print(options)
        print("done") 