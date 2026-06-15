"""CLI entry point for MathEdu Toolkit."""

import click
import json
import sys


@click.group()
@click.version_option(version="0.4.2", prog_name="mathedu")
def cli():
    """🧮 MathEdu Toolkit — AI-Powered Elementary Mathematics Education Toolkit."""
    pass


@cli.command()
@click.option("--grade", "-g", default=3, help="Grade level (1-6)")
@click.option("--publisher", "-p", default="qingdao", help="Textbook publisher")
@click.option("--unit", "-u", default=None, help="Unit number (1-7, or 'all')")
@click.option("--count", "-n", default=20, help="Number of problems to generate")
@click.option("--difficulty", "-d", default="mixed", type=click.Choice(["easy", "medium", "hard", "mixed"]))
@click.option("--output", "-o", default="problems.json", help="Output file")
def generate(grade, publisher, unit, count, difficulty, output):
    """Generate math problems."""
    from mathedu.problem_gen import ProblemGenerator
    
    click.echo(f"🧮 Generating {count} problems (Grade {grade}, {publisher} edition)...")
    
    gen = ProblemGenerator(
        grade=grade,
        publisher=publisher,
        unit=int(unit) if unit else None,
    )
    
    problems = gen.generate(count=count, difficulty=difficulty)
    
    data = [p.to_dict() for p in problems]
    with open(output, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    click.echo(f"✅ Generated {len(problems)} problems → {output}")
    
    # Print summary
    units = Counter(p.unit for p in problems)
    for u in sorted(units.keys()):
        click.echo(f"   Unit {u}: {units[u]} problems")


@cli.command("pptx")
@click.option("--grade", "-g", default=3, help="Grade level")
@click.option("--unit", "-u", default="all", help="Unit number or 'all'")
@click.option("--count", "-n", default=49, help="Number of problems")
@click.option("--output", "-o", default=None, help="Output PPTX file path")
def generate_pptx(grade, unit, count, output):
    """Generate review PowerPoint slides."""
    from mathedu.problem_gen import ProblemGenerator
    
    if output is None:
        output = f"三年级下册数学期末复习.pptx"
    
    u = None if unit == "all" else int(unit)
    gen = ProblemGenerator(grade=grade, unit=u)
    problems = gen.generate(count=count)
    
    click.echo(f"📊 Generating PPTX with {len(problems)} problems...")
    gen.export_pptx(problems, output=output)
    click.echo(f"Done! → {output}")


@cli.command("answers")
@click.option("--input", "-i", "input_file", required=True, help="Input JSON file with problems")
@click.option("--output", "-o", default="answers.docx", help="Output DOCX file")
def generate_answers(input_file, output):
    """Generate answer key document."""
    from mathedu.problem_gen import ProblemGenerator, MathProblem
    
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    problems = [
        MathProblem(
            number=d["number"],
            unit=d["unit"],
            knowledge_point=d["knowledge_point"],
            difficulty=d["difficulty"],
            question_text=d["question"],
            answer=d["answer"],
            solution_steps=d.get("steps", []),
            tags=d.get("tags", []),
        )
        for d in data
    ]
    
    gen = ProblemGenerator()
    gen.export_answers(problems, output=output)
    click.echo(f"✅ Answer key → {output}")


@cli.command()
@click.option("--image", "-i", required=True, help="Path to student work image")
@click.option("--answers", "-a", required=True, help="Path to answer key JSON")
@click.option("--output", "-o", default="feedback.docx", help="Output feedback file")
def grade(image, answers, output):
    """Grade handwritten answers from a photo."""
    from mathedu.grader import Grader
    
    with open(answers, "r", encoding="utf-8") as f:
        answer_key = json.load(f)
    
    grader = Grader(model="gpt-4o")
    results = grader.grade_from_image(image, answer_key)
    grader.export_feedback(results, output=output)
    click.echo(f"✅ Grading complete → {output}")


@cli.command()
@click.option("--data", "-d", required=True, help="Grading results JSON")
@click.option("--student-id", "-s", default=None, help="Student ID for individual report")
def analyze(data, student_id):
    """Analyze learning analytics."""
    from mathedu.analytics import Analytics
    
    analytics = Analytics()
    # Load and process data...
    click.echo("📊 Analytics module loaded. Processing...")


if __name__ == "__main__":
    cli()
