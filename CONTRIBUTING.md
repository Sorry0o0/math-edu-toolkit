# Contributing to MathEdu Toolkit

Thank you for considering contributing! This document provides guidelines for contributing to this project.

## How to Contribute

### Reporting Bugs

Please use GitHub Issues with the following template:
- **Problem description** — What happened vs. what you expected
- **Steps to reproduce** — Minimal code/example to reproduce
- **Environment** — Python/Node version, OS, textbook edition
- **Screenshots** — If applicable

### Suggesting Features

Open an Issue with the `feature-request` tag. Include:
- Use case (which grade/subject/unit)
- Proposed API or behavior
- Examples if possible

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes with tests
4. Ensure all tests pass (`pytest` / `npm test`)
5. Commit with conventional commits format
6. Push and open a PR

### Code Style

- **Python:** Follow PEP 8, use type hints, docstrings for public APIs
- **JavaScript/Node:** ESLint config provided, use ES modules
- **Comments:** Chinese + English for education-domain terms

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/math-edu-toolkit.git
cd math-edu-toolkit

# Python venv
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

pip install -r requirements-dev.txt
npm install

# Run tests
pytest
npm test
```

## Community

- Be respectful and constructive
- This project serves K-12 educators — keep content appropriate
- Questions? Open a Discussion or contact the maintainer
