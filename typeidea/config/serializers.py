from rest_framework import serializers

from .models import Link, SideBar


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = (
            'id', 'title', 'href', 'created_time'
        )


class SideBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = SideBar
        fields = (
            'id', 'title', 'display_type', 'created_time'
        )


class SideBarDetailSerializer(SideBarSerializer):
    class Meta:
        model = SideBar
        fields = (
            'id', 'title', 'display_type', 'content', 'created_time'
        )
