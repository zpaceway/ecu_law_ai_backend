from os import getenv, environ
from typing import Optional, List
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex
from django.conf import settings
from pathlib import Path
import json

OPENAI_API_KEYS = json.loads(getenv("OPENAI_API_KEYS"))


def set_openai_api_key(api_key: str):
    environ["OPENAI_API_KEY"] = api_key


class ChatBotIndex:
    instance: GPTSimpleVectorIndex = None
    selected_index_api_key = 0

    def __init__(self) -> None:
        openai_api_key = OPENAI_API_KEYS[self.selected_index_api_key]
        set_openai_api_key(openai_api_key)
        self.train_model()

    def refresh_model(self):
        self.train_model()

    def get_next_possible_api_key(self) -> str:
        self.selected_index_api_key = (
            self.selected_index_api_key + 1
            if self.selected_index_api_key + 1 < len(OPENAI_API_KEYS)
            else 0
        )
        openai_api_key = OPENAI_API_KEYS[self.selected_index_api_key]

        return openai_api_key

    def train_model(self, tried: Optional[List[str]] = None):
        openai_api_key = OPENAI_API_KEYS[self.selected_index_api_key]
        tried = tried or []
        print(
            f"trying api key {OPENAI_API_KEYS[self.selected_index_api_key]} , {tried}"
        )
        try:
            tried.append(openai_api_key)

            documents = SimpleDirectoryReader(
                Path.joinpath(settings.BASE_DIR, settings.MEDIA_ROOT)
            ).load_data()

            self.instance = GPTSimpleVectorIndex(documents)

        except:
            openai_api_key = self.get_next_possible_api_key()
            set_openai_api_key(openai_api_key)

            if not openai_api_key in tried:
                return self.train_model(tried)

            return


chat_bot_index = ChatBotIndex()
