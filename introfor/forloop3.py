#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# loop across the list called farms

for x in farms:
    print("\nThe farm name is " + x.get("name"))
    for crop in x.get("agriculture"):
        print(crop + "--")
print("/nOur loop has ended.")
