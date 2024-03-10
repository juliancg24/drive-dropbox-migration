# Google Drive to Dropbox Migration Tool

## Overview
This Python script automates the process of migrating data from Google Drive to Dropbox. It is designed to handle large data volumes efficiently, ensuring that all files are transferred securely and accurately. This tool is particularly useful for users looking to back up or move their data from Google Drive to Dropbox without manual intervention.

## Features
- Lists folders in Google Drive for user selection.
- Transfers a selected folder from Google Drive to Dropbox.
- Verifies that all files have been successfully transferred.

## Prerequisites
Before you begin, ensure you have the following:
- Python 3.6 or higher installed on your system.
- Access to a Google Cloud Platform account with the Drive API enabled.
- A Dropbox account with API access.

## Installation
1. Clone this repository to your local machine.
```bash
git clone https://github.com/juliancg24/drive-dropbox-migration.git
```
2. Navigate to the project directory.
```bash
cd drive-to-dropbox-migration
```
3. Install the required Python dependencies.
```bash
pip install -r requirements.txt
```

## Configuration
1. **Google Drive API**: Follow the [Google Drive API documentation](https://developers.google.com/drive/api/v3/quickstart/python) to create a project, enable the Drive API, and obtain your `credentials.json` file. Place this file in the root directory of the project.
2. **Dropbox API**: Obtain your Dropbox API token by creating an app in the [Dropbox App Console](https://www.dropbox.com/developers/apps). Set your Dropbox API token in a `.env` file or directly in the script as specified.

## Usage
1. Run the migration script.
```bash
python migrate_drive_to_dropbox.py
```

2. Follow the prompts to authenticate with Google Drive and Dropbox if it's your first time running the script.
3. Select the Google Drive folder you wish to transfer when prompted.
4. The script will begin transferring the selected folder to your Dropbox account and will notify you upon completion.

## Verification
The script performs a verification check after the transfer to ensure all files have been successfully migrated to Dropbox. In case of any discrepancies, it will provide a detailed report.

## Contributing
Contributions to this project are welcome! Please fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer
This tool is provided as-is, with no guarantees of functionality or efficiency. Users should use this script at their own risk. Always ensure you have backups of your data before proceeding with the migration.