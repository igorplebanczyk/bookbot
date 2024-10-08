import re

class SentimentAnalyzer:
    def __init__(self):
        # Expanded positive and negative word lists
        self.positive_words = {
            "happy", "joy", "love", "excited", "pleasant", "fantastic",
            "good", "wonderful", "amazing", "bright", "delight", "excellent",
            "beautiful", "successful", "peace", "positive", "grateful",
            "inspiring", "hope", "cheerful", "thrilling", "great",
            "satisfied", "content", "fabulous", "awesome", "blissful",
            "optimistic", "rewarding", "fantasy", "exhilarating", "incredible",
            "radiant", "wonder", "serene", "uplifting", "motivated",
            "remarkable", "marvelous", "joyous", "celebratory", "enchanting",
            "graceful", "kind", "generous", "friendly", "supportive",
            "successful", "fulfilling", "enthusiastic", "thriving", "amusing",
            "exciting", "invigorating", "loving", "passionate", "playful"
        }

        self.negative_words = {
            "sad", "angry", "hate", "miserable", "unpleasant", "horrible",
            "bad", "terrible", "dark", "depressing", "failure", "dreadful",
            "ugly", "hopeless", "negative", "fear", "pain", "disappointing",
            "frustrated", "disgusting", "awful", "sorrow", "regret",
            "anxiety", "rage", "suffer", "fail", "stress",
            "lonely", "dismal", "heartbreaking", "painful", "tragic",
            "stressful", "unhappy", "distressing", "discouraging", "despair",
            "devastating", "sorrowful", "terrifying", "shocking", "frightening",
            "disheartened", "hopeless", "unlucky", "burdened", "conflicted",
            "overwhelmed", "abysmal", "gloomy", "tense", "bitter"
        }

        # Modifier words for sentiment intensification or negation
        self.intensifiers = {"very", "extremely", "really", "incredibly", "somewhat"}
        self.negations = {"not", "never"}

    def analyze_sentiment(self, text: str) -> str:
        # Clean the text
        words = re.findall(r'\b\w+\b', text.lower())

        positive_count = 0
        negative_count = 0
        score = 1  # Default score

        for i, word in enumerate(words):

            # Check for negations
            if word in self.negations and i + 1 < len(words):
                next_word = words[i + 1]
                if next_word in self.positive_words:
                    score = -1
                    negative_count += 1
                elif next_word in self.negative_words:
                    score = 1
                    positive_count += 1
                continue

            # Check for modifiers
            if i > 0 and words[i - 1] in self.intensifiers:
                score = 2  # Double score for intensifiers

            if word in self.positive_words:
                positive_count += score
            elif word in self.negative_words:
                negative_count += score

        # Sentiment conclusion
        if positive_count > negative_count:
            return "Positive"
        elif negative_count > positive_count:
            return "Negative"
        else:
            return "Neutral"