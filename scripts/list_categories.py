"""
List categories from Jekyll posts.
"""
import glob
import os, os.path
import re
from collections import Counter


dirs = ['_drafts', '_posts']

def extract_front_matter(lines):
    if len(lines) == 0 or lines[0] != '---':
        return {}
    start_header = 1
    end_header = 1
    while end_header < len(lines) and lines[end_header] != '---':
        end_header += 1

    return dict(re.split(
            r'\s*:\s*',
            line,
            maxsplit=1,
        ) for line in lines[start_header:end_header])

counter = Counter()

for d in dirs:
    for path in glob.glob(os.path.join(d, '*.md')):
        with open(path) as f:
            lines = f.read().splitlines(keepends=False)
            header_fields = extract_front_matter(lines)
            if 'categories' in header_fields:
                for cat in header_fields['categories'].split():
                    counter[cat] += 1

for k,v in counter.most_common():
    print(k,v)
