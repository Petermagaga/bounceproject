from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .pregnancy_data import WEEKLY_TIPS,TRIMESTER_NUTRITION

from rest_framework import generics,permissions
from .models import User,JournalEntry,FAQ
from .serializers import UserSerializer, registerSerializer,PregnancyInfoSerializer,journalEntrySerializer,FAQSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

User=get_user_model()

class UserDetailUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes=[AllowAny]
    serializer_class=registerSerializer

class PregnancyInfoView(APIView):
    permission_classes =[IsAuthenticated]

    def get(self,request):
        user=request.user
        if not user.pregnacy_start_date:
            return Response({"error":"Pregnancy start date not set."},status=400)
        days=(date.today() -user.pregnacy_start_date).days
        current_week=max(1,days//7)

        weekly_data=WEEKLY_TIPS.get(current_week, {
            "tip":"keep going consult your doct reg",
            "baby_size":"unkknown"})
        

        data={
            "current_week":current_week,
            "trimester":user.trimesster,
            "due_date":user.due_date,
            "baby_size":weekly_data["baby_size"],
            "weekly_tip":weekly_data["tip"],
            "nutrition_advice":TRIMESTER_NUTRITION.get(user.trimester, "Eat balanced and rest well."),
        }
        serializer=PregnancyInfoSerializer(data)
        return Response(serializer.data)
    

class journalListCreateView(generics.ListCreateAPIView):
    serializer_class=journalEntrySerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class JournalDeleteView(generics.DestroyAPIView):
    serializer_class=journalEntrySerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)
    
class FAQListView(generics.ListAPIView):
    queryset=FAQ.objects.all()
    serializer_class=FAQSerializer
    permission_classes=[AllowAny]
