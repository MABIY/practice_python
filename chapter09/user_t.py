from admin import Admin

eric = Admin('eric','matthes','e_matthes','e_mattthes@example.com','alaska')
eric.describe_user()

eric_privileges = [
    'can reset password',
    'can moderate discussions',
    'can suspend accounts',
]
eric.privileges.privileges = eric_privileges

print(f"\nThe admin {eric.username} has these privileges:")
eric.privileges.show_privileges()
