# Claude architect study notes

My practice questions and study notes for the Claude Certified Architect, Foundations exam (CCAR-F).

I'm O'Brien (OB). AI engineer, GTM engineer, consultant and trainer, with 10+ years in DevOps and SRE. [LinkedIn](https://www.linkedin.com/in/obrienalaribe/)

## Why this exists

Most free question sets for the exam give you an answer key and ask you to trust it. I wanted to see why each answer is right and why the other three are wrong, so I wrote my own from the public docs. They are open here so you can use them and tell me where I slipped.

## What is here

- [`questions/`](questions/): 10 practice questions, 2 per exam domain. The answer and reasoning sit in a collapsed block so you can try first.
- [`questions/questions.json`](questions/questions.json): the same 10, machine readable.
- [`METHOD.md`](METHOD.md): how a question gets written and checked.
- [`CORRECTIONS.md`](CORRECTIONS.md): every fix, dated.
- [`scripts/build.py`](scripts/build.py): rebuilds the Markdown files from the JSON.

## How the questions are made

Each question is written from public documentation and tests one fact I can point to a page for.
Every wrong option has a written reason it fails.
A reviewer with no answer key answers it cold, and if they can defend a different answer the question gets rewritten.
The full process and the numbers are in [`METHOD.md`](METHOD.md).

## Found a mistake?

Good. [Open a "Report an error" issue](https://github.com/obrienalaribe/claude-architect-study-notes/issues/new?template=report-an-error.yml) with the question id (`q1` to `q10`), what looks wrong, and a link to the public doc that backs you up. A blank issue is fine too. Fixes are logged in [`CORRECTIONS.md`](CORRECTIONS.md) with the date and who spotted it.

## Architect readiness check

The same 10 questions as a free timed check:
https://architect-readiness-check.pages.dev/?ref=github

It asks for an email, then gives you a score for each exam domain so you can see where to study next.

## Licence

- Questions and notes: [CC BY 4.0](LICENSE-CONTENT). Use them, adapt them, credit "O'Brien Alaribe" with a link back.
- Code: [MIT](LICENSE).

Copyright 2026 O'Brien Alaribe.

<sub>Claude and Anthropic are trademarks of Anthropic.</sub>
