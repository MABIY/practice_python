class User:
    """Represent a simple user profile."""
    def __init__(self,first_name,last_name,username,email,location):
        """Initialize the user."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")
    def increment_login_attempts(self):
        """Increment the value of login_attempts"""
        self.login_attempts +=1

    def reset_login_attempts(self):
        """Reset login.attempts to 0."""
        self.login_attempts = 0
eric = User("eric","matthes",'e_matthes','e_mattes@example.com','alaska')
eric.describe_user()
eric.greet_user()

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print(f" Login attempts: {eric.login_attempts}")

print("Resetting login attempts...")
eric.reset_login_attempts()
print(f" Login attempts: {eric.login_attempts}")
