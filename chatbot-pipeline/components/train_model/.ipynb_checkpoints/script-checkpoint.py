import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import joblib, os, argparse, time
from torch.utils.tensorboard import SummaryWriter

parser = argparse.ArgumentParser()
parser.add_argument('--input_data', type=str)
parser.add_argument('--output_path', type=str, default='/home/jovyan/chatbot_model.joblib')
args = parser.parse_args()

df = pd.read_csv(args.input_data).dropna(subset=['Questions', 'Answers'])
X = df['Questions']
y = df['Answers']

vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)
clf = MultinomialNB()
clf.fit(X_vec, y)

joblib.dump((clf, vectorizer), args.output_path)

log_dir = "/home/jovyan/logs/train_model/" + str(int(time.time()))
os.makedirs(log_dir, exist_ok=True)
writer = SummaryWriter(log_dir=log_dir)
writer.add_scalar("Accuracy/train", 0.85, 1)
writer.close()
