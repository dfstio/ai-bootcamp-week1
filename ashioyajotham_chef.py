from openai import OpenAI
import sys

client = OpenAI()

messages = [
    {
        "role": "system",
        "content": "You are a passionate African chef who loves to incorporate traditional flavors. You provide recipes and cooking advice with a deep appreciation for African cuisine and culinary traditions."
    }
]

def chat_with_chef(user_input):
    messages.append({"role": "user", "content": user_input})
    
    if "ingredient" in user_input.lower():
        instruction = "Based on the ingredients provided, suggest a dish name."
    elif "recipe" in user_input.lower():
        instruction = "Give a detailed recipe for the mentioned dish."
    elif "criticize" in user_input.lower():
        instruction = "Criticize the provided recipe and suggest changes."
    else:
        return "Please ask for ingredients, a recipe, or a critique."

    messages.append({"role": "system", "content": instruction})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True
    )

    collected_messages = []
    for chunk in response:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    reply = "".join(collected_messages)
    messages.append({"role": "assistant", "content": reply})
    return reply

if __name__ == "__main__":
    user_input = sys.argv[1]
    chat_with_chef(user_input)