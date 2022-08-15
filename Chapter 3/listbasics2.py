guest_list = ["The National", "The Strokes", "The Antlers"]
print(f"{guest_list[0]} is my favorite band")
print(f"Closely followed by {guest_list[1]} and {guest_list[2]}")

print(f"Sadly {guest_list[1]} cannot make it")
guest_list[1] = "Mac Miller"
print(guest_list)

print("We found a larger group to invite!")
guest_list.insert(0, 'Clairo')
guest_list.insert(2, 'Cavetown')
guest_list.append("Stevie Nicks")
print(guest_list)

print("Actually we can only have two people :(")
print(f"Sorry, {guest_list.pop()}, but you cannot come.")
print(f"Sorry, {guest_list.pop()}, but you cannot come either.")
print(f"Sorry, {guest_list.pop()}, but you cannot come either.")
print(f"Sorry, {guest_list.pop()}, but you cannot come either.")

print(guest_list)

del guest_list[1]
del guest_list[0]
print(guest_list)
