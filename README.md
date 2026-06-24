SyntecxHub AI Internship Project 1
Simple Rule Based Chatbot

About this project

This is Project 1 from the SyntecxHub Artificial Intelligence Internship. The task was to build a simple chatbot in Python that can chat with a user in the console, answer a few questions about SyntecxHub, and save the conversation to a file.

Why we made this

We wanted to learn how a chatbot actually works before jumping into anything complicated. A rule based chatbot is the simplest type there is, it just checks what the user typed and matches it against some fixed rules to decide what to reply. Building it ourselves helped us understand how text input is read, how to check for keywords in a sentence, and how to store a small set of questions and answers so the bot can look them up. This is the same basic idea that bigger chatbots use, just on a much smaller scale.

What the chatbot can do

When you run the program, it keeps asking you to type something in the console. Depending on what you type, it does one of these things.

If you type bye or exit, it says goodbye and the program stops.

If your message matches one of the questions we stored about SyntecxHub or the internship, it gives you the answer for that question.

If your message has the word hi, hello or hey in it, it greets you back.

If your message has the word help in it, it tells you what the bot can do.

If your message asks how it is doing, it gives a short reply about that.

If none of the above match, it just says it did not understand the message.

Every message you type and every reply the bot gives gets saved into a text file. Each time you run the program, a new file is created with the date and time in its name, so you always have a record of that conversation.

How we built it, step by step

First we wrote a basic loop using the input function so the program keeps asking for text and only stops when you type bye or exit. This was just to get the chatbot running and talking back, even if it only repeated what you said at first.

Next we added a way to check what kind of message the user sent. We did this with simple if and elif checks looking for certain words, like hi or hello for a greeting, or help when someone needs help. Each of these checks has its own reply.

After that we added a small knowledge base. This is just a Python dictionary where each question is a key and the answer is the value. So when someone types a question that matches exactly, the bot looks it up in the dictionary and prints the answer.

Then we added logging. We used the datetime module to create a file name based on the exact time the program started, so every run gets its own log file. Every time the bot or the user says something, it gets written into that file as well as shown on the screen, so nothing is lost.

Last we added some color to the console using the colorama library, so the user's messages and the bot's replies show up in different colors and are easier to read.

What we used

Everything is written in plain Python. We used the datetime module that comes built into Python to create the log file names. We used a library called colorama to add colors to the text in the terminal. We did not use any AI model, any API, or any paid service, the whole thing runs on its own on your computer.

How to run it

Make sure Python is installed on your computer. Open this folder in a code editor like VS Code. Run this command once to install colorama, pip install colorama. Then run the chatbot by typing python chatbot.py. Once it starts, just type your messages and press enter. Type bye or exit when you want to stop. After you stop it, you will see a new log file appear in the folder with your conversation saved in it.

Files in this project

chatbot.py is the actual code for the chatbot.

The log files are example conversations that were saved automatically when we tested the bot.

What we learned

This project helped us practice loops, if and elif conditions, dictionaries, functions, and writing to files in Python. We also learned how to use an outside library in our code and how a basic chatbot decides what to reply based on simple rules. This gives us a good base before trying anything more advanced later on.

Made for the SyntecxHub Artificial Intelligence Internship.
