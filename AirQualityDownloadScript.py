import requests

def download_data_from_urls(urls, filenames):
    # Record the start time
    start_time = time.time()

    counter = 0

    for url in urls:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the content of the response to a local CSV file
            with open(filenames[counter], "wb") as f:
                f.write(response.content)
            print("CSV file downloaded successfully")
        else:
            print("Failed to download CSV file. Status code:", response.status_code)
        counter = counter + 1
    counter = 0
    
    # Record the end time
    end_time = time.time()

    # Calculate the duration
    duration = end_time - start_time
    print("Task took", duration, "seconds")