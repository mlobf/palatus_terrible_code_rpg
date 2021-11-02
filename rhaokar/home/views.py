from django.shortcuts import render
from django.http import HttpResponse

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def index(request):
    return render(request, "index.html")

def mapa(request):
    return render(request, "./world/maps/mapa.html")

def ancestries(request):
    return render(request, "./ancestries/ancestries.html")

def alchfeats(request):
    return render(request, "./alchemy/alchfeats/alchfeats.html")

def alchitens(request):
    return render(request, "./alchemy/alchitens/alchitens.html")

def grafts(request):
    return render(request, "./alchemy/grafts/grafts.html")

def symbionts(request):
    return render(request, "./alchemy/symbionts/symbionts.html")

def alchemy(request):
    return render(request, "./alchemy/alchemy.html")

def common(request):
    return render(request, "./ancestries/common/common.html")

def uncommon(request):
    return render(request, "./ancestries/uncommon/uncommon.html")

def rare(request):
    return render(request, "./ancestries/rare/rare.html")

def universal(request):
    return render(request, "./ancestries/universal/universal.html")

def campaign(request):
    return render(request, "./logs/campaign/campaign.html")

def characters(request):
    return render(request, "./logs/characters/characters.html")

def hall(request):
    return render(request, "./logs/hall/hall.html")

def logs(request):
    return render(request, "./logs/logs.html")

def mudancas(request):
    return render(request, "./magic/mudancas/mudancas.html")

def magicarquetypes(request):
    return render(request, "./magic/magicarquetypes/magicarquetypes.html")

def magicitens(request):
    return render(request, "./magic/magicitens/magicitens.html")

def newpowers(request):
    return render(request, "./magic/newpowers/newpowers.html")

def magic(request):
    return render(request, "./magic/magic.html")

def techcreations(request):
    return render(request, "./tech/techcreations/techcreations.html")

def techfeats(request):
    return render(request, "./tech/techfeats/techfeats.html")

def techitens(request):
    return render(request, "./tech/techitens/techitens.html")

def tech(request):
    return render(request, "./tech/tech.html")

def cosmos(request):
    return render(request, "./world/cosmos/cosmos.html")

def entities(request):
    return render(request, "./world/gods/entities/entities.html")

def faecourts(request):
    return render(request, "./world/gods/faecourts/faecourts.html")

def herogods(request):
    return render(request, "./world/gods/herogods/herogods.html")

def oldgods(request):
    return render(request, "./world/gods/oldgods/oldgods.html")

def gods(request):
    return render(request, "./world/gods/gods.html")

def kingdoms(request):
    return render(request, "./world/kingdoms/kingdoms.html")

def cenario(request):
    return render(request, "./world/cenario.html")