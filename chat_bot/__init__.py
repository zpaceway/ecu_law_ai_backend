from os import getenv
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex
from django.conf import settings
from pathlib import Path

OPENAI_API_KEY = getenv("OPENAI_API_KEY")


class ChatBotIndex:
    instance: GPTSimpleVectorIndex = None

    def __init__(self) -> None:
        self.train_model()

    def refresh_model(self):
        self.train_model()

    def train_model(self):
        documents = SimpleDirectoryReader(
            Path.joinpath(settings.BASE_DIR, settings.MEDIA_ROOT)
        ).load_data()

        self.instance = GPTSimpleVectorIndex(documents)


chat_bot_index = ChatBotIndex()
