
from django.urls import path
from .views import UserDetailUpdateView,RegisterView,PregnancyInfoView,journalListCreateView,JournalDeleteView,FAQListView


urlpatterns=[
    path('user/',UserDetailUpdateView.as_view(),name='user-detail'),
    path('register/',RegisterView.as_view(), name='register'),
    path('pregnancy/',PregnancyInfoView.as_view(),name='pregnancy-info'),
    path('journal/',journalListCreateView.as_view(),name='journal-list-create'),
    path('journal/<int:pk>/',JournalDeleteView.as_view(),name='journal-delete'),
    path('FAQ/',FAQListView.as_view(),name='faq-list'),

]