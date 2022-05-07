# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework.reverse import reverse

from .models import UserProfile, Lift
from .serializers import UserProfileSerializer, LiftSerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework import generics

@api_view(['GET'])
def api_root(request):
    return Response({
        'users': reverse('user-list', request=request),
        'lifts': reverse('lift-list', request=request)
    })


class UserProfileList(generics.ListAPIView):
    """Lists all users"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.RetrieveAPIView):
    """Gives details on specific user"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileLifts(generics.ListAPIView):
    """Lists the lifts of a specific user"""
    serializer_class = LiftSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        username = self.kwargs['pk']
        return Lift.objects.filter(user_profile=username)


class UserProfileExercise(generics.ListAPIView):
    """Lists the instances of an exercise for a specific user"""
    serializer_class = LiftSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        username = self.kwargs['pk']
        exercise = self.kwargs['exercise']
        return Lift.objects.filter(user_profile=username, exercise=exercise)


class LiftList(generics.ListCreateAPIView):
    """Lists all lifts by all users"""
    queryset = Lift.objects.all()
    serializer_class = LiftSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)


class LiftDetail(generics.RetrieveUpdateDestroyAPIView):
    """Gives details on specific lift"""
    queryset = Lift.objects.all()
    serializer_class = LiftSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]