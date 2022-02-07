from ossapi import OssapiV2
api = OssapiV2("12634", "gF0jEtyf8SYYkIS1wdV1Kj5Ym1MYkoxTJarQKtRS", "http://178.40.240.46:838")
import requests
import base64
from osrparse import Replay, parse_replay_data

def download_replay(path, beatmapid, userid):
    r = requests.post("https://osu.ppy.sh/api/get_replay", data={"k": "d1c0cf81d9e83ae9e1d08fdccc6a6703d1037858", "u": userid, "b": beatmapid})
    text = r.text
    print(text)
    json = r.json()["content"]
    data = base64.b64decode(json)
    open("pog.txt", "w+").write(r)
    open("data.txt", "w+").write(data)
    replay_data = parse_replay_data(data)
    replay_data.write_path("./osr.osr")
    # replay = parse_replay(data, pure_lzma=True)

def get_replay(userid):
    """This function gets the latest replay.
    
Returns None if no new recent replays are made.
Else it returns the replay."""
    wtp = api.user_scores(userid, "best", limit=30)[-1].pp
    scores = score = api.user_scores(userid, "recent", limit=10)
    rendered = open("replays.txt").read().splitlines()
    for cn in range(0, 60):
        score = scores[cn]
        pp = score.pp
        if pp == None:
            pp = 0
        score_id = score.id
        print(wtp, pp, score.pp, cn, score.id)

        if pp >= wtp and score_id not in rendered:
            download_replay("./replay.osr", score.beatmap.id, userid)
            print("found")
            break


get_replay(11917029)