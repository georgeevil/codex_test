from typing import Optional

# Placeholder DB API

class VectorDatabase:
    def __init__(self):
        # Initialize connection to Postgres/pgvector here
        pass

    def search_embedding(self, image_bytes: bytes, label: str) -> Optional[str]:
        """Search for a matching embedding and return its record id if found."""
        return None

    def save_record(self, image_bytes: bytes, label: str, identity: Optional[str]):
        """Save embedding to the database and tie it to a record."""
        record = {
            "label": label,
            "id": identity or "new_hash",
        }
        return record

# Singleton DB connection

db = VectorDatabase()
