from django.shortcuts import render
from rest_framework import viewsets

from theatre.models import Actor, Genre, Play, TheatreHall, Performance
from theatre.serializers import (
    ActorSerializer,
    GenreSerializer,
    PlayListSerializer,
    PlayDetailSerializer,
    TheatreHallSerializer,
    PerformanceListSerializer,
    PerformanceDetailSerializer,
    PerformanceSerializer,
)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PlayDetailSerializer
        return PlayListSerializer


class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PerformanceDetailSerializer
        if self.action == "list":
            return PerformanceListSerializer
        return PerformanceSerializer
