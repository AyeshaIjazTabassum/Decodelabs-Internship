def generate_recommendation(extracted_skills, role_data):

    required = role_data["skills"]

    matched = []

    missing = []

    for skill in required:

        if skill.lower() in [
            s.lower() for s in extracted_skills
        ]:
            matched.append(skill)

        else:
            missing.append(skill)

    score = int(
        (len(matched)/len(required))*100
    )

    roadmap = [
        f"Learn {skill}"
        for skill in missing
    ]

    return {
        "score":score,
        "current_skills":matched,
        "missing_skills":missing,
        "roadmap":roadmap,
        "projects":role_data["projects"],
        "certifications":role_data["certifications"]
    }