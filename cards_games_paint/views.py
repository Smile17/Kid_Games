from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json

from cards_games_paint.models import PaintImageFile


@csrf_exempt
def paint(request):
    if request.method == 'GET':
        return render(request, 'cards_games_paint/paint.html')
    elif request.method == 'POST':
        filename = request.POST['save_fname']
        image = request.POST['save_image']
        file_data = PaintImageFile(name=filename, canvas_image=image)
        file_data.save()
        return HttpResponse("Done")
