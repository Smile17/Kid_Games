import os
import shutil
import codecs
import numpy as np
from Kid_Games.cards_gallery.models import Card, CardItem

directory = r'C:\Users\kam\PycharmProjects\Python_Django\Content_Maker\results\ukr_alphabet'
prefix = 'ukr_alpha'
target_directory = r'C:\Users\kam\PycharmProjects\Python_Django\Kid_Games\uploads'
images = []
d = os.path.join(directory, 'image')
for filename in os.listdir(d):
    source = os.path.join(d, filename)
    target = os.path.join(target_directory, 'image', prefix + '_' + filename)
    shutil.copy(source, target)
    images.append('image' + "/" + prefix + '_' + filename)
audios = []
d = os.path.join(directory, 'audio')
for filename in os.listdir(d):
    source = os.path.join(d, filename)
    target = os.path.join(target_directory, 'audio', prefix + '_' + filename)
    shutil.copy(source, target)
    audios.append('audio' + "/" + prefix + '_' + filename)

slugs = np.arange(1, len(audios) + 1)
slugs = [prefix + str(s) for s in slugs]

titles = []
f = os.path.join(directory, 'title.txt')
with codecs.open(f, encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        titles.append(line[0])

for slug, title, image, audio in zip(slugs, titles, images, audios):
    obj = Card(slug=slug, title=title, image=image, audio=audio)
    obj.save()

parent = Card.objects.get(slug='ukr_alpha')
for slug in slugs:
    child = Card.objects.get(slug=slug)
    obj = CardItem(parent=parent, child=child)
    obj.save()






