import praw
import json
from pathlib import Path


class SaveReddit:
    def __init__(self) -> None:
        self._client = self.get_client()
        self._saved = None

    def get_client(self):
        creds = Path(Path(__file__).parent.absolute(), "auth.json")
        with open(creds) as f:
            auth = json.load(f)
        return praw.Reddit(**auth)

    def get_saved(self):
        if self._saved is None:
            self._saved = [s for s in self._client.user.me().saved()]
        return self._saved
