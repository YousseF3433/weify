from deep_translator import GoogleTranslator

def translation(text, src="en", to="ar"):
  default_dect = {"protfolio": "سابقه اعملنا"}
  try:
     if text in default_dect.keys():
        return default_dect[text]
     result = GoogleTranslator(source=src, target=to).translate(text)
     return result
  except Exception as e:
     print(f"there is error with translation: {e}")
     return "sorry there is a problem with translation right now."