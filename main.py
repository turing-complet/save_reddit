import praw
import json
from pathlib import Path
from tqdm import tqdm


class SaveReddit:
    def __init__(self) -> None:
        self._client = None
        self._saved = None

    @property
    def client(self):
        if self._client is None:
            creds = Path(Path(__file__).parent.absolute(), "auth.json")
            with open(creds) as f:
                auth = json.load(f)
            self._client = praw.Reddit(**auth)
        return self._client

    @property
    def saved(self):
        if self._saved is None:
            self._saved = [s for s in self.client.user.me().saved()]
        return self._saved

    def sort_saved(self):
        return sorted(self.saved, key=lambda x: str(type(x)))

    def extract(self, name):
        result = []
        for s in tqdm(self.saved):
            try:
                result.append(getattr(s, name))
            except:
                pass
        return result

    def extract_comments(self):
        return self.extract("body")

    def extract_title(self):
        return self.extract("title")
