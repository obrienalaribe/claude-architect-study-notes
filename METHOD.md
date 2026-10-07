# Method

How a question for the Claude Certified Architect, Foundations exam (CCAR-F) gets written and checked.

1. **Public sources only.** The public exam guide and the public Anthropic and Claude Code docs. The exam's official sample questions are not reproduced. Nothing comes from an exam sitting, a question dump, or a course or practice test behind a login.
2. **A ledger of facts.** I keep a private ledger of single facts, each tied to its public page. No ledger row, no question.
3. **One scenario, one keyed answer.** A short scenario with invented details (company, numbers, tool names), one question, four options, exactly one correct.
4. **Every wrong option fails for a stated reason,** published with the question. If I can't say why in one sentence, the option gets rewritten.
5. **The answer's shape gives nothing away.** Correct answers by position across the 10: A 2, B 3, C 2, D 3. By length rank among the four options (1 is longest): 1, 2, 2, 2, 3, 2, 2, 4, 1, 3. One rank in more than half the questions fails the set; rank 2 appears 5 times in 10.
6. **Blind review.** A reviewer without the answer key answers from the page alone and explains every option. The question fails if they can defend a different answer from the sources, if two options are defensible, if the answer can be guessed from length or wording, or if it echoes one of the guide's sample questions. A failed question is reworded and goes to a fresh reviewer.
7. **Similarity check.** The guide prints 12 sample questions. Each question here is compared with those pages by machine: a shared run of 8 or more consecutive words fails. The blind reviewer also names the nearest sample by topic and says how this one differs in setup, numbers and options.
8. **Currency check.** The guide is a snapshot and the product keeps moving. Each explanation is checked against the current public docs, and says so where a tool has been renamed or a feature added since.

## Numbers

| What | Value |
|---|---|
| Questions | 10, 2 per exam domain |
| Bank frozen | 2026-10-07 |
| Guide sample questions checked against | 12 |
| Longest shared run with the sample pages, any question | 5 words |
| Longest shared run with the sample pages, whole repo | 6 words (the exam's name) |

The frozen bank has a SHA-256 hash and a dated tag in my private repo. The JSON here is that bank minus one internal field (a page reference into the guide), so its hash differs. Questions added later go through the same steps.
