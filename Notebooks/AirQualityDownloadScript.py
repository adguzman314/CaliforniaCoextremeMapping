import requests

def download_data_from_urls(urls, filenames):
    #Depending on connection, retriving all files for one sensor can take up to 10 minutes
    start_time = time.time()

    counter = 0

    for url in urls:
        response = requests.get(url)
        #Check if the request was successful
        if response.status_code == 200:
            # Save the content of the response to a local CSV file
            with open(filenames[counter], "wb") as f:
                f.write(response.content)
            print("CSV file downloaded successfully")
        else:
            print("Failed to download CSV file. Status code:", response.status_code)
        counter =counter + 1
    counter = 0
    
    # Record the end time
    end_time = time.time()

    
    duration = end_time - start_time
    print("Task took", duration, "seconds")
