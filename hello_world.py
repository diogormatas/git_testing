import requests
import argparse


def deploy_to_environment(connection_string):
    # Lógica para implantação no ambiente com base na conexão fornecida
    print(f"Deploying to environment with connection string: {connection_string}")
    # Restante da lógica de implantação
    print("Hello, World from development branch -> merged to main!")
    response = requests.get("https://www.example.com")
    print("Response status code:", response.status_code)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--connection-string", required=True, help="Connection string for the environment")
    args = parser.parse_args()

    deploy_to_environment(args.connection_string)

if __name__ == "__main__":
    main()
