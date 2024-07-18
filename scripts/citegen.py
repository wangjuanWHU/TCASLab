import bibtexparser
import os
import re

CITE_FILE = "./cite.bib"
OUTPUT_FILE = "../publications.md"


pattern = re.compile(
    r"[\u4e00-\u9fff]+.*?and.*?[\u4e00-\u9fff]+|[\u4e00-\u9fff]+.*?and.*?|.*?and.*?[\u4e00-\u9fff]+"
)

with open(CITE_FILE) as bibtex_file:
    out = open(OUTPUT_FILE, "w")

    out.write("---\ntitle: Publication\npermalink: /publication/\n---\n\n")

    out.write("<hr>\n\n")

    content = bibtex_file.read()
    bib_database = bibtexparser.parse_string(content)
    entrys = sorted(
        bib_database.entries, key=lambda x: x.fields_dict["year"].value, reverse=True
    )
    current_year = 0
    for entry in entrys:
        filed = entry.fields_dict
        if entry.fields_dict["year"].value != current_year:
            current_year = entry.fields_dict["year"].value
            out.write(f"### {current_year}\n\n")

        out.write(f"_{filed['title'].value}_<br>\n")

        author_string = pattern.sub(
            lambda x: x.group(0).replace(" and", ","), filed["author"].value
        )
        out.write(f"{author_string}<br>\n")

        # process the name of book or meeting
        if "journal" in filed:
            out.write(f"{filed['journal'].value}, ")
        elif "booktitle" in filed:
            out.write(f"{filed['booktitle'].value}, ")

        out.write(f"{filed['year'].value} ")
        out.write("\n\n")

    out.close()
