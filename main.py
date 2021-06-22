import praw
import json
from pathlib import Path


def get_client():
    creds = Path(Path(__file__).parent.absolute(), "auth.json")
    with open(creds) as f:
        auth = json.load(f)
    return praw.Reddit(**auth)


if __name__ == "__main__":
    client = get_client()
    print(client.user.me())
