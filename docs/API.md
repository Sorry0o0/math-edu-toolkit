# MathEdu Toolkit — Python Core

## Installation

```bash
pip install -r requirements.txt
```

## Requirements

```
openai>=1.12.0
Pillow>=10.0.0
numpy>=1.24.0
pandas>=2.0.0
scikit-learn>=1.3.0
python-docx>=1.1.0
jinja2>=3.1.0
pydantic>=2.4.0
rich>=13.0.0
click>=8.1.0
```

## Module: problem_gen/

Core problem generation engine.

### Usage

```python
from mathedu.problem_gen import ProblemGenerator

gen = ProblemGenerator(
    grade=3,
    publisher="qingdao",     # qingdao / renjiao / beijing / suke
    semester=2,
    unit=1                   # 1-7, or "all"
)

# Generate problems
problems = gen.generate(count=20, difficulty="mixed")

# Export to PPTX (requires Node.js ppt_generator module)
gen.export_pptx(problems, output="review.pptx")

# Export to DOCX (answer key)
gen.export_answers(problems, output="answers.docx")
```

### Supported Problem Types

| Type | Units | Example |
|------|-------|---------|
| multiplication | 1 | 23 × 45 = ? |
| division | 3,5 | 72 ÷ 8 = ? |
| mixed_operation | 4 | 25 + 36 ÷ 6 = ? |
| fraction | 6 | 3/4 + 1/8 = ? |
| perimeter | 2 | Rectangle with sides 5cm and 8cm |
| statistics | 6 | Bar chart reading |
| calendar | 7 | Days between dates |
| angles | 2 | Identify acute/obtuse/right angle |

## Module: grader/

Automated grading pipeline.

```python
from mathedu.grader import Grader

grader = Grader(model="gpt-4o")  # or "local" for offline mode

# Grade from image
results = grader.grade_from_image(
    image_path="student_work.jpg",
    answer_key=answer_key_list,
    config={"language": "zh-CN", "handwriting": True}
)

# Get feedback
for r in results:
    print(f"Q{r.number}: {r.score}/10 — {r.feedback}")
```

## Module: analytics/

Learning analytics and recommendations.

```python
from mathedu.analytics import Analytics

analytics = Analytics()
report = analytics.class_report(grading_results)

print(report.summary())
print(report.knowledge_gaps())       # Weak areas by unit
print(recommendations.for_student("student_001"))
```
