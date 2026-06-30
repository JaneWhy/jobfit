import unittest

from fallback_report import build_fallback_report


class TestFallbackReport(unittest.TestCase):
    def test_build_fallback_report_contains_core_match_result(self):
        match_result = {
            "score": 50.0,
            "matched_skills": ["Python", "Agent"],
            "missing_skills": ["LangChain", "Git"],
            "categories": {
                "编程语言": {
                    "score": 100.0,
                    "matched_skills": ["Python"],
                    "missing_skills": [],
                },
                "AI/大模型": {
                    "score": 50.0,
                    "matched_skills": ["Agent"],
                    "missing_skills": ["LangChain"],
                },
            },
        }

        report = build_fallback_report(match_result)

        self.assertIn("基础分析报告", report)
        self.assertIn("基础匹配度：50.0%", report)
        self.assertIn("已匹配技能：Python, Agent", report)
        self.assertIn("待补强技能：LangChain, Git", report)
        self.assertIn("### 编程语言", report)
        self.assertIn("### AI/大模型", report)


if __name__ == "__main__":
    unittest.main()
