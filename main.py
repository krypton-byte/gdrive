from __future__ import print_function
import pickle,mimetypes
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
	"""Shows basic usage of the Drive v3 API.
	Prints the names and ids of the first 10 files the user has access to.
	"""
	creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
 			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
			creds = flow.run_local_server()
        # Save the credentials for the next run
		with open('token.pickle', 'wb') as token:
			pickle.dump(creds, token)
	service = build('drive', 'v3', credentials=creds)
    #file_metadata = {'name': '111sample.pdf'}
	FileUpload=input('file : ')
	file_metadata = {'name': input('upload as name : '),'parents': ['1-IBGrRYqlouIVOmteS0Gzv0_IX5VH91J']}
	media = MediaFileUpload(os.path.abspath(FileUpload), mimetype=mimetypes.guess_type(FileUpload)[0])
	file = service.files().create(body=file_metadata,media_body=media,fields='id').execute()

if __name__ == '__main__':
    main()
