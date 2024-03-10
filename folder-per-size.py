from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import os

SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]

creds = Credentials.from_authorized_user_file("token.json", SCOPES)

# Assuming `creds` is your authenticated credentials object
service = build('drive', 'v3', credentials=creds)


def list_folders_in_root(service):
    """List all folders in the root directory."""
    results = service.files().list(
        q="'root' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false",
        fields='nextPageToken, files(id, name)').execute()
    folders = results.get('files', [])
    return folders

def folders_to_csv(folders):
    """Delete folders.csv if it exists."""
    try:
        os.remove('folders.csv')
    except FileNotFoundError:
        pass

    """Write the folders to a CSV file."""
    with open('folders.csv', 'w') as f:
        f.write('id,name\n')
        for folder in folders:
            f.write(f"{folder['id']},{folder['name']}\n")


def get_folder_size(service, folder_id):
    """Recursively calculate the size of a folder."""
    size = 0
    # Query for files in the current folder
    results = service.files().list(
        q=f"'{folder_id}' in parents and trashed = false",
        fields='nextPageToken, files(id, name, mimeType, size)',
        pageSize=1000).execute()
    files = results.get('files', [])

    for file in files:
        if file['mimeType'] == 'application/vnd.google-apps.folder':
            # Recursively sum up sizes if this is a folder
            size += get_folder_size(service, file['id'])
        else:
            # Add file size (note: size is in bytes)
            size += int(file.get('size', 0))
    return size

def append_size_to_folders_csv(service, folders):
    """Append the size of each folder to the CSV file."""
    with open('folders.csv', 'a') as f:
        f.write('size\n')
        for folder in folders:
            size = get_folder_size(service, folder['id']) / 1024 / 1024 / 1024
            f.write(f"{size}\n")


def main(service):
    folders = list_folders_in_root(service)
    test_folder = [d for d in folders if d.get('id') == '1EHGVxkNxuRGU2X74vZhMI8xFTBwTK-9a']
    folders_to_csv(folders)
    append_size_to_folders_csv(service, test_folder)
    print("Done")


if __name__ == "__main__":
    main(service)