import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK data (run this only once)
# nltk.download('punkt')
# nltk.download('stopwords')

class SimpleChatbot:
    def __init__(self):
        self.context = {}
        self.stop_words = set(stopwords.words('english'))

    def greet(self):
        return "Hello! How can I assist you today?"

    def farewell(self):
        return "Goodbye! Have a great day!"

    def preprocess_input(self, user_input):
        tokens = word_tokenize(user_input.lower())
        filtered_tokens = [word for word in tokens if word.isalnum() and word not in self.stop_words]
        return filtered_tokens

    def respond_to_question(self, question):
        responses = {
            "name": "I am Nexus Bot.",
            "how": "I'm just a bot, but I'm doing great!",
            "what": "I can assist you with basic questions and remember our conversation.",
            "joke": "Why don't scientists trust atoms? Because they make up everything!",
            "who": "I was created by the Nexus Info team."
        }
        
        tokens = self.preprocess_input(question)
        for key in responses:
            if key in tokens:
                return responses[key]
        return "I'm sorry, I don't understand that question."

    def ask_user(self, question):
        user_response = input(question + " ")
        self.context[question] = user_response
        return user_response

    def handle_interaction(self):
        print(self.greet())
        for question in ["What is your name?", "How can I help you?", "Do you like chatbots?"]:
            self.ask_user(question)
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["bye", "goodbye"]:
                print(self.farewell())
                break
            response = self.respond_to_question(user_input)
            print("Bot:", response)
            if response == "I'm sorry, I don't understand that question.":
                print("Can you please rephrase or ask something else?")

    def recall_context(self):
        if self.context:
            print("Here's what I remember from our conversation:")
            for question, answer in self.context.items():
                print(f" - {question}: {answer}")
        else:
            print("I don't have any previous context to recall.")

if __name__ == "__main__":
    bot = SimpleChatbot()
    bot.handle_interaction()
    bot.recall_context()
