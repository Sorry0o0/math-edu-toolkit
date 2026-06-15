# Changelog

All notable changes to this project will be documented in this file.

## [0.4.2] — 2026-06-10

### Added
- PPTX generator: support for mixed-difficulty problem sets (easy/medium/hard)
- New curriculum data: Grade 3, Semester 2 (Qingdao Press 2024 edition)
- `ProblemGenerator.export_with_answers()` — generate PPT + answer key in one call
- CLI command: `mathedu pptx --grade 3 --unit all --count 50`

### Fixed
- Fraction rendering in PPTX slides (Unicode fraction display issue)
- Answer key numbering mismatch when problems are shuffled

## [0.4.1] — 2026-05-28

### Added
- Grader module: basic template matching for handwritten digit recognition
- Analytics module: class-level knowledge gap detection (v1)
- Support for Qingdao Press Grade 1-2 curriculum data

### Fixed
- DOCX generation encoding issue for Chinese characters on Windows
- npm install compatibility with Node.js 18.x

## [0.4.0] — 2026-05-15

### Added
- Initial public release
- Problem Generator engine (Grade 3, Qingdao Press)
- PPTX/DOCX export via Node.js (PptxGenJS + python-docx)
- Curriculum knowledge graph (7 units, Grade 3 Sem 2)
- Basic CLI interface
