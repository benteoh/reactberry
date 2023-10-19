import requests
import zipfile
import os

# URL of the zip file
zip_urls = ['https://zenodo.org/records/1188976/files/Audio_Speech_Actors_01-24.zip?download=1', 
            'https://zenodo.org/records/1188976/files/Audio_Song_Actors_01-24.zip?download=1']

# Directory to save the downloaded and extracted files
output_directory = '.'

# Define the file paths
zip_filename = os.path.join(output_directory, 'data.zip')
extracted_dir = output_directory

# Download the zip file
for i in range(len(zip_urls)):
    response = requests.get(zip_urls[i])

    if response.status_code == 200:
        with open(zip_filename, 'wb') as zip_file:
            zip_file.write(response.content)
        print('Zip file downloaded successfully.')

        # Unzip the file
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(extracted_dir)
        print('Zip file extracted to', extracted_dir)

    else:
        print('Failed to download the zip file.')
        if response.status_code == 429:
            print('Too many requests. Try again in a minute.')

