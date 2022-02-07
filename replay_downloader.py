from ossapi import OssapiV2
api = OssapiV2("12634", "gF0jEtyf8SYYkIS1wdV1Kj5Ym1MYkoxTJarQKtRS", "http://178.40.240.46:838")
import requests
import base64
from osrparse import Replay, parse_replay_data

def download_replay(path, beatmapid, userid):
    r = requests.post("https://osu.ppy.sh/api/get_replay", data={"k": "d1c0cf81d9e83ae9e1d08fdccc6a6703d1037858", "u": userid, "b": beatmapid}) # should get LZMA stream
    text = r.text # gets content
    print(text)
    json = r.json()["content"] # gets lzma content
    data = base64.b64decode(json) # decodes into bytes
    open("pog.txt", "w+").write(r) # saving to reduce rate limit
    open("data.txt", "w+").write(data) # saving to reduce rate limit
    replay_data = parse_replay_data(data) # parses data... at least it should
    replay_data.write_path("./osr.osr") # saves data... idk tho cant try
    # replay = parse_replay(data, pure_lzma=True)

def get_replay(userid):
    """This function gets the latest replay.
    
Returns None if no new recent replays are made.
Else it returns the replay."""

    # gets the 30th top play pp
    wtp = api.user_scores(userid, "best", limit=30)[-1].pp
    # gets the last 10 scores
    scores = score = api.user_scores(userid, "recent", limit=10)
    # opens the replays.txt, so we dont process replays that have been already rendered and shit
    rendered = open("replays.txt").read().splitlines()
    for cn in range(0, 60):
        score = scores[cn] # grabs score
        pp = score.pp # gets pp
        if pp == None: # loved maps return None PP, so i change it to 0 if its none to make it work normally
            pp = 0
        score_id = score.id # score id
        print(wtp, pp, score.pp, cn, score.id) # debugging, ignore

        # checks if the score pp if more than 30th top play, and isnt rendered
        if pp >= wtp and score_id not in rendered:
            download_replay("./replay.osr", score.beatmap.id, userid)
            print("found")
            break

# call
get_replay(11917029)