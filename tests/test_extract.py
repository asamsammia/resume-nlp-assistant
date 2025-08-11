from src.extract import extract_skills

def test_extract_basic():
    text = "Looking for SQL, Python and Power BI developer"
    out = extract_skills(text)
    assert {"SQL","Python","Power BI"}.issubset(set(out))