import speech_recognition as sr
from colorama import Fore, Style, init
from deep_translator import GoogleTranslator
import argostranslate.translate as translator

init(autoreset=True)


def listen_and_translate():
    """translate to English."""
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300     # mice sensitivity
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 1.5

    with sr.Microphone() as source:
        print(Fore.YELLOW + "Calibrating for background noise...", end="", flush=True)
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("\r" + " " * 40 + "\r", end="", flush=True)

        print(Fore.LIGHTGREEN_EX + "🎤 Listening... (speak now)", flush=True)

        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)
        except sr.WaitTimeoutError:
            print(Fore.RED + "⏱  No speech detected. Try again.")
            return None

    print(Fore.LIGHTYELLOW_EX + "🔄 Recognizing...", flush=True)

    try:
        # Urdu speech recognition (Pakistan)
        urdu_text = recognizer.recognize_google(audio, language="ur-PK")  # Detection lang
    except sr.UnknownValueError:
        print(Fore.RED + "❌ Could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(Fore.RED + f"❌ Google API error: {e}")
        return None

    print(Fore.CYAN + f"🗣  You said (Urdu): {urdu_text}")




    # try:
    #     # FIXED: Using deep-translator instead of mtranslate
    #     english_text = translator.translate(urdu_text, "ur", "en")
    # except Exception as e:
    #     print(Fore.RED + f"❌ Translation failed: {e}")
    #     return None
    #
    # print(Fore.BLUE + f"🇬🇧 English: {english_text}")
    return urdu_text



if __name__ == "__main__":
    print(Fore.MAGENTA + "=" * 50)
    print(Fore.MAGENTA + "   Urdu → English Voice Translator")
    print(Fore.MAGENTA + "   Press Ctrl+C to quit")
    print(Fore.MAGENTA + "=" * 50)

    while True:
        try:
            result = listen_and_translate()
            if result:
                print(Fore.GREEN + "-" * 50, flush=True)
        except KeyboardInterrupt:
            print(Fore.MAGENTA + "\n👋 Goodbye!")
            break