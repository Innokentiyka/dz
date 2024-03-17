from rest_framework import  filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Payment
from .serializers import PaymentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework import permissions
from .models import Course
from .serializers import CourseSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import UserSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['payment_date']


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    # Разрешаем доступ неаутентифицированным пользователям
    permission_classes = ()