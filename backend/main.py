from flask import Flask, render_template, request, jsonify
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Initialize the Groq client using the API key from environment
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = 'llama-3.3-70b-versatile'

class Conversation:
    def __init__(self):
        self.messages = [{"role": "system", "content": "You are a code review assistant."}]
        self.active = True

conversations = {}

def get_or_create_conversation(conversation_id):
    if conversation_id not in conversations:
        conversations[conversation_id] = Conversation()
    return conversations[conversation_id]

def query_groq_api(conversation):
    formatted_prompt = f"""
    Review the following code diff and provide feedback in a short and friendly tone. 
    Focus on:
    1. Any bugs or issues that need fixing.
    2. Quick suggestions for improvement or optimization.
    3. Mention changes only if necessary or if there are bugs.

    Keep your response simple, conversational, and to the point. Avoid mentioning your role, just give feedback like a peer would. 
No long explanations, just highlight what's important in a casual manner.



    Code Diff:
    {conversation.messages[-1]['content']}
    """

    try:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "system", "content": formatted_prompt}] + conversation.messages,
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        response = ""
        for chunk in completion:
            response += chunk.choices[0].delta.content or ""

        return response
    except Exception as e:
        raise Exception(f"Error with Groq API: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_diff', methods=['POST'])
def submit_diff():
    user_diff = request.form.get('code_diff')
    conversation_id = "unique_conversation_id"
    conversation = get_or_create_conversation(conversation_id)
    conversation.messages.append({"role": "user", "content": user_diff})

    try:
        response = query_groq_api(conversation)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
