import abc
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from elasticsearch_dsl import Q, search
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework import generics

from .documents import UserDocument
from custom.api.serializers import UserSerializer
from custom.models import User


class PaginatedElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression."""

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()

            print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)


class SearchUsers(PaginatedElasticSearchAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    document_class = UserDocument

    def generate_q_expression(self, query):
        return Q(
            "bool",
            should=[
                Q("match", username=query),
                Q("match", first_name=query),
                Q("match", last_name=query),
            ],
            minimum_should_match=1,
        )


def search_view(request):
    query = request.GET.get("q", "")
    results = search.query(
        "bool",
        should=[
            Q("match", username=query),
            Q("match", first_name=query),
            Q("match", last_name=query),
        ],
        minimum_should_match=1,
    ).execute()
    serialized_results = [{"username": hit.username} for hit in results]
    return JsonResponse({"results": serialized_results})
