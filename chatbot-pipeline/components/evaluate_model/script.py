import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str)
parser.add_argument('--data', type=str)
args = parser.parse_args()

clf, vectorizer = joblib.load(args.model)
df = pd.read_csv(args.data)

X_train, X_test, y_train, y_test = train_test_split(df['Questions'], df['Answers'], test_size=0.2, random_state=42)
X_vec = vectorizer.transform(X_test)
y_pred = clf.predict(X_vec)

acc = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {acc}")
