class User:
    """Represent a simple user profile."""

    def __init__(self,first_name,last_name,username,email,location):
        """Initialize the user."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"Welcome back, {self.username}")

eric = User('eric','matthes','e_matthes','e_matthes@example.com','alaska')
eric.describe_user()
eric.greet_user()

willie = User('willie','burger','willieburger','web@example.com',location='alaska')
willie.describe_user()
willie.greet_user()