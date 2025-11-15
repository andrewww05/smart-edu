from enum import IntEnum

class AccessLevel(IntEnum):
    SUPER_ADMIN = 100
    ADMIN = 80
    MANAGER = 60
    STAFF = 40
    USER = 20
    GUEST = 10 # Unvefified user