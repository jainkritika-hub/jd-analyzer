from pathlib import Path

from analyzer import analyze_jd

jd_text = Path("jd.txt").read_text(encoding="utf-8")
result = analyze_jd(jd_text)

print("Title:", result.job_title)
print("Company:", result.company)
print("Location:", result.location)
print("Type:", result.employment_type)
print("Min experience (years):", result.min_experience_years)

print("\nRequired skills:")
for skill in result.required_skills:
    print(" -", skill)

print("\nNice to have:")
for skill in result.nice_to_have_skills:
    print(" -", skill)

print("\nResponsibilities:")
for item in result.responsibilities:
    print(" -", item)

print("\nSummary:", result.summary)

Path("result.json").write_text(result.model_dump_json(indent=2), encoding="utf-8")
print("\nSaved to result.json")