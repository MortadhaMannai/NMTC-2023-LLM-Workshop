
import pprint
import google.generativeai as palm

palm.configure(api_key='AIzaSyCmcexKMERb_lxOyl_AK08yJ9M7RBBgyFk')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
# print(model)

def chat_with_palm(prompt):
    response = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800,
    )
    return response.result


print("Welcome to NMTC-2023 Bot! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("NMTC-2023 Bot: Goodbye!")
        break

    response = chat_with_palm(user_input)
    print("NMTC-2023 Bot:", response)
