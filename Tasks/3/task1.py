name = "John"
day = "Thursday"
message1 = f"Good day {name}! {day} is a perfect day to learn some python."
print("Method 1 (f-string):")
print(message1)
print()

message2 = "Good day {}! {} is a perfect day to learn some python.".format(name, day)
print("Method 2 (.format()):")
print(message2)
print()

# Method 3: .format() with named placeholders
message3 = "Good day {student_name}! {weekday} is a perfect day to learn some python.".format(student_name=name, weekday=day)
print("Method 3 (.format() with names):")
print(message3)
print()

message4 = "Good day %s! %s is a perfect day to learn some python." % (name, day)
print("Method 4 (% formatting):")
print(message4)
print()

message5 = "Good day " + name + "! " + day + " is a perfect day to learn some python."
print("Bonus (string concatenation):")
print(message5)

message5 = "Good day " + name.upper() + "! " + day + " is a perfect day to learn some python."
print("Bonus (string concatenation):")
print(message5)