import requests

async def download_beatmap(beatmapset_id, path):
    resp = requests.get(f'https://beatconnect.io/b/{beatmapset_id}')
    with open(path, 'wb') as f:
        for buff in resp:
            f.write(buff)