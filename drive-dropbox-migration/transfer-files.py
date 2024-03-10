import dropbox
import os

def upload_files(dropbox_access_token, local_folder_path, dropbox_folder_path):
    dbx = dropbox.Dropbox(dropbox_access_token)

    for root, dirs, files in os.walk(local_folder_path):
        for filename in files:
            local_path = os.path.join(root, filename)
            relative_path = os.path.relpath(local_path, local_folder_path)
            dropbox_path = os.path.join(dropbox_folder_path, relative_path)

            with open(local_path, "rb") as f:
                dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)

dropbox_access_token = 'YOUR_DROPBOX_ACCESS_TOKEN'
local_folder_path = 'path/to/local/folder'
dropbox_folder_path = '/path/in/dropbox'

upload_files(dropbox_access_token, local_folder_path, dropbox_folder_path)