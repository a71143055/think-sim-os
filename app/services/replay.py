import orjson

def load_snapshot(path: str) -> dict:
    with open(path, "rb") as f:
        return orjson.loads(f.read())

