# haikyuuBot
his project is an interactive, character-driven AI chatbot inspired by Hinata Shoyo from Haikyuu!!.

The system uses a locally hosted Large Language Model (LLM) and custom UI animations to create an immersive conversational experience that feels like chatting with an anime character.

Unlike standard chatbots, this project integrates:

Personality-constrained prompting

Animated UI interactions

Themed visual design

Hidden interactive “special move” triggers

🎯 Objective

To explore how prompt engineering, UI design, and animation can transform a basic LLM chatbot into an engaging, character-consistent interactive experience.

This project demonstrates how AI systems can be enhanced through:

Strong persona conditioning

Frontend animation effects

Context memory handling

Thematic user interaction design

🧠 Core Features
🟠 Character Persona System

The chatbot is strictly instructed to:

Speak energetically

Use volleyball metaphors

Encourage the user like a teammate

Stay in-character at all times

Prompt engineering ensures persona consistency.

🏐 Animated Interaction Effects

When a user sends a message:

A volleyball toss animation plays

A rolling volleyball loader appears while generating a response

A “SPIKE” success message appears after reply

This creates a dynamic interaction rather than static text exchange.

⚡ Hidden Easter Egg – “Quick Attack”

If the user types:

quick attack


The system triggers:

Full white-screen flash (2 seconds)

Orange burst animation

Faster rolling animation

Special formatted reply styling

This gamifies the chatbot experience and adds interactivity beyond standard messaging.

🎥 Full-Screen Video Background

The interface includes:

Embedded looping Haikyuu-themed video

Dark overlay for readability

Fixed-position chat input

Custom sidebar styling

The UI is designed to feel immersive and anime-themed rather than minimalistic.

⚙️ Tech Stack

Python

Streamlit (Frontend UI)

Ollama (Local LLM inference)

Custom CSS animations

Base64 video embedding

🏗 Architecture

User Input →
Session Memory →
LLM (Gemma model via Ollama) →
Persona Prompt Conditioning →
Animated UI Rendering →
Response Display

The system maintains conversational memory using Streamlit session state.

💡 Key Concepts Demonstrated

Prompt engineering for personality consistency

Stateful conversation handling

Interactive UI design with CSS animations

Event-triggered UI transformations

Character-driven AI UX design
