from rest_framework import viewsets

from .models import Link, SideBar
from .serializers import LinkSerializer, SideBarSerializer, SideBarDetailSerializer


class LinkViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)


class SideBarViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SideBarSerializer
    queryset = SideBar.objects.filter(status=SideBar.STATUS_SHOW)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = SideBarDetailSerializer
        return super().retrieve(request, *args, **kwargs)
