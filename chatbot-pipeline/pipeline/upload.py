import kfp
from kfp.client import Client

KFP_HOST = "http://ml-pipeline.kubeflow.svc.cluster.local:8888"
PIPELINE_FILE = "/home/jovyan/chatbot-pipeline/pipeline/chatbot_pipeline.yaml"
PIPELINE_NAME = "Chatbot Skripsi Final"

def upload_pipeline():
    client = Client(host=KFP_HOST)
    try:
        pipeline = client.upload_pipeline(PIPELINE_FILE, pipeline_name=PIPELINE_NAME)
        pipeline_id = getattr(pipeline, "pipeline_id", None)
        print("✅ Pipeline berhasil diupload.")
        if pipeline_id:
            print(f"Pipeline ID: {pipeline_id}")
    except Exception as e:
        print(f"❌ Gagal upload pipeline: {e}")

if __name__ == "__main__":
    upload_pipeline()
