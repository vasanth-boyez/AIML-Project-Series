import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer

# Download NLTK data (run this only once)
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

class CollegeAdmissionBot:
    def __init__(self):
        self.context = {}
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.admission_info = {
            "procedures": "To apply for admission, you need to fill out the online application form, submit required documents, and pay the application fee.",
            "requirements": "Admission requirements include a completed application form, official transcripts, letters of recommendation, and a personal statement.",
            "deadlines": "The application deadlines are December 1st for early decision and March 15th for regular decision.",
            "scholarships": "We offer a variety of scholarships based on academic merit, financial need, and extracurricular involvement. Check our website for detailed information and application deadlines.",
            "contact": "You can contact the admission office via email at admissions@example.com or call us at (123) 456-7890.",
            "tours": "Campus tours are available Monday through Friday. You can schedule a tour on our website.",
            "housing": "We offer a range of housing options for students, including dormitories, apartments, and shared housing. Visit our housing portal for more details."
        }

    def greet(self):
        return "Hello! I'm here to help you with your college admission queries. How can I assist you today?"

    def farewell(self):
        return "Goodbye! Best of luck with your college admission process!"

    def preprocess_input(self, user_input):
        tokens = word_tokenize(user_input.lower())
        filtered_tokens = [self.lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in self.stop_words]
        return filtered_tokens

    def respond_to_question(self, question):
        tokens = self.preprocess_input(question)
        if any(word in tokens for word in ["procedure", "apply", "application"]):
            return self.admission_info["procedures"]
        elif any(word in tokens for word in ["requirement", "document"]):
            return self.admission_info["requirements"]
        elif any(word in tokens for word in ["deadline", "date", "time"]):
            return self.admission_info["deadlines"]
        elif any(word in tokens for word in ["scholarship", "financial", "aid"]):
            return self.admission_info["scholarships"]
        elif any(word in tokens for word in ["contact", "email", "phone"]):
            return self.admission_info["contact"]
        elif any(word in tokens for word in ["tour", "visit", "campus"]):
            return self.admission_info["tours"]
        elif any(word in tokens for word in ["housing", "dormitory", "apartment", "accommodation"]):
            return self.admission_info["housing"]
        else:
            return "I'm sorry, I don't understand that question. Could you please ask something else?"

    def ask_user(self, question):
        user_response = input(question + " ")
        self.context[question] = user_response
        return user_response

    def handle_interaction(self):
        print(self.greet())
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["bye", "goodbye"]:
                print(self.farewell())
                break
            response = self.respond_to_question(user_input)
            print("Bot:", response)
            if response.startswith("I'm sorry"):
                print("Can you please rephrase or ask something else?")

    def recall_context(self):
        if self.context:
            print("Here's what I remember from our conversation:")
            for question, answer in self.context.items():
                print(f" - {question}: {answer}")
        else:
            print("I don't have any previous context to recall.")

if __name__ == "__main__":
    bot = CollegeAdmissionBot()
    bot.handle_interaction()
    bot.recall_context()
