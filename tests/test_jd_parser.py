import unittest

from jd_parser import extract_skills, extract_skills_by_category


class TestJdParser(unittest.TestCase):
    def test_extract_skills_is_case_insensitive(self):
        text = "熟悉 python、LANGCHAIN 和 Git，了解 Prompt Engineering。"

        result = extract_skills(text)

        self.assertIn("Python", result)
        self.assertIn("LangChain", result)
        self.assertIn("Git", result)
        self.assertIn("Prompt Engineering", result)

    def test_extract_skills_by_category_groups_agent_jd_keywords(self):
        text = "要求 Python 编程能力，熟悉 LangChain、Agent、工具调用，了解 Git 和单元测试。"

        result = extract_skills_by_category(text)

        self.assertIn("Python", result["编程语言"])
        self.assertIn("LangChain", result["AI/大模型"])
        self.assertIn("Agent", result["AI/大模型"])
        self.assertIn("工具调用", result["AI/大模型"])
        self.assertIn("Git", result["开发工具"])
        self.assertIn("单元测试", result["测试能力"])

    def test_extract_skills_by_category_returns_empty_lists_when_no_match(self):
        result = extract_skills_by_category("这是一个没有技术关键词的岗位描述。")

        self.assertTrue(all(skills == [] for skills in result.values()))


if __name__ == "__main__":
    unittest.main()
