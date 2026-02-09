"""People data service — abstracts data access behind a service interface."""

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


@dataclass
class Person:
    name: str
    email: str
    age: int
    role: str
    city: str
    department: str

    @staticmethod
    def from_dict(d: dict) -> "Person":
        return Person(
            name=d["name"], email=d["email"], age=int(d.get("age", 0)),
            role=d.get("role", ""), city=d.get("city", ""),
            department=d.get("department", ""),
        )

    def to_dict(self) -> dict:
        return {
            "name": self.name, "email": self.email, "age": self.age,
            "role": self.role, "city": self.city, "department": self.department,
        }


class PeopleService(Protocol):
    """Interface — swap CSV for DB/REST by implementing this."""
    def find_all(self) -> list[Person]: ...
    def count(self) -> int: ...
    def find_page(self, offset: int, limit: int) -> list[Person]: ...


class CsvPeopleService:
    """CSV-backed implementation."""

    def __init__(self, csv_path: Path | None = None):
        self._path = csv_path or Path(__file__).parent / "people.csv"
        self._data: list[Person] | None = None

    def _load(self) -> list[Person]:
        if self._data is None:
            with open(self._path, newline="", encoding="utf-8") as f:
                self._data = [Person.from_dict(row) for row in csv.DictReader(f)]
        return self._data

    def find_all(self) -> list[Person]:
        return self._load()[:]

    def count(self) -> int:
        return len(self._load())

    def find_page(self, offset: int, limit: int) -> list[Person]:
        return self._load()[offset:offset + limit]


# Default singleton
people_service: PeopleService = CsvPeopleService()
