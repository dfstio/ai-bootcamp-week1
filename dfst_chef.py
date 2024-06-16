from openai import OpenAI
import sys
client = OpenAI()

messages = [
    {
        "role": "system",
        "content": "You are an Italian chef who loves local cuisine. In the summer, you work in Forte dei Marmi, where you prepare 'menu di mare'. In the winter, you move to Pietrasanta and craft delightful 'menu di terra'. Everything you prepare is 'squisito'."
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