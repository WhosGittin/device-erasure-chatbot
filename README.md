# Device Erasure Chatbot

**Joni Voutilainen**

## Overview

### The plan

I started this challenge by prompting ChatGPT with the assignment and asked how and with what tools should I start creating the chatbot. ChatGPT came up with the following architecture:

![The device erasure chatbot architecture](documentation/initial_architecture.png)

After going through AI's reasoning and familiarizing myself a bit more about these chosen tools, I decided to go with the plan.

While researching the tools depicted in the architecture plan above, I realized there's probably going to be some kind of cost associated with using them. After researching the topic in question, I learned that some of the tools, for example Amazon Bedrock, which provides LLM's for developers to use in their applications, uses a pricing model based on tokens consumed. So everytime your application uses the LLM, a token is used. So for the purpose of this project, I didn't want to incur any costs for myself, so I decided to first build the application locally without any AWS services. This way I could test and tinker with it freely without worrying about any costs associated with AWS services. After prompting chatgpt with this idea in mind, it came up with a solution as shown below:

![The plan to divide local and aws development](documentation/local_and_aws_division.png)

So the plan was to first develop a solution that works fully locally, but design and implement it in a way, that it's easy to plug in AWS services into it with minimal changes to the code. In the end I didn't manage to complete the plan as I visioned it in the beginning, as the hours I put in started to exceed what I felt comfortable with for a job recruitment assignment. The size and complicatedness of the project also started to creep up on me and I felt my expertise was not quite enough to handle everything by myself. So after a week of working hard on the assignment, I decided I had done enough to show my capabilities. Here's what I came up with.

### Project structure

- device-erasure-chatbot >
  - backend >
    - aitools > | Contains the functionality of how the LLM interacts with the tools
      - definitions.py | Contains Bedrock compatible definitions for the tools and for what they are used
      - executor.py | Handles dispatching of the tool asked by LLM
      - implementations.py | Contains the tools to get data from database and return it in a structured way
    - chat >
      - chat_interface.py
      - chat_service.py
      - fake_ai.py
    - database >
      - base.py
      - local.py
    - api.py
    - data_loader.py
    - models.py
    - requirements.txt
  - data >
    - example_records.json
  - documentation | materials for the final assignment report
  - erasure-chat-frontend >
    - src >
      - api >
        - chat.ts
      - App.css
      - App.tsx
      - index.css
  - scripts >
    - generate_data.py
  - tests >
    - test_executor.py
    - test_get_erasure.py

## How to run

## Decisions

## AI usage
