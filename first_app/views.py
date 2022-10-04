from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .filter import BookFilter
from .serializers import BookSerializer, PublisherSerializer
from .models import Book, Publisher


# Create your views here.
def hello(request, name: str, num: int):
    return HttpResponse(f"{num}. {name.title()}, welcome to Django")


def index(request):
    context = [1, 2, 5]

    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
           "dolore magna aliqua. "
    return render(request, "first_app/index.html", context={"obj": context,
                                                            "name": "Wale", "is_major": False, "text": text})


def redirect(request):
    print(reverse('first_app:about'))
    return HttpResponseRedirect(reverse('first_app:about'))


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        # serializer = BookSerializer(queryset, many=True, context={'request': self.request})
        # the comment was changed in the serializer to return link
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data)

    elif request.method in ('PUT', 'PATCH'):
        serializer = BookSerializer(book, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def publisher_detail(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'GET':
        serializer = PublisherSerializer(publisher, context={'request': request})
        return Response(serializer.data)

    elif request.method in ('PUT', 'PATCH'):
        serializer = PublisherSerializer(publisher, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def about(request):
    return render(request, 'first_app/about.html')


@api_view()
def publisher_detail(request, pk):
    try:
        publisher = Publisher.objects.get(pk=pk)
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)
    except Publisher.DoesNotExist:
        return Response({"error": "could not find resource for publisher"}, status=status.HTTP_404_NOT_FOUND)


@api_view()
def publisher_list(request):
    queryset = Publisher.objects.all()
    serializer = PublisherSerializer(queryset, many=True)
    return Response(serializer.data)
