from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		#"baseball_leagues": League.objects.filter(sport="Baseball"),
		"baseball_leagues": League.objects.filter(sport__contains="baseball"), 		#1
		"women_leagues": League.objects.filter(name__contains="women"),				#2
		"all_hockey_leagues": League.objects.filter(sport__contains="hockey"),		#3
		"not_football_leagues": League.objects.exclude(sport__contains="football"),	#4
		"conferences_leagues": League.objects.filter(name__contains="conference"),	#5
		"all_leags_atlantic": League.objects.filter(name__contains="atlantic"),		#6
		"teams_house_dallas":Team.objects.filter(location__contains="dallas"),		#7
		"teams_whith_raptor":Team.objects.filter(team_name__contains="Raptors"),		#8
		"teams_startwhith_t":Team.objects.filter(team_name__startswith="T"),		#9
		"teams_with_city":Team.objects.filter(location__contains="city"),			#10
		"team_by_locations":Team.objects.all().order_by("location"),				#11
		"team_by_name":Team.objects.all().order_by("-team_name"),					#12
		"each_player_cooper":Player.objects.filter(last_name__contains="Cooper"),	#13
		"each_player_Joshua":Player.objects.filter(first_name__contains="Joshua"),	#14
		"all_player_cooper_less_joshua":Player.objects.filter(last_name__contains="Cooper").exclude(first_name__contains="Joshua"), #15
		"player_alexander_or_wyatt":Player.objects.filter(first_name__in=["Alexander","Wyatt"]), #16
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")