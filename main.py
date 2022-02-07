import requests
import json


def api_request(endpoint: str, parameters: dict):
    return requests.get(f'https://osu.ppy.sh/api/{endpoint}', params=parameters).json()


def main():
    #placeholder
    pass


if __name__ == '__main__':
    main()
