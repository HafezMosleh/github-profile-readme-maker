import sys

def generate_readme(name, bio, skills):
    readme = f"# Hi there, I'm {name} 👋\n\n"
    readme += f"### {bio}\n\n"
    readme += f"## 🛠️ Skills\n"
    for skill in skills:
        readme += f"- {skill}\n"
    return readme

if __name__ == '__main__':
    print("Welcome to GitHub Profile README Maker!")
    name = input("Enter your name: ") if sys.stdin.isatty() else "Hafez"
    bio = input("Enter your short bio: ") if sys.stdin.isatty() else "A passionate developer"
    skills = ["Python", "JavaScript", "Docker"]
    out = generate_readme(name, bio, skills)
    with open("PROFILE_README.md", "w") as f:
        f.write(out)
    print("✅ PROFILE_README.md generated successfully!")
