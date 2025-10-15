# test_app.py
import unittest
from main import chat_backend
from pydantic import BaseModel

class DummyRequest(BaseModel):
    question: str

class TestChatbot(unittest.TestCase):

    def test_chat_backend(self):
        req = DummyRequest(question="What is Gemini?")
        resp = chat_backend(req)
        self.assertIsInstance(resp.answer, str)

if __name__ == "__main__":
    unittest.main()
