from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from common.utils import inline_serializer
from paths.models import Path
from common.mixins import APIErrorsMixin
from paths.selectors import path_list


class PathListApi(APIView):
    permission_classes = [IsAuthenticated | IsAdminUser]

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Path
            fields = (
                'id',
                'title',
                'description'
            )

    def get(self, request):
        paths = path_list()

        data = self.OutputSerializer(paths, many=True).data

        return Response(data)


class PathDetailApi(APIErrorsMixin, APIView):
    permission_classes = [IsAuthenticated]


    class OutputSerializer(serializers.ModelSerializer):
        textures = inline_serializer(many=True, fields={
            'id': serializers.IntegerField(),
            'title': serializers.CharField(),
            'image': serializers.ImageField(),
        })
        dungeons = inline_serializer(many=True, fields={
            'id': serializers.IntegerField(),
            'title': serializers.CharField(),
            'image': serializers.ImageField(),
            'position': serializers.IntegerField(),
        })

        class Meta:
            model = Path
            fields = (
                'id',
                'title',
                'description',
                'textures',
                'dungeons',
            )

    def get(self, request, path: Path) -> Response:
        serializer = self.OutputSerializer(path)

        return Response(serializer.data)
