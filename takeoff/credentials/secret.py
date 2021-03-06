from dataclasses import dataclass


@dataclass(frozen=True)
class Secret:
    key: str
    val: str

    @property
    def env_key(self):
        return self.jinja_safe_key.upper()

    @property
    def jinja_safe_key(self):
        return self.key.replace("-", "_")

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        if isinstance(other, Secret):
            return self.key == other.key
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other: "Secret"):
        return NotImplemented

    def __le__(self, other: "Secret"):
        return self.__eq__(other)

    def __gt__(self, other: "Secret"):
        return NotImplemented

    def __ge__(self, other: "Secret"):
        return self.__eq__(other)

    def __repr__(self):
        return "%s: '%s'" % (self.key, "*****")
