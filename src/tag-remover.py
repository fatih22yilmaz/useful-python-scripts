import re


def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def trunc_at(s, d, n=3):
    return d.join(s.split(d, n)[:n])

file_r = open('../resources/modified.txt', 'r')
#
# cleaned = None
# if file_r.mode == 'r':
#     html = file_r.read()
#     cleaned = clean_html(html)
#
# file_w = open('cleaned.txt', 'w+')

file_w = open('../resources/stipped.txt', 'a')
for line in file_r:
    file_w.write(trunc_at(line, '.', 3) + '\n')
