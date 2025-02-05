from user import User
from privileges import Privileges

class Admin(User):
    """A user with administrative"""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()

