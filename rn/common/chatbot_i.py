from abc import ABC, abstractmethod


class IChatbot(ABC):
    """
    Interface for simple chatbot that receives a question and returns a response.
    """

    def __init__(self):
        pass

    @abstractmethod
    def initialize(self, *args, **kwargs):
        pass

    @abstractmethod
    def answer(self, question, *args, **kwargs):
        pass