SkillMap = dict[str, list[str]]


def flatten_skills(skills_by_category: SkillMap) -> list[str]:
    skills = []
    for category_skills in skills_by_category.values():
        skills.extend(category_skills)
    return skills


def calculate_match(jd_skills: SkillMap, resume_skills: SkillMap) -> dict:
    category_results = {}
    total_jd_skills = set()
    total_matched_skills = set()
    total_missing_skills = set()

    for category, skills in jd_skills.items():
        jd_set = set(skills)
        resume_set = set(resume_skills.get(category, []))

        matched_skills = sorted(jd_set & resume_set)
        missing_skills = sorted(jd_set - resume_set)
        score = 0 if not jd_set else round(len(matched_skills) / len(jd_set) * 100, 2)

        category_results[category] = {
            "score": score,
            "jd_skills": sorted(jd_set),
            "resume_skills": sorted(resume_set),
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
        }

        total_jd_skills.update(jd_set)
        total_matched_skills.update(matched_skills)
        total_missing_skills.update(missing_skills)

    overall_score = (
        0
        if not total_jd_skills
        else round(len(total_matched_skills) / len(total_jd_skills) * 100, 2)
    )

    return {
        "score": overall_score,
        "matched_skills": sorted(total_matched_skills),
        "missing_skills": sorted(total_missing_skills),
        "categories": category_results,
    }
