# Very Simple Agent
import ollama

try:
    response = ollama.generate(
        model="deepseek-r1:latest",
        prompt="What is an AI Transformer?"
    )
    print(response["response"])

except Exception as e:
    print(f"An error occurred: {e}")
    # Optional: Check the ollama.log file for server-side issues