try:
    from google.cloud import translate_v2 as translate
    import os

    def translate_text(text, target="ar"):
        client = translate.Client()
        result = client.translate(text, target_language=target)
        return result["translatedText"]

except ImportError:
    from googletrans import Translator
    translator = Translator()

    def translate_text(text, target="ar"):
        return translator.translate(text, dest=target).text
