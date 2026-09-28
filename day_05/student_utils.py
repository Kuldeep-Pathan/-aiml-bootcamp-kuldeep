"""Provide utilities for managing student marks and results."""


class Student:
    """Represent a student and their marks."""

    def __init__(self, name: str, roll_number: int) -> None:
        """Initialize a student.

        Args:
            name: The student's name.
            roll_number: The student's roll number.
        """
        self.name = name
        self.roll_number = roll_number
        self.marks: list[float] = []

    def add_mark(self, mark: float) -> None:
        """Add a mark to the student's marks.

        Args:
            mark: The mark to add.
        """
        self.marks.append(mark)

    def average(self) -> float:
        """Return the student's average mark.

        Returns:
            The average mark, or 0.0 if no marks exist.
        """
        if not self.marks:
            return 0.0

        return sum(self.marks) / len(self.marks)

    def highest_mark(self) -> float | None:
        """Return the student's highest mark.

        Returns:
            The highest mark, or None if no marks exist.
        """
        if not self.marks:
            return None

        return max(self.marks)

    def lowest_mark(self) -> float | None:
        """Return the student's lowest mark.

        Returns:
            The lowest mark, or None if no marks exist.
        """
        if not self.marks:
            return None

        return min(self.marks)

    def __str__(self) -> str:
        """Return a readable description of the student.

        Returns:
            The student's name and roll number.
        """
        return f"Student(name={self.name}, roll_number={self.roll_number})"

    def __repr__(self) -> str:
        """Return a developer-friendly representation of the student.

        Returns:
            A representation containing the student's name and roll number.
        """
        return f"Student(name='{self.name}', roll_number={self.roll_number})"
