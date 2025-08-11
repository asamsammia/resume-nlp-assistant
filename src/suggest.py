import re


def keyword_suggestions(job_desc: str, top_n: int = 20):
    """Very simple frequency-based keyword suggester (demo)."""
    tokens = re.findall(r"[A-Za-z][A-Za-z\-\+\/#0-9\.]{1,}", job_desc)
    freq = {}
    for t in tokens:
        k = t.lower()
        if len(k) <= 2:
            continue
        freq[k] = freq.get(k, 0) + 1
    return sorted(freq, key=freq.get, reverse=True)[:top_n]
