def calculate_final_score(
    resume_json: str,
    jd_json: str,
    skills_evaluation_json: str,
    responsibilities_evaluation_json: str
) -> str:
    """
    Calculates the final ATS score. This version reliably uses the keys enforced in the agent prompts.
    """
    import json

    # Load the JSON strings
    resume = json.loads(resume_json)
    jd = json.loads(jd_json)
    skills_eval = json.loads(skills_evaluation_json)
    resp_eval = json.loads(responsibilities_evaluation_json)

    weights = {
        "skills": 0.35,
        "experience_level": 0.15,
        "responsibilities_and_accomplishments": 0.30,
        "role_type": 0.05,
        "seniority_level": 0.05,
        "education": 0.10,
    }

    sub_scores = {}

    # --- Use the enforced keys from the LLM outputs and normalize ---
    
    # Use "match_percentage" and normalize it
    skills_match_raw = skills_eval.get("match_percentage", 0.0)
    sub_scores["skills"] = skills_match_raw / 100.0 if skills_match_raw > 1.0 else skills_match_raw

    # Use "overall_alignment_score"
    resp_score_raw = resp_eval.get("overall_alignment_score", 0.0)
    sub_scores["responsibilities_and_accomplishments"] = min(resp_score_raw, 1.0)

    # --- Deterministic checks remain the same ---
    try:
        jd_exp_str = jd.get("ExperienceInYears", "0")
        resume_exp_val = float(resume.get("ExperienceInYears", 0))
        required_years = int(jd_exp_str.split('+')[0].split('-')[0])
        sub_scores["experience_level"] = 1.0 if resume_exp_val >= required_years else 0.75
    except (ValueError, IndexError):
        sub_scores["experience_level"] = 1.0 if resume.get("ExperienceInYears", 0) else 0.0

    jd_role = jd.get("RoleType", "").lower()
    resume_role = resume.get("RoleType", "").lower()
    sub_scores["role_type"] = 1.0 if jd_role in resume_role else 0.0

    jd_seniority = jd.get("SeniorityLevel", "").lower()
    resume_seniority = resume.get("SeniorityLevel", "").lower()
    sub_scores["seniority_level"] = 1.0 if jd_seniority in resume_seniority else 0.0
    
    sub_scores["education"] = 1.0 if resume.get("Education") else 0.0

    # --- Final Calculation ---
    final_score = sum(sub_scores.get(key, 0) * weight for key, weight in weights.items())
    final_score_percent = round(final_score * 100, 2)

    report = {
        "final_score": final_score_percent,
        "details": {
            "component_scores_normalized": sub_scores,
            "llm_evaluations": {
                "skills_analysis": skills_eval,
                "responsibilities_analysis": resp_eval
            }
        }
    }
    return json.dumps(report, indent=2)