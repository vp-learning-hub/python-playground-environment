print("=== Mad Libs Story ===")
print("Answer the questions to create a funny story!\n")

noun1 = input("Enter a noun (person, place, or thing): ")
adjective1 = input("Enter an adjective: ")
verb1 = input("Enter a verb: ")
place = input("Enter a place: ")
adjective2 = input("Enter another adjective: ")

story = f"""
Once upon a time, there was a {adjective1} {noun1} who loved to {verb1}.
One day, they went to {place} and met a {adjective2} dragon!
The dragon said, "Hello, little {noun1}! Let's {verb1} together!"
And they all lived happily ever after.
"""

print("\n" + "="*40)
print(story)
print("="*40)
