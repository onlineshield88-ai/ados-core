import sys

from providers.github import Github

url=sys.argv[1]

g=Github()

d=g.repository(url)

print("="*60)

print("Name :",d["full_name"])

print("Language :",d["language"])

print("Stars :",d["stargazers_count"])

print("Forks :",d["forks_count"])

print("License :",d["license"]["spdx_id"] if d["license"] else "None")

print("="*60)
