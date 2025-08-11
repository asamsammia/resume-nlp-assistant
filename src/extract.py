import argparse
import re
import sys


DEFAULT_SKILLS = [
    "SQL",
    "Python",
    "R",
    "Tableau",
    "Power BI",
    "Snowflake",
    "A/B testing",
    "Forecasting",
    "Regression",
    "Classification",
    "Excel",
    "Azure",
    "dbt",
    "ETL",
    "ELT",
]


def extract_skills(text: str, skills=None):
    """Return a sorted list of matched skills found in *text*."""
    skills = skills or DEFAULT_SKILLS
    found = []
    for s in skills:
        if re.search(rf"\b{re.escape(s)}\b", text, flags=re.I):
            found.append(s)
    return sorted(set(found), key=lambda x: x.lower())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", type=str, help="Inline text to scan")
    args = parser.parse_args()
    if args.text:
        print(", ".join(extract_skills(args.text)))
    else:
        print("Provide --text")
        sys.exit(1)
