import os
import msal
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_token_header():
    TENANT_ID = os.getenv("TENANT_ID")
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")

    authority = f"https://login.microsoftonline.com/{TENANT_ID}"
    app = msal.ConfidentialClientApplication(CLIENT_ID, authority=authority, client_credential=CLIENT_SECRET)

    result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    access_token = result.get("access_token")

    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}

    return headers