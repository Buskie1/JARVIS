from characterai import PyCAI

client = PyCAI('aa86ee006fb4d052e1d2a6a9f02fbdb454c8e4a5')
    
char = 'lcEFlUIHUcruERtBVjFHqyTjk7Vti7BWRu3wWljt5qM'

# Save tgt and history_external_id 
# to avoid making a lot of requests
chat = client.chat.get_chat(char)

participants = chat['participants']

# In the list of "participants",
# a character can be at zero or in the first place
if not participants[0]['is_human']:
    tgt = participants[0]['user']['username']
else:
    tgt = participants[1]['user']['username']

while True:
    message = input('You: ')

    data = client.chat.send_message(
        chat['external_id'], tgt, message
    )

    name = data['src_char']['participant']['name']
    text = data['replies'][0]['text']

    print(f"{name}: {text}")

# aa86ee006fb4d052e1d2a6a9f02fbdb454c8e4a5

#lcEFlUIHUcruERtBVjFHqyTjk7Vti7BWRu3wWljt5qM