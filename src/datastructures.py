"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # Assign an ID if it's not provided
        if "id" not in member:
            member["id"] = self._generate_id()
        # Add last_name if it's not provided
        if "last_name" not in member:
            member["last_name"] = self.last_name
        self._members.append(member)

    def delete_member(self, id):
    # Check if the member exists
        for member in self._members:
            if member["id"] == id:
                return [m for m in self._members if m["id"] != id]
        return False  # Member not found

    def get_member(self, id):
        # Find and return the member with the given id
        for member in self._members:
            if member["id"] == id:
                return member
        return None  # If not found

    def get_all_members(self):
        return self._members