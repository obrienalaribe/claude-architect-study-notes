# Method

How a question here gets written and checked. Short version: write from public docs, then try hard to break it before anyone else has to.

## 1. Start from a ledger of facts

Before any question exists, I keep a private ledger of single facts, each tied to the public page it came from: the public exam guide and public Anthropic and Claude Code documentation. A question can only test something that has a ledger row. No row, no question.

The ledger itself is not in this repo. It tracks the guide closely, and the guide is Anthropic's.

What never goes in: anything from an exam sitting, anything recalled, anything from a course or practice test behind a login, anything from a question dump.

## 2. One scenario, one keyed answer

Each question is a short scenario with invented details (the company, the numbers, the tool names are all made up), one question, four options. Exactly one option is correct, and the ledger row says why.

## 3. Distractors are wrong for a stated reason

Every wrong option has a written reason it fails, and that reason is published with the question. If I cannot say in one sentence why an option is wrong, it is either right or vague, and it gets rewritten.

## 4. Length and position checks

A correct answer should not be guessable from its shape.

- **Position.** Across the 10: A 2, B 3, C 2, D 3.
- **Length.** The correct option's length rank among the four is tabulated for the set. One rank in more than half the questions fails the set. Current ranks (1 is longest): 1, 2, 2, 2, 3, 2, 2, 4, 1, 3. Rank 2 appears 5 times in 10, which is at the limit and not over it.

## 5. Blind review

A reviewer who has not seen the answer key answers the question from the page alone and explains every option. The question fails if:

- the reviewer picks a different answer and can defend it from the sources,
- two options are defensible,
- the correct option can be guessed from length or wording (the longest, the most hedged, the only detailed one),
- the scenario, numbers or option set echo a sample question from the exam guide.

A failed question is reworded and sent to a fresh reviewer, not back to the same one. An author cannot un-know their own answer, which is why the reviewer has to come in blind.

## 6. Similarity check against the guide's sample questions

The exam guide prints 12 sample questions. They are off limits: not reproduced, not paraphrased, not reused with different numbers.

Two checks keep it that way:

- **By machine.** Each question is compared with the sample question pages for shared runs of consecutive words. A shared run of 8 words or more fails. Today the longest shared run in any question is 5 words, and the longest anywhere in the repo is 6 words, which is the name of the exam in the README.
- **By reviewer.** The blind reviewer names the nearest sample question by topic and says how this one differs in setup, numbers and options.

The same topic can be taught. The framing around it cannot be borrowed.

## 7. Currency check

The guide is a snapshot and the product keeps moving. Each explanation is checked against the current public docs. Where something has changed since the guide was written (a renamed tool, a new stop reason, a newer feature that does the same job), the explanation says so in a sentence starting "Today:".

## Numbers

| What | Value |
|---|---|
| Questions | 10, 2 per exam domain |
| Bank frozen | 2026-10-07, before I registered for or booked any exam |
| Sources | Public exam guide, public Anthropic and Claude Code docs |
| Guide sample questions kept off limits | 12 |
| Shared word run that fails a question | 8 or more |
| Longest shared run with the sample pages, any question | 5 words |
| Longest shared run with the sample pages, whole repo | 6 words (the exam's name) |
| Corrections so far | 0 |

The frozen bank has a SHA-256 hash and a dated tag in my private working repo, so the origin is on record. The JSON here is that bank minus one internal field (a page reference into the guide), so its hash differs.

## After the freeze

New questions are written the same way, from public sources only, and never from memory of an exam. Once I have sat the exam I will not write questions from what I saw there.
