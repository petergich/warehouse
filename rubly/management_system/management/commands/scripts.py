from django.core.management.base import BaseCommand
import time
import datetime
import os
import json
from management_system.models import SKUs
import django

# Initialize Django
django.setup()
def create():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    data=SKUs.objects.all()
    model_data=[]
    for dat in data:
        purchase_order=str(dat.Purchase_Order)
        model_data.append([dat.Description,dat.Type,dat.Price,dat.Packaging,dat.Quantity,purchase_order])
    print(model_data)
    if now=="06:00":
        current_date = time.strftime("%Y%m%d")  # Generate a date-only timestamp
        directory = "data"
        # Create the directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_name = os.path.join("data", f"opening{current_date}.json")  # Create a file path within the "data" directory

        with open(file_name, 'w') as file:
            json.dump(model_data, file)
    if now=="16:00":
        current_date = time.strftime("%Y%m%d")  # Generate a date-only timestamp
        directory = "data"
        # Create the directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_name = os.path.join("data", f"closing{current_date}.json")  # Create a file path within the "data" directory

        with open(file_name, 'w') as file:
            json.dump(model_data, file)
class Command(BaseCommand):
    help = 'Runs a continuous task'

    def handle(self, *args, **options):
        while True:
            create()
            time.sleep(2)