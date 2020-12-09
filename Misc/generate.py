#!/usr/bin/env python3
import sys
import os
import random

def writeListToF(name,items):
	with open(name,'w') as f:
		for item in items:
			f.write('\n'+item)

Groceries = ["Apple","Bananna","Cucumber","Soylent Green","Pasta",
		"rice","Honey Bunches of Oats", "Ketchup","Hot dogs",
		"hot dog buns", "soup","tomatoes","Tuna","Salmon",
		"Kidney beans", "Pears","Oranges","Waffles","eggs",
		"Lettuce","squash","zucchini","mushrooms"] 

Shopping = ["Pens","Pencils","Markers",
	   'Highlighters','Paper clips','Tape','Rubber bands',
	   'Erasers', 'Stamp pads', 'Ink for stamp pads',
	   'Staples', 'Fasteners','Glue','Glue sticks',
           'push-pins','3–ring binders']


#make topline
writeListToF("GroceriesList.txt",Groceries)
writeListToF("ShoppingList.txt",Shopping)

# Make Dirs 
ndir = './completed'
if not os.path.exists(ndir):
	os.makedirs(ndir)

# make past items
months = ["Jan",'Feb','Mar','Apr','Jun','Jul','Sep','Oct','Nov','Dec']
days = list(range(1,28))
n_files = 10

UnifiedList = Groceries+Shopping

for n in range(0,n_files):
	filename = random.choice(months)+str(random.choice(days))+'.txt'
	n_items = random.randint(10,30)
	items = random.choices(UnifiedList,k=n_items)
	writeListToF('./completed/'+filename,items)