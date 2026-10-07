# Claude architect study notes

My practice questions and study notes for the Claude Certified Architect, Foundations exam (CCAR-F).

I'm OBrien (OB): AI and GTM engineer, consultant and trainer, with 10+ years in DevOps and SRE. [LinkedIn](https://www.linkedin.com/in/obrienalaribe/)

## Why

Most free question sets for the exam give you an answer key and ask you to trust it. I wanted to see why each answer is right and why the other three are wrong, so I wrote my own from the public docs. They're open so you can use them and tell me where I slipped.

## What is here

- [`questions/`](questions/): 10 practice questions, 2 per exam domain. Answer and reasoning are collapsed so you can try first.
- [`questions/questions.json`](questions/questions.json): the same 10, machine readable.
- [`METHOD.md`](METHOD.md): how a question gets written and checked. One sourced fact each, a written reason for every wrong option, a blind review.
- [`CORRECTIONS.md`](CORRECTIONS.md): every fix, dated.
- [`scripts/build.py`](scripts/build.py): rebuilds the Markdown from the JSON.

## Found a mistake?

[Open a "Report an error" issue](https://github.com/obrienalaribe/claude-architect-study-notes/issues/new?template=report-an-error.yml) with the question id (`q1` to `q10`), what looks wrong and a public doc that backs you up. Fixes go in [`CORRECTIONS.md`](CORRECTIONS.md) with the date and who spotted it.

## Architect readiness check

The same 10 questions as a free check, about 6 minutes:
https://architect-readiness-check.pages.dev/?ref=github

It asks for an email, then gives you a score for each exam domain so you can see where to study next.

## Licence

Questions and notes: [CC BY 4.0](LICENSE-CONTENT), credit "OBrien Alaribe" with a link back. Code: [MIT](LICENSE).

<sub>Claude and Anthropic are trademarks of Anthropic.</sub>
