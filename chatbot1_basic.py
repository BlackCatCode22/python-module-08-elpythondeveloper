# CIT-95-21257-2024SP: Python Programming
# Miguel Quezada
# Date: 05/17/2025
# File: chatbot1_basic.py
# Description: Simple Chatbot with the ability to remember previous conversations.

# Import the OpenAI library, which provides access to OpenAI's powerful language models.
import openai

# Prior to checking in my chatbot to the Class GitHub Repo I removed my API Key from here.
# Set your OpenAI API key here
openai.api_key = "YOUR OPENAI API KEY GOES HERE"

# Initialize an empty list to store the conversation messages.
# This list will hold a history of interactions between the user and the chatbot.
messages = []

# Prompt the user to define the chatbot's personality or purpose.
# Get the system message from the user, defining the chatbot's personality.
# The user's input will stored in variable system_msg and set the system role message for the chatbot.
system_msg = input("What type of chatbot would you like to create?\n")

# Append the user's defined system message which is stored in variable system_msg to the messages list.
# This tells the AI how it should behave or what its core function is.
messages.append({"role": "system", "content": system_msg})

# Display the string to the user, telling them that the chatbot is ready to interact.
print("Your new assistant is ready!")

# ---------- Start of the while loop ----------
# Start an infinite loop for continuous conversation until the user types quit().
while input != "quit()":
    # Get user input for their message to the chatbot.
    message = input()
    # Append the user's message to the messages list with the user role.
    messages.append({"role": "user", "content": message})

    # Call the OpenAI ChatCompletion API to get a response from the model.
    # model - specifies the AI model to use. In this chatbot I am using OpenAI's gpt-3.5-turbo model.
    # messages - provides the entire conversation history to the AI, allowing it to maintain context.
    # This call uses the 1.0.0 interface which uses dot notation (accessing attributes) 
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages)

    # Extract the text content of the AI's reply from the API response.
    # The response structure typically involves accessing choices, then the first choice by getting the first index[0],
    # then message, and finally content.
    # I'm access the response data using dot notation (accessing attributes) which is the new way, 
    # instead of bracket notation (accessing dictionary keys) which is the old way.
    reply = response.choices[0].message.content

    # Append the AI's reply to the messages list with the assistant role.
    # This keeps the conversation history complete for future turns.
    messages.append({"role": "assistant", "content": reply})

    # Print the AI's reply to the console and add newlines for better readability.
    print("\n" + reply + "\n")
# ---------- End of the while loop ----------

# ---------- References ----------
#
# ChatGPT in Python for Beginners - By AI Advantage
# https://www.youtube.com/watch?v=pGOyw_M1mNE
#
# OpenAI API - API keys
# https://platform.openai.com/api-keys
# On this page is where we set up OpenAI API keys
#
# OpenAI API - Usage
# https://platform.openai.com/usage
# On this page is where we check the usage of the requests we have made using OpenAI Keys.
#
# OpenAI API - Limits
# https://platform.openai.com/settings/organization/limits
# When we purchase OpenAI credit or add our credit card, we can set the monthly 
# minimum and maximum limit amounts of usage on this page. 
# For example if we set a minimum limit of $10, when our usage reaches $10 then
# we would get a notification email saying our usage reached $10.
# For example if we set a maximum limit of $20, when our usage reaches $20 then
# we would get a notification email saying our usage reached $20. Once we reach
# the maximum limit, any further OpenAI requests would just fail in our chatbot until
# we purchase more credit our increase the limit.
#
# ---------- References ----------
