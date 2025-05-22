import pandas as pd
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--output_path', type=str, default='/home/jovyan/processed_data.csv')
args = parser.parse_args()

faq = pd.read_csv('/home/jovyan/Mental_Health_FAQ.csv')
with open('/home/jovyan/intents.json') as f:
    intents = json.load(f)

intents_df = pd.DataFrame([
    {
        'Questions': '|'.join(intent['patterns']),
        'Answers': '|'.join(intent['responses'])
    }
    for intent in intents['intents']
])

combined_df = pd.concat([faq, intents_df], ignore_index=True)
combined_df.to_csv(args.output_path, index=False)
