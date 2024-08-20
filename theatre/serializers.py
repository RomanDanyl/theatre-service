from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from theatre.models import Actor, Genre, Play, TheatreHall


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            "id",
            "first_name",
            "last_name",
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class PlayListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Play
        fields = ("id", "title", "description", "actors", "genres")


class PlayDetailSerializer(PlayListSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Play
        fields = ("id", "title", "description", "actors", "genres")


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_row",
        )

    def validate_rows(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "The number of rows must be greater than zero."
            )
        return value

    def validate_seats_in_row(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "The number of seats per row must be greater than zero."
            )
        return value
