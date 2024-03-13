from django.urls import path

from point.views import PointView, PointListView, PointListDetailView, PointChargeView, PointUseListView, \
    PointUseDetailView, PointDetailView

app_name = 'point'

urlpatterns = [
    path('new/', PointView.as_view(), name='new'),
    path('list/', PointListView.as_view(), name='list'),
    path('use/',PointUseListView.as_view(), name='use'),
    path('useDetail/',PointUseDetailView.as_view(), name='useDetail'),
    path('detail/<int:price>/', PointDetailView.as_view(), name='detail'),
    # path('api/',PointApiView.as_view(), name='api'),
    path('charge/',PointChargeView.as_view(), name='charge'),
    path('detail/', PointListDetailView.as_view(), name='detaillist')
]