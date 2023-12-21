![Build Status](https://github.com/EldarDL/helm-project/actions/workflows/docker-image.yml/badge.svg)

# Rick and Morty Characters Script

This script queries the Rick and Morty API to find characters that meet specific conditions and writes the results to a CSV file.

## Prerequisites

- Python 3.9
- Requests library (`pip install ./scripts/requirements.txt`)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/eldard/helm-project.git
    cd helm-project
    ```

2. Install dependencies:

    ```bash
    pip install -r scripts/requirements.txt
    ```

3. Run the script:

    ```bash
    python script.py
    ```

## Script Details

### `get_characters()`

This function queries the Rick and Morty API to fetch characters based on specified conditions.

### `write_to_csv(characters)`

This function writes the fetched character details to a CSV file named `rick_and_morty_characters.csv`.

## Results

The script generates a CSV file with the following columns:

- Name
- Location
- Image

The file is named `rick_and_morty_characters.csv` and is located in the csv folder.

## Notes

- If there's an error during the API request, the script will print the HTTP status code.

# Rick and Morty App

## Prerequisites

Before getting started, ensure you have the following prerequisites installed:

- Python 3.9
- Flask (You can install dependencies using `pip install -r ./app/requirements.txt`)

## Overview

This application follows a simple workflow:

1. **Continuous Integration (CI) Pipeline:**
   - The CI pipeline is configured to automatically build a Docker image and push it to the GitHub Container Registry (GHCR).
   - This ensures that the latest version of the app is always available for deployment.

2. **Deployment using Helm:**
   - After the Docker image is pushed to GHCR, you can use Helm to deploy the changes to local minikube cluster.