import pandas as pd
import json

# 1. Baca CSV
df_csv = pd.read_csv("Mental_Health_FAQ.csv")

# 2. Baca JSON
with open("intents.json", "r") as f:
    data_json = json.load(f)

# 3. Ekstrak intents JSON ke format dataframe
rows = []
for intent in data_json['intents']:
    tag = intent['tag']
    for pattern in intent['patterns']:
        response = intent['responses'][0] if intent['responses'] else ""
        rows.append({
            "Tag": tag,
            "Patterns": pattern,
            "Responses": response
        })

df_json = pd.DataFrame(rows)

# 4. Gabungkan kedua dataframe
combined_df = pd.concat([df_csv, df_json], ignore_index=True)

# 5. Simpan ke file baru
combined_df.to_csv("combined_chatbot_dataset.csv", index=False)

print("Dataset berhasil digabung dan disimpan sebagai 'combined_chatbot_dataset.csv'")
