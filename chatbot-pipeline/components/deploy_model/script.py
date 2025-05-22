import shutil, argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str)
args = parser.parse_args()

deploy_dir = "/home/jovyan/deployed_model"
os.makedirs(deploy_dir, exist_ok=True)
shutil.copy(args.model, os.path.join(deploy_dir, "chatbot_model.joblib"))
print("Model deployed to /home/jovyan/deployed_model/")
