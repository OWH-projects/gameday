from gameday.models import * 
from django.shortcuts import * 
from django.db.models import * 

def Opponent(request,season,team):
    gameday = Game.objects.filter(season=season).get(slug=team)
	
    dictionaries = { 'gameday': gameday, }
    return render_to_response('gameday/opponent.html', dictionaries)

	
def Main(request):
    games = Game.objects.order_by('-date')
	
    dictionaries = { 'games': games, }
    return render_to_response('gameday/main.html', dictionaries)
