from dataclasses import dataclass


@dataclass
class PonsRecord:
    source: str
    target: str


if __name__ == "__main__":
    record1 = PonsRecord(source="Kraft")
