#5.8 Hello Admin
usernames = ['admin', 'peter', 'andrew', 'sam', 'john']

for user in usernames:
  if user == 'admin':
    print(f"Hello {user}!")
  else:
    print(f"Hello {user}.")

#5.9 Works when no users
if not usernames:
  print("Uh oh user list is empty!")

#5.10 Checking usernames
current_users = ['peter', 'andrew']
new_users = ['charlie', 'don', 'Andrew']

lower_users = [user.lower() for user in current_users]
for user in new_users:
  if user.lower() in current_users:
    print(f"Uh oh, username {user} is taken.")
  else:
    print("Username is available.")

#5.11 Ordinal numbers

nums = list(range(1,10))
for val in nums:
  if (val == 1):
    print(f"{val}st")
  elif (val == 2):
    print(f"{val}nd")
  elif (val == 3):
    print(f"{val}rd")
  elif (val > 3):
    print(f"{val}th")
