import requests

def main():
    print("Hello, World!")
    response = requests.get("https://www.example.com")
    print("Response status code:", response.status_code)

if __name__ == "__main__":
    main()
