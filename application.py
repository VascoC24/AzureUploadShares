from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from flask import Flask, render_template, request

app = Flask(__name__)

load_dotenv()

AZURE_CONNECTION_STRING = os.getenv("AZURE_CONNECTION_STRING")
AZURE_CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME")

AZURE_ACCOUNT_NAME = os.getenv("AZURE_ACCOUNT_NAME")
AZURE_KEY = os.getenv("AZURE_KEY")

blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(AZURE_CONTAINER_NAME)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/uploadpage")
def form_page():
    return render_template("uploadpage.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'Nenhum ficheiro enviado', 400

    file = request.files['file']

    if file.filename == '':
        return 'Nome de ficheiro inválido', 400

    blob_client = container_client.get_blob_client(file.filename)
    blob_client.upload_blob(file, overwrite=True)

    sas_token = generate_blob_sas(account_name=AZURE_ACCOUNT_NAME, container_name=AZURE_CONTAINER_NAME, blob_name=file.filename, account_key=AZURE_KEY,
                                  permission=BlobSasPermissions(read=True),
                                  expiry=datetime.utcnow() + timedelta(hours=1))

    download_url = f"https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/{AZURE_CONTAINER_NAME}/{file.filename}?{sas_token}"
    return render_template("result.html", filename=file.filename, download_url=download_url)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
