from pathlib import Path

_ROOT = Path(__file__).resolve().parents[0]


def execute(filename: str):
    with open(Path(_ROOT, "data", filename), "r") as f:
        pass
    return True


if __name__ == "__main__":
    print(f"Output: {execute('input.txt')}")
