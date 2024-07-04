import openai
from googletrans import Translator

# Set up OpenAI API Key
openai.api_key = ''

def translate(word):
    translator = Translator()
    languages = ['es', 'en', 'ru', 'pt', 'it', 'fr', 'de', 'ko']
    translation = {}

    for lang in languages:
        translation[lang] = translator.translate(word, dest=lang).text

    return translation

def get_word_info(word):
    prompt = f"Provide the definition and a usage example for the word '{word}'."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        definition_and_usage = response.choices[0].message['content'].strip()
        
        result = {
            'word': word,
            'definition_and_usage': definition_and_usage,
            'translations': translate(word)
        }
        return result
    
    except openai.error.RateLimitError:
        print("Rate limit exceeded. Please wait and try again later.")
        return "Rate limit exceeded. Please wait and try again later."
    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"


