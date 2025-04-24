# generator.py
import os
from string import Template

def generate_readme(template_path, values):
    with open(template_path, "r") as file:
        template = Template(file.read())

    output = template.safe_substitute(values)

    os.makedirs("output", exist_ok=True)
    with open(f"output/README.md", "w") as f:
        f.write(output)

    print("\n README.md has been generated successfully!")
