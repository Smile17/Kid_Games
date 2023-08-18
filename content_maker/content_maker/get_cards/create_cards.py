import os
import shutil
import codecs
from cards_gallery.models import Card, CardItem
from django.utils.text import slugify

directory = r'C:\Users\kam\Documents\projects\Kid_Games\content_maker\results\syllables\M'
prefix = 'ukr_alpha17'
target_directory = r'C:\Users\kam\Documents\projects\Kid_Games\uploads'
images = []
d = os.path.join(directory, 'image')
for filename in os.listdir(d):
    source = os.path.join(d, filename)
    target = os.path.join(target_directory, 'image', prefix + '_' + filename)
    shutil.copy(source, target)
    images.append('image' + "/" + prefix + '_' + filename)
images = sorted(images)
audios = []
d = os.path.join(directory, 'audio')
for filename in os.listdir(d):
    source = os.path.join(d, filename)
    target = os.path.join(target_directory, 'audio', prefix + '_' + filename)
    shutil.copy(source, target)
    audios.append('audio' + "/" + prefix + '_' + filename)
audios = sorted(audios)

slugs = range(1, len(audios) + 1)
slugs = [prefix + "_" + str(s) for s in slugs]

titles = []
f = os.path.join(directory, 'title.txt')
with codecs.open(f, encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        titles.append(line.replace('\n', '').replace('\r', ''))
titles = sorted(titles)

slugs = []
for title in titles:
    slugs.append(slugify(title))

for slug, title, image, audio in zip(slugs, titles, images, audios):
    obj = Card(slug=slug, title=title, image=image, audio=audio)
    obj.save()

parent = Card.objects.get(slug=prefix)
for slug in slugs:
    child = Card.objects.get(slug=slug)
    obj = CardItem(parent=parent, child=child)
    obj.save()






