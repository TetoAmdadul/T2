import requests

try:
    response = requests.get(
        "http://localhost:11434",
        timeout=5
    )

    response.raise_for_status()

except requests.exceptions.ConnectionError:
    print("Could not connect to the server.")

except requests.exceptions.Timeout:
    print("The request timed out.")

except requests.exceptions.HTTPError:
    print("HTTP error occurred.")

except requests.exceptions.RequestException:
    print("A request error occurred.")

else:
    print("Request successful.")
    print(response.status_code)
