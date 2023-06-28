# GitHub Actions - CI/CD Workflow  

name: CI/CD Workflow

on:
  pull_request:
    branches:
      - main

env:
  DEV_CONNECTION_STRING: "string_de_dev"
  UAT_CONNECTION_STRING: "string_de_uat"
  PROD_CONNECTION_STRING: "string_de_prod"

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.x

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest

      - name: Deploy to environment
        run: |
          if [[ ${{ github.event_name }} == 'pull_request' ]]; then
            # Pull request, use DEV_CONNECTION_STRING
            echo "Deploying to dev environment with connection string $DEV_CONNECTION_STRING"
            python hello_world.py --connection-string $DEV_CONNECTION_STRING
          elif [[ ${{ github.ref }} == 'refs/heads/main' ]]; then
            # main branch, use UAT_CONNECTION_STRING
            echo "Deploying to UAT environment with connection string $UAT_CONNECTION_STRING"
            python hello_world.py --connection-string $UAT_CONNECTION_STRING
          else
            # Other branches, use PROD_CONNECTION_STRING
            echo "Deploying to prod environment with connection string $PROD_CONNECTION_STRING"
            python hello_world.py --connection-string $PROD_CONNECTION_STRING
          fi
