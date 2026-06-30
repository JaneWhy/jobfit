import unittest

from matcher import calculate_match, flatten_skills


class TestMatcher(unittest.TestCase):
    def test_flatten_skills_merges_all_categories(self):
        skills = {
            "编程语言": ["Python"],
            "AI/大模型": ["LangChain", "Agent"],
        }

        self.assertEqual(flatten_skills(skills), ["Python", "LangChain", "Agent"])

    def test_calculate_match_returns_overall_and_category_results(self):
        jd_skills = {
            "编程语言": ["Python"],
            "AI/大模型": ["LangChain", "Agent"],
            "开发工具": ["Git"],
        }
        resume_skills = {
            "编程语言": ["Python"],
            "AI/大模型": ["Agent"],
            "开发工具": [],
        }

        result = calculate_match(jd_skills, resume_skills)

        self.assertEqual(result["score"], 50.0)
        self.assertEqual(result["matched_skills"], ["Agent", "Python"])
        self.assertEqual(result["missing_skills"], ["Git", "LangChain"])
        self.assertEqual(result["categories"]["编程语言"]["score"], 100.0)
        self.assertEqual(result["categories"]["AI/大模型"]["score"], 50.0)
        self.assertEqual(result["categories"]["开发工具"]["score"], 0.0)

    def test_calculate_match_handles_empty_jd_skills(self):
        result = calculate_match({"编程语言": []}, {"编程语言": ["Python"]})

        self.assertEqual(result["score"], 0)
        self.assertEqual(result["matched_skills"], [])
        self.assertEqual(result["missing_skills"], [])


if __name__ == "__main__":
    unittest.main()
