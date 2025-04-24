# 📘 README Generator

![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-in--development-yellow)

> A command-line tool to generate professional `README.md` files using modular templates — for practices, projects, and multiple technologies like Docker, Python, Jenkins, and more.

---

## 📚 Table of Contents

- [✨ Features](#features)
- [📁 Available Templates](#available-templates)
- [🚀 Getting Started](#getting-started)
- [🔧 Usage](#usage)
- [🧪 Example CLI Session](#example-cli-session)
- [📦 Project Structure](#project-structure)
- [🛠️ Future Plans](#future-plans)
- [📄 License](#license)

---

## ✨ Features

- 🧪 Supports both **practice** and **project** templates
- 🐳 Docker, 🐍 Python, and more technologies supported
- 📁 Modular structure: easily extend or customize
- 🧩 Dynamic field prompts based on context
- ⚡ Generates professional-looking `README.md` files instantly

---

## 📁 Available Templates

The generator currently supports the following combinations:

| Type     | Technology | Template File                  |
|----------|------------|--------------------------------|
| Project  | Docker     | `templates/project_docker.md.tpl`   |
| Practice | Python     | `templates/practice_python.md.tpl` |

You can easily add more templates by creating new `.tpl` files in the `templates/` folder.  
Just name them following the pattern: `project_<tech>.md.tpl` or `practice_<tech>.md.tpl`.

> 🛠️ Example:
> To add a template for Jenkins projects, create:  
> `templates/project_jenkins.md.tpl`
---


---

## 💻 Requirements

- Python 3.10+
- Git

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/readme-generator.git
cd readme-generator
```

## 🔧 Usage

### 2. Run the CLI script
```bash
python cli.py
```
You will be asked to provide:

### 📁 README Type
- `project`
- `practice`

### 🔧 Technology Used
- `docker`
- `python`
- *(more options coming soon)*

### 📝 Custom Information
- Project title
- Description
- Objective
- Commands used
- Expected result

Once completed, a fully formatted `README.md` file will be generated in your current working directory.
---

## 🧪 Example CLI Session

Below is a sample interaction with the CLI:

```bash
📄 README Generator
===================
What type of README? (project/practice): project
Which technology? (docker/python): docker

📝 Please provide the following information:

Project title: Apache SSL Server  
Description: A Docker-based project to serve HTTPS using Apache and self-signed certificates.  
Objective: Learn how to configure SSL inside a Docker container using Apache.  
Commands used: docker build -t apache_ssl . && docker run -p 443:443 apache_ssl  
Expected result: Access a secure web server via https://localhost  
Dockerfile path: ./Dockerfile
```
---

## 📦 Project Structure

The project is organized in a modular way to keep it clean and extensible:

```bash
readme-generator/
├── cli.py                      # CLI entry point to interact with the user
├── generator.py                # Handles loading templates and rendering the README
├── fields.py                   # Defines the required fields per template type/tech
├── templates/                  # Markdown templates for README generation
│   ├── project_docker.md.tpl
│   └── practice_python.md.tpl
├── examples/                   # (Optional) Example generated READMEs
│   └── sample_project.md
├── README.md                   # Main README file for the generator itself
└── requirements.txt            # Python dependencies

```
---

## 🛠️ Future Plans

Here are some features planned for upcoming versions:

- [ ] Add support for Jenkins, Node.js, and other technologies
- [ ] Implement `typer` for a more robust and user-friendly CLI
- [ ] Use `Jinja2` for more advanced templating
- [ ] Auto-detect GitHub username and repo name from local `.git` config
- [ ] Support multilingual templates (e.g., English / Spanish)
- [ ] Add unit tests and CI/CD pipeline
- [ ] Enable custom template folders via command-line flags
- [ ] Package the project for installation via `pip`

> 🧠 Contributions and suggestions are welcome! Feel free to open an issue or submit a pull request.
---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

You are free to use, modify, and distribute this software with proper attribution.  
See the `LICENSE` file for full license text.
---
