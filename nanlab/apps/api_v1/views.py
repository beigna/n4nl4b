from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException, ValidationError

from .serializers import IssueSerializer, BugSerializer, TaskSerializer
from .services import issue_create, bug_create, task_create


SERIALIZERS = {
    'issue': IssueSerializer,
    'bug': BugSerializer,
    'task': TaskSerializer,
}


class TrelloCardAPI(APIView):

    def post(self, request, format=None):
        card_type = request.data.get('type')

        if card_type not in SERIALIZERS.keys():
            raise ValidationError(f'"{card_type}" is invalid value for type')

        serializer = SERIALIZERS[card_type](data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        try:
            if card_type == 'issue':
                issue_create(
                    title=serializer.validated_data['title'],
                    description=serializer.validated_data['description'],
                )

            elif card_type == 'bug':
                bug_create(
                    description=serializer.validated_data['description']
                )

            elif card_type == 'task':
                task_create(
                    title=serializer.validated_data['title'],
                    category=serializer.validated_data['category']
                )

            else:
                raise APIException('Card type "{card_type}" not implemented')

        except Exception as e:
            raise APIException(e)

        return Response(status=201)
