import threading
import requests

# Define the URLs of the files to download
urls = [
    "https://example.com/file1.zip",
    "https://example.com/file2.zip",
    "https://example.com/file3.zip",
]

# Function to download a file from a given URL
def download_file(url):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Extract the filename from the URL
            filename = url.split("/")[-1]
            with open(filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download: {url}")
    except Exception as e:
        print(f"Error while downloading {url}: {str(e)}")

# Create a thread for each URL and start downloading
threads = []
for url in urls:
    thread = threading.Thread(target=download_file, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All downloads completed.")
