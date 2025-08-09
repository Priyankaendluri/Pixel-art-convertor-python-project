import random

# Sample lines or phrases categorized by type
subjects = ["The moon", "A lonely star", "My heart", "The silent night", "A wandering breeze"]
verbs = ["whispers", "shines", "dances", "sings", "weeps"]
objects = ["in the dark", "through the clouds", "beneath the sky", "in my dreams", "with sorrow"]

def generate_poem(lines=4):
    poem = []
    for _ in range(lines):
        line = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}."
        poem.append(line)
    return "\n".join(poem)

if __name__ == "__main__":
    print("🌸 Your Generated Poem:\n")
    print(generate_poem())

