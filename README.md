# MathEdu Toolkit 🧮📚

<p align="center">
  <strong>AI-Powered Elementary Mathematics Education Toolkit</strong><br>
  <em>for Chinese K-12 Teachers (Qingdao Press Curriculum)</em>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#modules">Modules</a> •
  <a href="#roadmap">Roadmap</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

---

## ✨ Features

- **🎯 Intelligent Problem Generator** — Auto-generate math problems aligned with Qingdao Press textbook standards (Grades 1-6), with configurable difficulty, knowledge point tagging, and step-by-step solutions.
- **✅ Automated Grading Engine** — Vision-language pipeline for handwritten answer recognition and evaluation using multimodal AI. Supports photo upload with instant feedback.
- **📊 Learning Analytics Dashboard** — Track class-wide and individual student progress, identify knowledge gaps, and generate personalized practice recommendations.
- **📝 PPT/Worksheet Generator** — One-click generate review slides, quizzes, and worksheets in PPTX/DOCX format. (Used by 200+ teachers in production)
- **🔗 Curriculum Knowledge Graph** — Structured taxonomy of all Qingdao Press math units with dependency mapping and prerequisite tracking.

## 📦 Quick Start

### Prerequisites

- Python 3.9+
- Node.js 18+
- (Optional) OpenAI API key for AI-powered features

### Installation

```bash
git clone https://github.com/zhangrui-dev/math-edu-toolkit.git
cd math-edu-toolkit

# Python core modules
pip install -r requirements.txt

# PPT/Worksheet generator (Node.js)
npm install
```

### Usage

```python
from mathedu import ProblemGenerator, Grader, Analytics

# Generate 20 Grade-3 multiplication problems (Qingdao Press Unit 1)
gen = ProblemGenerator(grade=3, publisher="qingdao", unit=1)
problems = gen.generate(count=20, difficulty="mixed")
gen.export_pptx(problems, output="review_day1.pptx")

# Grade handwritten answers from image
grader = Grader(model="gpt-4o")
results = grader.grade_from_image("student_answers.jpg", answer_key=problems)
results.export_feedback("feedback.docx")

# Class analytics
analytics = Analytics()
report = analytics.class_report(results)
print(report.knowledge_gaps())  # Identify weak areas
```

## 🏗️ Modules

| Module | Language | Description | Status |
|--------|----------|-------------|--------|
| `problem_gen/` | Python | Problem generation engine with template system | ✅ Stable |
| `grader/` | Python | Multi-modal grading pipeline | ✅ Stable |
| `analytics/` | Python | Learning analytics & recommendation | 🔄 Beta |
| `ppt_generator/` | Node.js | PPTX/DOCX generation via PptxGenJS | ✅ Stable |
| `knowledge_graph/` | Python | Curriculum taxonomy & dependency graph | 🔄 Beta |
| `curriculum_data/` | JSON | Qingdao Press textbook structured data | ✅ Complete |
| `cli/` | Python | Command-line interface | 🔄 Development |

## 📊 Project Stats

- **Total Downloads (PyPI + npm):** ~1,500/month
- **GitHub Stars:** Growing ⭐
- **Active Educator Users:** 200+ (Chinese K-12 community)
- **Last Release:** v0.4.2 (2026-06-10)
- **License:** MIT

## 🗺️ Roadmap

- [ ] v0.5.0 — GPT-4o integration for natural language math understanding
- [ ] v0.6.0 — Student-facing mobile mini-program (WeChat)
- [ ] v0.7.0 — Collaborative problem bank (community-contributed)
- [ ] v1.0.0 — Full LMS integration (DingTalk / Feishu)

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Areas where we especially need help:
- 🌐 Internationalization (English documentation)
- 🧪 Test coverage expansion
- 📚 More curriculum data (other textbook publishers)
- 🔌 LMS integrations

## 👨‍💻 Author

**Zhang Rui (张睿)** — Elementary mathematics teacher & ed-tech developer.

- 🔭 Currently teaching Grade 3 at a public school in Shandong, China
- 💡 Building open-source tools to democratize AI in education
- 📫 WeChat: 和AI对线中

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [PptxGenJS](https://github.com/gitbrent/PptxGenJS) — PowerPoint generation
- [python-docx](https://github.com/python-openxml/python-docx) — Word document generation
- OpenAI — For making advanced AI accessible to developers
- The Chinese open-source education community for feedback and support

---

<p align="center">
  <sub>If this project helps your teaching, consider giving it a ⭐!</sub><br>
  <sub>Made with ❤️ by teachers, for teachers.</sub>
</p>
