from django.conf.urls import url,include
from RestOne.views import EmailRUDView,EmailCreateView,EmailListCreateMixinView,EmailListView
urlpatterns = [
    url(r'^(?P<pk>\d+)/$',EmailRUDView.as_view(),name="apiRUDView"),
    url(r'^$',EmailCreateView.as_view(),name="apiCreateView"),
    url(r'^mixins/$',EmailListCreateMixinView.as_view(),name="apiListCreateView"),
    url(r'^listview/$',EmailListView.as_view(),name="ListView"),
]
