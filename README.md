# Claude architect study notes

Why this exists: free question sets for this exam are everywhere, and a lot of them are recalled exam content. I did not want to study from those, and I did not want to wonder whether an answer key was right. So I write my own questions from the public docs, get them checked by someone who cannot see the answer, and fix mistakes where everyone can see the fix.

I'm O'Brien (OB). Ten plus years in DevOps and SRE, now an independent AI engineer and consultant. I'm working towards the Claude Certified Architect, Foundations exam (CCAR-F). I have not sat it and I am not certified. These are my study notes, shared as I go.

Independent project. Not affiliated with or endorsed by Anthropic. Claude and Anthropic are trademarks of Anthropic.

## What is here

| Path | What |
|---|---|
| [`questions/`](questions/) | 10 original practice questions, one file each, 2 per exam domain. Answer and reasoning sit in a collapsed block so you can try first. |
| [`questions/questions.json`](questions/questions.json) | The same 10, machine readable. |
| [`METHOD.md`](METHOD.md) | How a question gets written and checked. |
| [`CORRECTIONS.md`](CORRECTIONS.md) | Every fix, dated. Empty so far. |
| [`scripts/build.py`](scripts/build.py) | Rebuilds the Markdown files from the JSON. |

The questions:

| # | Domain | Topic |
|---|---|---|
| [1](questions/q01.md) | 1 Agentic Architecture and Orchestration | When an agent loop should stop |
| [2](questions/q02.md) | 1 Agentic Architecture and Orchestration | What a subagent can see |
| [3](questions/q03.md) | 2 Tool Design and MCP Integration | Empty result versus failed lookup |
| [4](questions/q04.md) | 2 Tool Design and MCP Integration | Sharing an MCP server with a team |
| [5](questions/q05.md) | 3 Claude Code Configuration and Workflows | A noisy skill in the middle of feature work |
| [6](questions/q06.md) | 3 Claude Code Configuration and Workflows | Repeated review comments in CI |
| [7](questions/q07.md) | 4 Prompt Engineering and Structured Output | Invented values in extraction |
| [8](questions/q08.md) | 4 Prompt Engineering and Structured Output | Too many false flags |
| [9](questions/q09.md) | 5 Context Management and Reliability | Exact figures lost in long chats |
| [10](questions/q10.md) | 5 Context Management and Reliability | When to cut human review |

Ten questions tell you where to look next. They do not predict a pass.

## The rules I follow

1. **Public sources only.** The public exam guide and public Anthropic and Claude Code documentation. That is the whole input.
2. **Nothing from an exam.** Nothing from any exam sitting, nothing recalled, nothing from a practice test or course behind a login.
3. **The sample questions in the exam guide are not reproduced here.** Not copied, not paraphrased, not reworked with new numbers. Each of my questions is checked against them so it does not echo one by accident.
4. **Blind review.** Every question is answered by a reviewer who has no answer key. If they pick a different answer and can defend it, the question is wrong, not the reviewer.
5. **Errors get fixed in the open.** A fix goes in [`CORRECTIONS.md`](CORRECTIONS.md) with the date and who spotted it.

If you find recalled exam content anywhere in this repo, tell me and it comes out the same day.

## Found a mistake?

Good. [Open a "Report an error" issue](https://github.com/obrienalaribe/claude-architect-study-notes/issues/new?template=report-an-error.yml). Give the question id (`q1` to `q10`), what looks wrong, and a link to the public doc that backs you up. A blank issue is fine too.

The docs move fast. An answer that was right in October 2026 can go stale, and I would rather hear it from you than from the exam.

Please do not send questions you remember from an exam or a practice test. I will close those without reading the detail.

## Try the timed version

The same 10 questions as a quick check with a score per domain:
https://architect-readiness-check.pages.dev/?ref=github

It asks for an email before the results, then scores you by exam domain so you can see where to study next.

## Study cards

I post study cards and question carousels on LinkedIn as I work through each domain. They live there, not here:
https://www.linkedin.com/in/obrienalaribe/

## Licence

- Questions and notes: [CC BY 4.0](LICENSE-CONTENT). Use them, adapt them, credit "O'Brien Alaribe" with a link back.
- Code: [MIT](LICENSE).

Copyright 2026 O'Brien Alaribe.
