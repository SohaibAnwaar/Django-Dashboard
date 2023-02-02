from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

from .models import User
from .serializers import UserSerializer

class UserList(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id",
                type=int,
                required=True,
                description="User ID",
            ),
        ],
    )
    def delete(self, request, *args, **kwargs):
        pk = self.request.query_params.get('id')
        self.kwargs['pk'] = pk
        data = self.destroy(request, *args, **kwargs)
        return Response(data, status=status.HTTP_200_OK)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id",
                type=int,
                required=True,
                description="User ID",
            ),
        ],
    )
    def patch(self, request, *args, **kwargs):
        pk = self.request.query_params.get('id')
        user = get_object_or_404(pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

