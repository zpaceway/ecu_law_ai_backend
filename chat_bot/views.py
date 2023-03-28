from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from chat_bot import chat_bot_index


class ChatBotIndexView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        question = request.data["question"]
        response = chat_bot_index.instance.query(question)
        return Response({"response": response.__str__().strip()})
