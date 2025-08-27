from translate import Translator

while True:
  lang = input("Enter first two letters of language you want to translate to: ")

  if lang in ("es"):
    try:
      words = input("Enter what to translate: ")
    except ValueError:
      print("Invalid input. Sorry.")
      continue

    translator = Translator(to_lang=lang)
    translation = translator.translate(words)
    print(translation)
    
    otherwise = input("Anything else? (yes/no): ")
    if otherwise == "no":
      break
      