# fields.py

import re
import os


def get_fields_for(readme_type, tech):
    """
    Dynamically extract all variables (${...}) from the corresponding template file.
    """
    template_path = f"templates/{readme_type}_{tech}.md.tpl"

    if not os.path.isfile(template_path):
        raise FileNotFoundError(f"Template not found: {template_path}")

    with open(template_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Find all variables like ${...}
    fields = re.findall(r"\$\{(.*?)\}", content)

    # Remove duplicates while preserving order
    seen = set()
    unique_fields = []
    for field in fields:
        if field not in seen:
            unique_fields.append(field)
            seen.add(field)

    return unique_fields