from datetime import datetime
from django.shortcuts import render

def date_actuelle(request):
	couleurs = {
	    'FF0000':'rouge', 
	    'ED7F10':'orange', 
	    'FFFF00':'jaune', 
	    '00FF00':'vert', 
	    '0000FF':'bleu', 
	    '4B0082':'indigo', 
	    '660099':'violet',
	}

	date = datetime.now().strftime("%A %d %B %Y - %H:%M")
	return render(request, 'blog/date.html', locals())


def addition(request, nombre1, nombre2):    
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())
