import os

# Specs file read karna
spec_file = "specs/book.spec.md"
if not os.path.exists(spec_file):
    raise Exception(f"{spec_file} not found")

with open(spec_file, "r", encoding="utf-8") as f:
    spec_content = f.read()

# Offline 10-chapter mock book generate
os.makedirs("docs", exist_ok=True)

for i in range(1, 11):
    filename = f"docs/chapter_{i}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Chapter {i}\n\n")
        f.write(f"This is offline generated content for Chapter {i}.\n\n")
        f.write("Sample MCQs:\n1. Question 1?\n2. Question 2?\n\n")
        f.write("Sample Practice Questions:\n1. Practice 1\n2. Practice 2\n")

print("✅ Offline book generated in docs/ folder!")
