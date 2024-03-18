class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the programming language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the programming language."""
        reflection_str = "Reflection=True" if self.reflection else "Reflection=False"
        return f"{self.name}, {self.typing} Typing, {reflection_str}, First appeared in {self.year}"
