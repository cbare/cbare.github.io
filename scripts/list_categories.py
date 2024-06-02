"""
Index Jekyll posts by categories.

This turned out to be quite silly, because of course Jekyll can
do a similar thing.
"""
import datetime as dt
import glob
import os
import pathlib
import re
from collections import Counter, defaultdict


date_formats = [
    '%Y-%m-%d %H:%M:%S %z',
    '%Y-%m-%d %H:%M %z',
    '%Y-%m-%d %H:%M',
    '%Y-%m-%d',
]

def parse_date(date, path=None):
    if date:
        for format in date_formats:
            try:
                return dt.datetime.strptime(date, format).astimezone(dt.timezone.utc)
            except ValueError as e:
                pass
    m = re.match(r'(\d{4}-\d{2}-\d{2})-', os.path.basename(path))
    if m:
        return dt.datetime.strptime(m.group(1), '%Y-%m-%d').astimezone(dt.timezone.utc)
    return None


def extract_front_matter(md, path):
    if not re.match(r'^---+\n', md, flags=re.MULTILINE):
        return {}

    result = re.split(r'^---+\n', md, maxsplit=2, flags=re.MULTILINE)

    if len(result) != 3:
        return {}

    headers = dict(
        re.split(r'\s*:\s*', line, maxsplit=1)
        for line in result[1].splitlines()
        if line
    )

    headers['date'] = parse_date(headers.get('date'), path)
    headers['categories'] = headers['categories'].split() if 'categories' in headers else []
    headers['path'] = path

    return headers


def build_index(dirs):
    index = defaultdict(list)
    for d in dirs:
        for path in glob(os.path.join(d, '*.md')):

            try:
                with open(path, 'rt') as f:
                    md = f.read()

                post = extract_front_matter(md, path)

                for category in post['categories']:
                    index[category].append(post)

            except Exception as e:
                print(f'file {path} failed: {e}')

    return index


def by_date_desc(post):
    return dt.datetime(3000,1,1, tzinfo=dt.timezone.utc) - post['date']

def lowercase(txt):
    return txt.lower()


def index_to_markdown(index, out=None):
    print('---', file=out)
    print('layout: page', file=out)
    print('title:  "Lab Notebook Index"', file=out)
    print('---', file=out)
    print('# Lab Notebook Index', file=out)
    for key in sorted(index.keys(), key=lowercase):
        print(f'\n\n## {key.title()}\n', file=out)
        for post in sorted(index[key], key=by_date_desc):
            print(f'- [{post["title"]}]({post["path"]})', file=out)


dirs = [
    #'_drafts',
    '_posts',
]

index = build_index(dirs)
with open('lab-notebook-index.md', 'wt') as f:
    index_to_markdown(index, out=f)
