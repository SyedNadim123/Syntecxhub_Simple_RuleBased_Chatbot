import datetime
from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.CYAN + "=== SyntecxBot ===")

knowledge_base = {
    "what is syntecxhub": "SyntecxHub is a company offering internships in Web Development, UI/UX Design, Data Science, and more.",
    "how do i submit my project": "You submit projects through the official Submission Form and upload code to GitHub.",
    "how do i get my certificate": "Complete and submit at least one project from each task, and share your status on LinkedIn tagging @Syntecxhub."
}

log_filename = "conversation_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".log"

def log_and_print(speaker, message):
    line = f"{speaker}: {message}"
    if speaker == "SyntecxBot":
        print(Fore.GREEN + line)
    else:
        print(Fore.YELLOW + line)
    with open(log_filename, "a", encoding="utf-8") as f:
        f.write(line + "\n")

while True:
    user_input = input(Fore.YELLOW + "You: ").strip()

    if user_input == "":
        continue

    text = user_input.lower()

    with open(log_filename, "a", encoding="utf-8") as f:
        f.write(f"You: {user_input}\n")

    if text in ("bye", "exit"):
        log_and_print("SyntecxBot", "Goodbye!")
        break

    elif text in knowledge_base:
        log_and_print("SyntecxBot", knowledge_base[text])

    elif any(word in text for word in ["hi", "hello", "hey"]):
        log_and_print("SyntecxBot", "Hello! How can I help you?")

    elif "help" in text:
        log_and_print("SyntecxBot", "I can chat with you. Try saying hello, bye, or ask me something.")

    elif "how are you" in text:
        log_and_print("SyntecxBot", "I'm doing great, thanks for asking!")

    else:
        log_and_print("SyntecxBot", "Sorry, I didn't understand that.")