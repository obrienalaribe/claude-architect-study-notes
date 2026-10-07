#!/usr/bin/env python3
"""Rebuild questions/q*.md from questions/questions.json. Run: python3 scripts/build.py"""
import json, pathlib

qdir = pathlib.Path(__file__).resolve().parent.parent / "questions"
L = "ABCD"
for q in json.loads((qdir / "questions.json").read_text()):
    n = q["id"][1:]
    a = q["correct"]
    md = [f"# Question {n}", "",
          "Original practice question. Not from any exam.", "",
          "## Scenario", "", q["scenario"], "",
          "## Question", "", q["question"], ""]
    md += [f"- **{L[k]}.** {o}" for k, o in enumerate(q["options"])]
    md += ["", "<details>", "<summary>Answer and reasoning</summary>", "",
           f"**Answer: {L[a]}.** {q['explanation']}", "", "Why the others fail:", ""]
    md += [f"- **{L[k]}.** {w}" for k, w in enumerate(q["whyNot"]) if w]
    md += ["", f"Exam domain: {q['domain'][1:]}, {q['domainName']}. Task statement: {q['task']}.", "",
           "</details>", "",
           f"Think it is wrong? [Report an error](https://github.com/obrienalaribe/claude-architect-study-notes/issues/new?template=report-an-error.yml) and quote `{q['id']}`.", ""]
    (qdir / f"q{int(n):02d}.md").write_text("\n".join(md))
