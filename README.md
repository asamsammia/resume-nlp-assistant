# Resume NLP Assistant

Extract skills, quantify impact, and suggest ATS-aligned keywords.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/extract.py --text examples/sample_resume.txt
```
## Modules
- `src/extract.py` – simple skill/entity extraction
- `src/suggest.py` – keyword suggestions from job desc
- `notebooks/eda.ipynb` – experiments
