# Super Simple Agent
import ollama
import time

try:
    # Get model name from user input, default to "gemma3:4b" if empty
    model_name = input("Enter model name (default: gemma3:4b): ") or "gemma3:4b"

    # Get prompt from user input, default to a question about AI Transformers if empty
    prompt = input("Enter your prompt (default: What is an AI Transformer and it ?): ") or "What is an AI Transformer and what is its mechanism?"
    # Start the timer
    start_time = time.time()

    response = ollama.generate(
        model=model_name,
        prompt=prompt
    )

    # End the timer
    end_time = time.time()

    # Calculate execution time
    execution_time = end_time - start_time

    print(response["response"])
    print(f"\nExecution time: {execution_time:.2f} seconds using model {model_name} locally")

except Exception as e:
    print(f"An error occurred: {e}")
    # Optional: Check the ollama.log file for server-side issues
