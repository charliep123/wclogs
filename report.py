from dataclasses import dataclass

@dataclass
class ReportInfo:
    id: str
    title: str
    owner: str
    start: int
    end: int
    zone: int
