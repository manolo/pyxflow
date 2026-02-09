"""SamplePerson data service — mirrors Java SamplePersonService."""

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class SamplePerson:
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    date_of_birth: str
    occupation: str
    role: str
    important: bool

    @staticmethod
    def from_dict(d: dict) -> "SamplePerson":
        return SamplePerson(
            id=int(d["id"]),
            first_name=d["first_name"],
            last_name=d["last_name"],
            email=d["email"],
            phone=d["phone"],
            date_of_birth=d.get("date_of_birth", ""),
            occupation=d.get("occupation", ""),
            role=d.get("role", ""),
            important=d.get("important", "false").lower() == "true",
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "dateOfBirth": self.date_of_birth,
            "occupation": self.occupation,
            "role": self.role,
            "important": self.important,
        }


class SamplePersonService:
    """CSV-backed SamplePerson service."""

    def __init__(self, csv_path: Path | None = None):
        self._path = csv_path or Path(__file__).parent / "sample_persons.csv"
        self._data: list[SamplePerson] | None = None
        self._next_id: int = 0

    def _load(self) -> list[SamplePerson]:
        if self._data is None:
            with open(self._path, newline="", encoding="utf-8") as f:
                self._data = [SamplePerson.from_dict(row) for row in csv.DictReader(f)]
            self._next_id = max(p.id for p in self._data) + 1 if self._data else 1
        return self._data

    def find_all(self) -> list[SamplePerson]:
        return self._load()[:]

    def count(self) -> int:
        return len(self._load())

    def list(self, offset: int = 0, limit: int | None = None) -> list[SamplePerson]:
        data = self._load()
        if limit is None:
            return data[offset:]
        return data[offset:offset + limit]

    def get(self, person_id: int) -> Optional[SamplePerson]:
        return next((p for p in self._load() if p.id == person_id), None)

    def save(self, person: SamplePerson) -> SamplePerson:
        data = self._load()
        existing = next((p for p in data if p.id == person.id), None)
        if existing:
            idx = data.index(existing)
            data[idx] = person
        else:
            if person.id == 0:
                person.id = self._next_id
                self._next_id += 1
            data.append(person)
        return person

    def delete(self, person_id: int):
        self._data = [p for p in self._load() if p.id != person_id]


# Default singleton
sample_person_service = SamplePersonService()
