# AI-Voice-Assistant-
AI-powered Python Voice Assistant that uses speech recognition and text-to-speech to perform tasks like web search, automation, email, and voice-based system control.

🚀 Project Overview

This project is a Python-based AI Voice Assistant designed to interact with users through natural voice commands and spoken responses. The assistant listens through the microphone, converts speech into text, understands the command, and performs useful real-world tasks automatically. It acts like a basic personal desktop assistant that helps users operate their system and access information without using a keyboard or mouse. The system demonstrates how speech recognition, text-to-speech, and automation libraries can be combined to build an intelligent interactive assistant. The project is fully modular, allowing multiple assistant versions and feature extensions such as calling and email support.

🎯 Project Objective

The main objective of this project is to create a smart, voice-controlled assistant that can improve human–computer interaction through hands-free operation. Instead of manually executing commands, users can speak naturally and receive instant audio feedback. The project focuses on applying AI-based speech recognition and voice synthesis in a practical way. It is built as an academic and real-world demonstration of how intelligent assistants work at a basic level and how automation can be integrated into everyday computing tasks.

🧠 System Working Principle

The assistant works in a continuous listening loop using the system microphone. When the user speaks, the audio input is captured and processed by a speech recognition engine that converts spoken language into text. This recognized text is then analyzed and matched with predefined command patterns. Based on the detected command, the assistant performs specific actions such as opening websites, searching online knowledge sources, playing music, or sending messages. After executing the task, the system generates a spoken reply using a text-to-speech engine so the user receives confirmation and results in audio form. Some modules also connect with external communication services to trigger phone calls, showing how the assistant can be extended beyond local system control.

🛠️ Technologies Used

This project is implemented completely in Python and uses multiple specialized libraries for voice and automation features. Speech recognition functionality is handled through a speech processing library that converts microphone audio into text commands. Text-to-speech output is generated using a voice engine that produces natural spoken responses. Online knowledge lookup is supported through a Wikipedia integration library. System and browser automation are handled using built-in OS and web control modules. Email functionality is implemented using SMTP protocol, and an external communication API library is used for automated calling features. Together, these technologies create a complete voice-driven assistant platform.

⚙️ Core Features

The voice assistant can greet the user based on the current time and respond conversationally. It can search topics and read summaries, open commonly used websites, launch browser pages, and play music from the local computer. It is capable of telling the current system time and executing application launch commands. The assistant also includes an email sending feature through configured credentials and an optional calling feature using an external service API. Multiple assistant script versions are included in the project to demonstrate alternative implementations and feature sets. The assistant supports continuous interaction mode so users can give commands repeatedly without restarting the program.

▶️ How to Run the Project

To run this project, first install all required Python packages listed in the requirements file. A working microphone must be connected and properly configured on the system so that voice input can be captured. After installing dependencies, open the project folder in the terminal or command prompt and run the main assistant file. Before using features like email or calling, configure credentials using placeholder values and never publish real passwords in a public repository. Once the program starts, speak commands clearly and wait briefly for recognition and response.

Run command:
python chandler.py

📦 Project Structure

The project contains multiple assistant implementation files that demonstrate different command handling styles and feature extensions. The main assistant file handles voice interaction and task execution. Supporting files include alternate assistant versions, communication API integration, and credential configuration templates. This modular structure allows easy upgrades and experimentation with new features without breaking the core assistant logic.

🌍 Applications

This AI Voice Assistant can be used as a foundation for personal desktop assistants, accessibility tools for users who prefer hands-free control, and voice-based automation systems. It is useful for demonstrating speech recognition and AI interaction in academic projects and technical presentations. The same concept can be extended to smart home control, office automation, and voice-driven service systems.

🔮 Future Enhancements

The assistant can be significantly improved by adding natural language understanding instead of simple keyword matching. Future versions can include chatbot-style conversations, multilingual voice support, offline speech models, and mobile or web deployment. Integration with large language models can make responses more intelligent and context aware. Smart device control and IoT integration can also be added to transform it into a full smart assistant platform.
