# HalluGuard: Anti-Hallucination Extension for Chatbots

![HalluGuard Logo](https://github.com/aidandf29/HalluGuard/blob/main/HalluGuard.jpg)

## 📝 Project Description

**HalluGuard** is an anti-hallucination extension for chatbots designed to improve the reliability and accuracy of chatbot responses. Hallucination in chatbots occurs when the model generates inaccurate or irrelevant responses. HalluGuard uses the **TinyLlama-1.1B** model for classification and fact-checking, integrating the **Brave Search API** and **GPT API** as fallbacks for fact verification.

This project is developed using **Streamlit** for the user interface and **Node.js** for the backend. HalluGuard aims to ensure the integrity of chatbot responses by verifying facts and distinguishing between facts and opinions.

## 🚀 Key Features

- **Fact and Opinion Classification**: Uses the TinyLlama-1.1B model to differentiate between facts and opinions in chatbot responses.
- **Fact-Checking**: Verifies the accuracy of facts using the Brave Search API and GPT API as a fallback.
- **User-Friendly Interface**: Built with Streamlit, allowing users to interact with the chatbot and verify facts easily.
- **Database Integration**: Uses PostgreSQL hosted on Supabase to store user data and chat history.

## 🛠️ Technologies Used

- **Frontend**: Streamlit (Python)
- **Backend**: Node.js
- **AI Models**: TinyLlama-1.1B, GPT-3.5 (fallback)
- **Database**: PostgreSQL (Supabase)
- **APIs**: Brave Search API, GPT API

## 📂 Repository Structure
```
/HalluGuard
├── /streamlit_app.py # Frontend code (Streamlit)
├── /.streamlit/ # API Key configuration
├── README.md # This README file
└── requirements.txt # Python dependencies
```

## 📊 Results and Evaluation

### Fact and Opinion Classification
HalluGuard successfully distinguishes between facts and opinions with high accuracy. Below is an example of the classification results:

| No | Text                                                                 | Expected Classification | Actual Classification |
|----|----------------------------------------------------------------------|-------------------------|-----------------------|
| 1  | The Grand Canyon is one of the most stunning natural wonders.        | Fact                    | Fact                  |
| 2  | In my view, visiting the Grand Canyon was an awe-inspiring experience.| Opinion                 | Opinion               |

### Fact-Checking
HalluGuard also successfully verifies the accuracy of facts using the Brave Search API. Below is an example of the fact-checking results:

| No | Sentence                                                                 | Expected | Actual |
|----|--------------------------------------------------------------------------|----------|--------|
| 1  | The Earth orbits the Sun, completing one full orbit every 365.25 days.   | Fact     | Fact   |
| 2  | The Moon is made of green cheese.                                        | Not Fact | Not Fact |

### Response Time
- **Fact and Opinion Classification**: The standard deviation of response time is **120.4326 ms**.
- **Fact-Checking**: The standard deviation of response time is **391.3301 ms**.

- ## 🤝 How to Contribute

We welcome contributions from the community! Here’s how you can contribute:

1. **Fork this repository**.
2. **Create a new branch** for your feature or fix:
   ```bash
   git checkout -b your-branch-name

- ## 🤝 Contact
Muhammad Aidan Daffa Junaidi - muhammad.aidan@ui.ac.id
Muhammad Naufal Faza - muhammad.naufal08@ui.ac.id
Kenya Damayanti Priyama - kenya.damayanti@ui.ac.id
