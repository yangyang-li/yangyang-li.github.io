"""Build the site's initial BibTeX catalogue from the archived WordPress PDFs.

The PDFs remain outside this repository.  This script extracts conservative
metadata and emits a review CSV alongside the bibliography so uncertain
records are visible instead of silently invented.
"""

from __future__ import annotations

import csv
import re
import unicodedata
from pathlib import Path

from pypdf import PdfReader


ARCHIVE = Path(__file__).resolve().parents[2] / "liyangyang.com" / "public_html" / "wp-content" / "uploads"
OUTPUT = Path(__file__).resolve().parents[1] / "_bibliography" / "papers.bib"
REVIEW = Path(__file__).resolve().parents[1] / "_data" / "publication_review.csv"

VENUES = {
    "AAAI": "AAAI Conference on Artificial Intelligence",
    "Access": "IEEE Access",
    "BSCI": "Blockchain: Research and Applications",
    "CAM": "Computers & Mathematics with Applications",
    "CCGrid": "IEEE/ACM International Symposium on Cluster, Cloud and Grid Computing",
    "ChinaCom": "International Conference on Communications and Networking in China",
    "CIKM": "ACM International Conference on Information and Knowledge Management",
    "Cluster": "Cluster Computing",
    "CMC": "Computers, Materials & Continua",
    "CogSci": "Annual Meeting of the Cognitive Science Society",
    "CSSE": "Computer Systems Science & Engineering",
    "DCC": "International Conference on Data Center Networking",
    "DMCIT": "International Conference on Data Mining, Communications and Information Technology",
    "DTPI": "Digital Technology and Policy Innovation",
    "electronics": "Electronics",
    "EMNLP": "Conference on Empirical Methods in Natural Language Processing",
    "Globecom": "IEEE Global Communications Conference",
    "Healthcom": "IEEE International Conference on E-health Networking, Application & Services",
    "HotICN": "IEEE International Conference on Hot Information-Centric Networking",
    "IASC": "International Conference on Intelligent Autonomous Systems",
    "ICAIS": "International Conference on Artificial Intelligence and Security",
    "ICCAI": "International Conference on Computing and Artificial Intelligence",
    "ICCSN": "IEEE International Conference on Computer and Communications",
    "ICCSNT": "International Conference on Communication Systems and Network Technologies",
    "ICDCSW": "IEEE International Conference on Distributed Computing Systems Workshops",
    "ICMLC": "International Conference on Machine Learning and Cybernetics",
    "IJCNN": "International Joint Conference on Neural Networks",
    "IJMLC": "International Journal of Machine Learning and Cybernetics",
    "Inscrypt": "International Conference on Information Security and Cryptology",
    "IOTJ": "IEEE Internet of Things Journal",
    "ISPA": "IEEE International Symposium on Parallel and Distributed Processing with Applications",
    "ISTA": "International Conference on Information Science and Technology Applications",
    "JACEIT": "Journal of Advances in Computer Networks",
    "JBD": "Journal of Big Data",
    "JCAEIT": "Journal of China Academy of Electronics and Information Technology",
    "JCOM": "Journal of Communications",
    "JCUPT": "Journal of China Universities of Posts and Telecommunications",
    "JEIT": "Journal of Electronic & Information Technology",
    "JFLE": "Journal of Forensic and Legal Medicine",
    "JHE": "Journal of Healthcare Engineering",
    "JIN": "Journal of Internet Technology",
    "JIT": "Journal of Information Technology",
    "JMLC": "International Journal of Machine Learning and Cybernetics",
    "JournalXJTU": "Journal of Xi'an Jiaotong University",
    "JXJU": "Journal of Xinjiang University",
    "KAIS": "Knowledge and Information Systems",
    "MCOM": "IEEE Communications Magazine",
    "MIS": "Mobile Information Systems",
    "MM": "ACM Multimedia",
    "MMAsia": "ACM Multimedia Asia",
    "MTA": "Multimedia Tools and Applications",
    "NN": "Neural Networks",
    "PDCAT": "International Conference on Parallel and Distributed Computing, Applications and Technologies",
    "SCN": "Security and Communication Networks",
    "SocialCom": "IEEE International Conference on Social Computing and Networking",
    "symmetry": "Symmetry",
    "TALLIP": "ACM Transactions on Asian and Low-Resource Language Information Processing",
    "TCSS": "IEEE Transactions on Computational Social Systems",
    "TIP": "IEEE Transactions on Image Processing",
    "TJEECS": "Turkish Journal of Electrical Engineering & Computer Sciences",
    "TKDE": "IEEE Transactions on Knowledge and Data Engineering",
    "TURC": "ACM Turing Celebration Conference",
    "TWEB": "ACM Transactions on the Web",
    "WCMC": "Wireless Communications and Mobile Computing",
    "WirelessNetwork": "Wireless Networks",
    "WWW": "The Web Conference",
    "XJU": "Journal of Xinjiang University",
}

NOISE = re.compile(
    r"^(abstract|article|research article|introduction|keywords?|citation|copyright|received|published|"
    r"ieee transactions|proceedings|vol\.|volume|doi[:\s]|\d+\s+ieee)", re.I
)
AFFILIATION = re.compile(
    r"(university|laboratory|academy|institute|school of|department of|college of|beijing|china|email|@)", re.I
)


def clean(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).replace("\u0000", " ")
    value = re.sub(r"\s+", " ", value).strip(" ,.;")
    return value


def tex(value: str) -> str:
    return value.replace("\\", "").replace("{", "").replace("}", "")


def venue_for(stem: str) -> str:
    prefix = re.split(r"[-_]", stem)[0]
    prefix = re.sub(r"\d+$", "", prefix)
    return VENUES.get(prefix, prefix or "Publication")


def year_for(path: Path) -> int:
    stem = path.stem
    match = re.match(r"[A-Za-z]+(\d{2})(?!\d)", stem)
    if match:
        short = int(match.group(1))
        year = 2000 + short if short < 80 else 1900 + short
        if 2010 <= year <= 2030:
            return year
    return int(path.relative_to(ARCHIVE).parts[0])


def extract(path: Path) -> tuple[str, str, str, str]:
    try:
        reader = PdfReader(str(path))
    except Exception:
        # Keep damaged legacy files represented without pretending metadata is known.
        return path.stem, "Li, Yangyang and others", "", "review"
    try:
        info = reader.metadata or {}
        raw = "\n".join((page.extract_text() or "") for page in reader.pages[:2])
    except Exception:
        return path.stem, "Li, Yangyang and others", "", "review"
    lines = [clean(line) for line in raw.splitlines()]
    lines = [line for line in lines if len(line) > 2 and not NOISE.search(line)]

    meta_title = clean(str(info.get("/Title", "")))
    if meta_title and meta_title.lower() not in {"untitled", "title", "microsoft word"} and len(meta_title) > 12:
        title = meta_title
    else:
        start = 0
        while start < len(lines) and (AFFILIATION.search(lines[start]) or len(lines[start]) < 12):
            start += 1
        title_parts: list[str] = []
        for line in lines[start : start + 4]:
            if AFFILIATION.search(line) or re.search(r"\b(and|,|∗|\*)\b", line) and title_parts:
                break
            title_parts.append(line)
            if len(" ".join(title_parts)) > 45 and not line.endswith(("-", ":")):
                break
        title = clean(" ".join(title_parts)) or path.stem

    title_index = next((i for i, line in enumerate(lines) if title[:25].lower() in line.lower()), 0)
    author_parts: list[str] = []
    for line in lines[title_index + 1 : title_index + 7]:
        if AFFILIATION.search(line) or NOISE.search(line):
            break
        if len(line) < 180:
            author_parts.append(line)
    authors = clean(" ".join(author_parts))
    authors = re.sub(r"\b(Senior Member|Member|Fellow)\s*,?\s*IEEE\b", "", authors, flags=re.I)
    authors = re.sub(r"\s*[,;]\s*", " and ", authors)
    authors = re.sub(r"\s+and\s+and\s+", " and ", authors)
    if "Yangyang Li" not in authors or len(authors) > 500:
        authors = "Li, Yangyang and others"

    doi_match = re.search(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", raw, re.I)
    doi = doi_match.group(0).rstrip(".,);]") if doi_match else ""
    confidence = "review" if authors.endswith("others") or title == path.stem else "extracted"
    return tex(title), tex(authors), doi, confidence


def main() -> None:
    pdfs = sorted(ARCHIVE.rglob("*.pdf"))
    # WordPress contains two duplicate IJCNN files; keep one record per exact file hash-sized name.
    seen: set[tuple[str, int]] = set()
    records = []
    for path in pdfs:
        signature = (path.name.lower(), path.stat().st_size)
        if signature in seen:
            continue
        seen.add(signature)
        title, authors, doi, confidence = extract(path)
        year = year_for(path)
        venue = venue_for(path.stem)
        key = re.sub(r"[^a-z0-9]", "", path.stem.lower())[:48]
        records.append((year, key, title, authors, venue, doi, confidence, path.relative_to(ARCHIVE).as_posix()))

    records.sort(key=lambda row: (-row[0], row[2].lower()))
    lines = ["---", "---", "", "% Generated from the archived WordPress publication PDFs.", "% The PDFs themselves are intentionally not included in this repository.", ""]
    review_rows = []
    selected = 0
    for year, key, title, authors, venue, doi, confidence, source in records:
        is_selected = year >= 2024 and selected < 6
        selected += int(is_selected)
        fields = [
            ("title", title),
            ("author", authors),
            ("year", str(year)),
            ("journal", venue),
            ("abbr", re.split(r"[-_]", Path(source).stem)[0]),
            ("selected", "true" if is_selected else "false"),
            ("bibtex_show", "true"),
        ]
        if doi:
            fields.extend((("doi", doi), ("url", f"https://doi.org/{doi}")))
        width = max(len(name) for name, _ in fields)
        lines.append(f"@article{{{key},")
        for index, (name, value) in enumerate(fields):
            comma = "," if index < len(fields) - 1 else ""
            lines.append(f"  {name.ljust(width)} = {{{value}}}{comma}")
        lines.extend(("}", ""))
        review_rows.append((key, confidence, source, title, authors, doi))

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    with REVIEW.open("w", newline="", encoding="utf-8-sig") as stream:
        writer = csv.writer(stream)
        writer.writerow(("bibtex_key", "status", "archive_source", "title", "authors", "doi"))
        writer.writerows(review_rows)
    print(f"Generated {len(records)} publication records; review list: {REVIEW}")


if __name__ == "__main__":
    main()
