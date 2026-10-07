# Method

How a question for the Claude Certified Architect, Foundations exam (CCAR-F) gets written and checked here.

## 1. Sources

Questions are written from public documentation: the public exam guide and the public Anthropic and Claude Code docs. The exam's official sample questions are not reproduced. Nothing comes from an exam sitting, a question dump, or a course or practice test behind a login.

## 2. Start from a ledger of facts

I keep a private ledger of single facts, each tied to the public page it came from. A question can only test something that has a ledger row. No row, no question.

## 3. One scenario, one keyed answer

Each question is a short scenario with invented details (the company, the numbers and the tool names are made up), one question and four options. Exactly one option is correct, and the ledger row says why.

## 4. Distractors are wrong for a stated reason

Every wrong option has a written reason it fails, and that reason is published with the question. If I cannot say in one sentence why an option is wrong, it gets rewritten.

## 5. Length and position checks

A correct answer should not be guessable from its shape.

- **Position.** Across the 10: A 2, B 3, C 2, D 3.
- **Length.** The correct option's length rank among the four is tabulated for the set. One rank in more than half the questions fails the set. Current ranks (1 is longest): 1, 2, 2, 2, 3, 2, 2, 4, 1, 3. Rank 2 appears 5 times in 10.

## 6. Blind review

A reviewer who has not seen the answer key answers the question from the page alone and explains every option. The question fails if:

- the reviewer picks a different answer and can defend it from the sources,
- two options are defensible,
- the correct option can be guessed from length or wording (the longest, the most hedged, the only detailed one),
- the scenario, numbers or option set echo one of the guide's sample questions.

A failed question is reworded and sent to a fresh reviewer.

## 7. Similarity check

The exam guide prints 12 sample questions. Two checks keep these questions clear of them:

- **By machine.** Each question is compared with the sample question pages for shared runs of consecutive words. A shared run of 8 words or more fails. The longest shared run in any question is 5 words. The longest anywhere in the repo is 6 words, which is the name of the exam.
- **By reviewer.** The blind reviewer names the nearest sample question by topic and says how this one differs in setup, numbers and options.

## 8. Currency check

The guide is a snapshot and the product keeps moving. Each explanation is checked against the current public docs. Where a tool has been renamed or a feature added since the guide was written, the explanation says so in a sentence.

## Numbers

| What | Value |
|---|---|
| Questions | 10, 2 per exam domain |
| Bank frozen | 2026-10-07 |
| Guide sample questions checked against | 12 |
| Shared word run that fails a question | 8 or more |
| Longest shared run with the sample pages, any question | 5 words |
| Longest shared run with the sample pages, whole repo | 6 words (the exam's name) |

The frozen bank has a SHA-256 hash and a dated tag in my private working repo. The JSON here is that bank minus one internal field (a page reference into the guide), so its hash differs.

Questions added after the freeze go through the same steps.
