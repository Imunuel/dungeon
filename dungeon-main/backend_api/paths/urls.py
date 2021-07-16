from django.urls import path, register_converter

from paths.apis import PathListApi, PathDetailApi
from paths.converters import PathConverter

register_converter(PathConverter, 'path')


paths_patterns = [
    path('', PathListApi.as_view(), name='path_list'),
    path('<path:path>/', PathDetailApi.as_view(), name='path_detail'),
]

urlpatterns = paths_patterns
