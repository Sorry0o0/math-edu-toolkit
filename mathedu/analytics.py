"""
Learning Analytics Engine
Track student progress, identify knowledge gaps, and generate recommendations.
"""

import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Optional


@dataclass
class StudentRecord:
    """Individual student performance record."""
    student_id: str
    name: str
    scores: list  # list of GradeResult objects
    weak_units: list = None
    
    def __post_init__(self):
        if self.weak_units is None:
            self.weak_units = self._analyze_weaknesses()
    
    def _analyze_weaknesses(self) -> list:
        """Identify units where this student scores below average."""
        unit_scores = defaultdict(list)
        for s in self.scores:
            # Extract unit from tags or knowledge_point
            unit = getattr(s, 'unit', getattr(s, 'knowledge_point', 'unknown'))
            unit_scores[unit].append(s.score)
        
        weak = []
        for unit, scores in unit_scores.items():
            avg = sum(scores) / len(scores)
            if avg < 6:
                weak.append((unit, avg))
        return sorted(weak, key=lambda x: x[1])


class Analytics:
    """Class-wide and individual learning analytics."""
    
    def __init__(self):
        self._records: dict[str, StudentRecord] = {}
    
    def add_results(self, student_id: str, name: str, results: list):
        """Add grading results for a student."""
        if student_id not in self._records:
            self._records[student_id] = StudentRecord(student_id, name, results)
        else:
            self._records[student_id].scores.extend(results)
    
    def class_report(self, all_results: list) -> "ClassReport":
        """Generate a comprehensive class report."""
        return ClassReport(all_results, self._records)
    
    def knowledge_gaps(self) -> list[tuple]:
        """Find units where the class as a whole struggles."""
        unit_performance = defaultdict(list)
        
        for record in self._records.values():
            for s in record.scores:
                kp = getattr(s, 'knowledge_point', '未知')
                unit_performance[kp].append(s.score)
        
        gaps = []
        for kp, scores in unit_performance.items():
            avg = sum(scores) / len(scores)
            if len(scores) >= 3 and avg < 6.5:
                gaps.append((kp, avg, len(scores)))
        
        return sorted(gaps, key=lambda x: x[1])
    
    def recommend_for_student(self, student_id: str) -> str:
        """Generate personalized practice recommendations."""
        record = self._records.get(student_id)
        if not record:
            return "暂无该学生的学习数据"
        
        lines = [f"📊 {record.name} 的个性化学习建议\n"]
        
        if record.weak_units:
            lines.append("⚠️ 需要加强的知识点：")
            for unit, avg in record.weak_units[:3]:
                lines.append(f"  • {unit}（平均分 {avg:.1f}）")
                lines.append(f"  → 建议多做{unit}相关的练习题")
        
        strong = [s for s in record.scores if s.score >= 9]
        if strong:
            kp_strong = set(getattr(s, 'knowledge_point', '') for s in strong)
            lines.append(f"\n✅ 掌握较好的：{'、'.join(kp_strong)}")
        
        return "\n".join(lines)


class ClassReport:
    """Comprehensive class analytics report."""
    
    def __init__(self, results: list, records: dict):
        self.results = results
        self.records = records
    
    def summary(self) -> str:
        """Print summary statistics."""
        if not self.results:
            return "暂无数据"
        
        total = sum(r.score for r in self.results)
        max_possible = len(self.results) * 10
        avg = total / len(self.results)
        
        above_80 = sum(1 for r in self.results if r.score >= 8)
        below_60 = sum(1 for r in self.results if r.score < 6)
        
        return f"""📊 班级学习报告
━━━━━━━━━━━━━━━━━━
👥 学生人数：{len(self.records)}
📝 总题数：{len(self.results)}
📈 平均分：{avg:.1f}/{max_possible}
✅ 优秀率（≥8分）：{above_80/len(self.results)*100:.1f}%
⚠️ 待提高（<6分）：{below_60/len(self.results)*100:.1f}%
━━━━━━━━━━━━━━━━━━"""
    
    def knowledge_gaps(self) -> str:
        """Return formatted knowledge gap analysis."""
        gaps = self._compute_gaps()
        if not gaps:
            return "🎉 全班各知识点掌握情况良好！"
        
        lines = ["⚠️ 班级薄弱知识点（需重点复习）：\n"]
        for kp, avg, count in gaps[:5]:
            bar = "█" * int(avg) + "░" * (10 - int(avg))
            lines.append(f"  {kp}  {bar}  平均{avg:.1f}分（{count}人次）")
        return "\n".join(lines)
    
    def _compute_gaps(self) -> list:
        """Compute per-knowledge-point averages."""
        kp_scores = defaultdict(list)
        for r in self.results:
            kp = getattr(r, 'knowledge_point', '未知')
            kp_scores[kp].append(r.score)
        
        result = []
        for kp, scores in kp_scores.items():
            if len(scores) >= 2:
                result.append((kp, sum(scores)/len(scores), len(scores)))
        return sorted(result, key=lambda x: x[1])
