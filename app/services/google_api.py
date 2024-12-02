from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload 
from google.oauth2 import service_account
from io import FileIO

# Get auth key to connect to the API
creds = service_account.Credentials.from_service_account_file(
    '/home/jpinto/Desktop/stellar-smoke-443112-c6-ce61a9c9cf54.json',
    scopes=['https://www.googleapis.com/auth/drive']
)

drive_service = build('drive', 'v3', credentials=creds)

# File present in the driver, where the websites URL are stored
file_id = '16u_9rr8M1sWjZHaTKZNlKFvyE_LncUW1'
# Path to were the information is going to be downloaded
file_path = '/home/jpinto/Documents/python_workshop/WhatsappBotProj/app/downloads/websites.txt'

# Request the file through the API
request = drive_service.files().get_media(fileId=file_id)

# Open the connection to the file
fh = FileIO(file_path, mode='wb')
# Start the download connection
downloader = MediaIoBaseDownload(fh, request)

done = False

# Download until finished
# Looks like it recieves packages until the ending package is recieved
while not done:
    status, done = downloader.next_chunk()
