from django.urls import path

from dungeons.apis import DungeonDetailApi

dungeons_patterns = [
    path('<int:pk>/', DungeonDetailApi.as_view({'get': 'retrieve'}), name='dungeon_detail'),
]

urlpatterns = dungeons_patterns
