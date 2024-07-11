from django.test import TestCase

# Create your tests here.

# test_quiz_bot.py
class MockSession:
    def __init__(self):
        self.data = {}
    
    def get(self, key, default=None):
        return self.data.get(key, default)
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def save(self):
        pass

def test_quiz_bot():
    session = MockSession()
    user_responses = ["5", "def"]
    
    all_bot_responses = []
    
    for response in user_responses:
        bot_responses = generate_bot_responses(response, session)
        all_bot_responses.extend(bot_responses)
    
    final_responses = generate_bot_responses("", session)
    all_bot_responses.extend(final_responses)
    
    for response in all_bot_responses:
        print(response)

if __name__ == "__main__":
    test_quiz_bot()

