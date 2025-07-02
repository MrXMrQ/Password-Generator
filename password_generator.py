import string
import random
from math import floor, ceil
from typing import List, Dict


class PasswordGenerator:
    """Handles password generation logic."""

    SPECIAL_CHARS = [
        "!",
        '"',
        "#",
        "$",
        "%",
        "&",
        "(",
        ")",
        "*",
        "+",
        "-",
        "/",
        ":",
        ";",
        "<",
        "=",
        ">",
        "?",
        "@",
        "[",
        "]",
        "^",
        "~",
    ]

    def __init__(self):
        self.numbers = list(string.digits)
        self.lowercase_letters = list(string.ascii_lowercase)
        self.uppercase_letters = list(string.ascii_uppercase)

    def generate(self, length: int, options: Dict[str, bool]) -> str:
        """Generate a password with specified length and character options."""
        character_groups = self._get_character_groups(options)
        character_counts = self._calculate_character_counts(
            length, len(character_groups)
        )

        password_chars = []
        for group, count in zip(character_groups, character_counts):
            password_chars.extend(random.choices(group, k=count))

        random.shuffle(password_chars)
        return "".join(password_chars)

    def _get_character_groups(self, options: Dict[str, bool]) -> List[List[str]]:
        """Get list of character groups based on selected options."""
        groups = []

        if options["special"]:
            groups.append(self.SPECIAL_CHARS)
        if options["numbers"]:
            groups.append(self.numbers)
        if options["upper"]:
            groups.append(self.uppercase_letters)

        # Always include lowercase letters
        groups.append(self.lowercase_letters)

        return groups

    def _calculate_character_counts(self, length: int, num_groups: int) -> List[int]:
        """Calculate how many characters to use from each group."""
        ideal_count = length / num_groups
        min_count = floor(ideal_count * 0.9)
        max_count = ceil(ideal_count * 1.1)

        counts = [int(ideal_count)] * num_groups
        total = sum(counts)

        # Adjust counts to match exact length
        i = 0
        while total < length:
            if counts[i] < max_count:
                counts[i] += 1
                total += 1
            i = (i + 1) % num_groups

        while total > length:
            if counts[i] > min_count:
                counts[i] -= 1
                total -= 1
            i = (i + 1) % num_groups

        return counts
