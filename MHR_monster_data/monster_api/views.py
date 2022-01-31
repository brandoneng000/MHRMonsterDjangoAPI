from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
import requests
from rest_framework.decorators import api_view
from rest_framework import generics

from .serializers import MonsterHZVSerializer, MonsterSerializer
from .models import Monster, Monster_HZV

# Create your views here.
class MonsterViewSet(viewsets.ModelViewSet):
    queryset = Monster.objects.all().order_by('id')
    serializer_class = MonsterSerializer

class MonsterHZVs(generics.ListAPIView):
    serializer_class = MonsterHZVSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Monster_HZV.objects.all()
            monster = self.request.GET.get('monster_id', None)
            if monster is not None:
                queryset = queryset.filter(monster_id=monster)
            return queryset


def monster_list(request):
    response = requests.get('http://127.0.0.1:8000/monsterdata/monster/')
    
    monsters = response.json()
    for mon in monsters:
        mon['monster_image'] = 'monster_api/'+ str(mon['id']) +'.png'
    print(len(monsters))
    print("\n\n\n\n")

    return render(request, "home.html", {'monsters': monsters})

def monster_detail(request, pk):
    response = requests.get('http://127.0.0.1:8000/monster-hzv/?monster_id=' + str(pk))
    name = requests.get('http://127.0.0.1:8000/monsterdata/monster/' + str(pk) + '/')
    
    monster_name = name.json()
    image = 'monster_api/'+ str(pk) +'.png'

    monster_hzv = response.json()
    monster_hzv.append(image)
    monster_hzv.append(monster_name['monster_name'])
    # print(monster_hzv)
    print(len(monster_hzv))
    print("\n\n\n\n")

    return render(request, "monster_detail.html", {'monster_hzv': monster_hzv})