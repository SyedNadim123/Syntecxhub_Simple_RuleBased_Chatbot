SyntecxHub AI Internship - Project 1
Simple Rule Based Chatbot
About this project
This project was built as part of the Artificial Intelligence Internship Program at SyntecxHub. The goal of this internship task was to design and build a simple rule based chatbot in Python that can hold a basic conversation, answer domain specific questions, and keep a record of every conversation it has.
Why we built this chatbot
The purpose of this project was to understand how conversational systems work before moving on to more advanced AI techniques. A rule based chatbot is the foundation of natural language processing systems. By building this from scratch, we learned how computers interpret human text input, how pattern matching can be used to detect intent, and how a simple knowledge base can be used to answer specific questions without using any external AI model or API. This project demonstrates the core logic that more advanced chatbots, including AI powered ones, are built on top of.
What the chatbot does
The chatbot runs in the console and waits for the user to type a message. Based on the message, it does one of the following things.
It checks if the message matches an exit command such as bye or exit, and ends the conversation if it does.
It checks if the message matches a question stored in the knowledge base, such as questions about SyntecxHub or the internship program, and replies with the correct answer.
It checks if the message contains a greeting such as hi, hello, or hey, and responds with a greeting back.
It checks if the message is asking for help, and explains what the chatbot can do.
It checks if the message is asking how the chatbot is doing, and responds accordingly.
If none of these match, it gives a fallback response letting the user know it did not understand the input.
Every single message from the user and every reply from the chatbot is saved into a log file with a timestamp in the file name, so a complete record of the conversation is always available afterward.
How we built it step by step
Step one was creating the basic structure of the program. We built a loop that continuously asks the user for input using the input function, and the loop only stops when the user types bye or exit. This created the foundation for an interactive console based application.
Step two was adding intent detection. We used simple keyword and pattern checking with if and elif statements to detect what kind of message the user sent. We grouped these into categories called intents, such as greeting, help, and small talk, and gave each one a fixed response.
Step three was building a small knowledge base. We created a Python dictionary where the keys were common questions related to SyntecxHub and the internship program, and the values were the correct answers. When the user types a question that matches a key in this dictionary, the chatbot retrieves and prints the matching answer.
Step four was adding conversation logging. We used the datetime module to generate a unique log file name every time the program runs, based on the exact date and time. We created a function that writes every message, both from the user and from the chatbot, into this log file using file handling in append mode. This way, nothing is lost even if the chatbot is run multiple times, since each run creates its own separate log file.
Step five was improving the visual presentation. We installed and used the colorama library to add color to the console output, so that the user’s messages and the chatbot’s replies are easy to tell apart visually. This made the chatbot feel more polished and professional.
Technologies used
Python was used as the programming language for the entire project. The datetime module from the Python standard library was used to generate timestamped log file names. The colorama library was used to add color formatting to the console output. No external AI models, APIs, or paid services were used. The entire logic runs locally and offline.
How to run this project
Make sure Python is installed on your computer. Open the project folder in a code editor such as Visual Studio Code. Install the colorama library by running pip install colorama in the terminal. Run the chatbot using python chatbot.py. Type messages into the console and press enter to chat with the bot. Type bye or exit to end the conversation. After the conversation ends, a new log file will appear in the project folder containing the full transcript.
Project files
chatbot.py contains the full source code for the chatbot.
The log files in this folder are sample transcripts generated automatically each time the chatbot is run, showing example conversations.
Conclusion
This project gave us hands on experience with core programming concepts including loops, conditional logic, dictionaries, functions, file handling, and third party library integration. It also gave us a clear understanding of how rule based natural language processing systems work, which is an important foundation before working with more advanced machine learning based chatbots in the future.
Built as part of the SyntecxHub Artificial Intelligence Internship Program.
