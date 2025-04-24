# cli.py

from generator import generate_readme
from fields import get_fields_for


def main():
    print("README Generator")
    print("===================")

    readme_type = input("What type of README? (project/practice): ").strip().lower()
    tech = input("Which technology? (docker/python): ").strip().lower()

    template_path = f"templates/{readme_type}_{tech}.md.tpl"
    fields = get_fields_for(readme_type, tech)

    print("\nPlease provide the following information:\n")
    answers = {}
    for field in fields:
        if field == "extra_technologies":
            raw = input("Extra technologies (comma-separated, optional): ").strip()
            if raw:
                extras = raw.split(",")
                answers[field] = ''.join([f"\n- {tech.strip()}" for tech in extras])
            else:
                answers[field] = ""
        else:
            answers[field] = input(f"{field.replace('_', ' ').capitalize()}: ").strip()

    generate_readme(template_path, answers)

if __name__ == "__main__":
    main()