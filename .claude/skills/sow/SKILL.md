---
name: sow
description: >-
  Generate a detailed Scope of Work (SOW) for an AI agency project. Use when
  the user wants to create, draft, or write a SOW, scope document, or
  statement of work that defines deliverables, milestones, acceptance
  criteria, and what is in and out of scope. The SOW is the operational
  contract: it controls what gets built, when, and when it counts as done.
  Pairs with the `proposal` and `contract` skills.
---

# Scope of Work (SOW) Generator

You are drafting a **Scope of Work**. Where the proposal sells, the SOW
*defines*. It is the document both sides point to when there is a
disagreement about whether something was promised. Ambiguity here is what
causes scope creep, unpaid work, and disputes. Be precise.

## Workflow

1. **Gather inputs.** Ask for anything missing, batched into one message.
   If a proposal already exists in `output/`, read it first and reuse its
   solution summary, deliverables, and pricing.

   Required:
   - Agency name and client name (must match the contract exactly)
   - Project objective: the one outcome that defines success
   - In-scope deliverables, each described concretely
   - Out-of-scope items (explicitly list what is excluded)
   - Milestones / phases with dates or week offsets
   - Acceptance criteria per deliverable (how the client signs off)
   - Client responsibilities and dependencies (access, data, content,
     approvals, named point of contact)
   - Assumptions the estimate relies on
   - Pricing and payment schedule tied to milestones
   - Number of revision rounds included per deliverable
   - Change-request process and rate for extra work

2. **Read `templates/sow.md`** and fill every section. For each deliverable
   write: what it is, the acceptance criteria, and the revision count. A
   deliverable without acceptance criteria is a future argument.

3. **Be explicit about exclusions.** The "Out of Scope" section protects the
   agency more than any other. If the user is vague, prompt them: hosting?
   ongoing maintenance? content writing? third-party API costs? data
   cleaning? training the client's staff? Push for specifics.

4. **AI-specific scope.** For AI projects, state which models/APIs are used,
   who pays for API/token usage (usually billed to client at cost or
   client-provided keys), expected accuracy targets if any, and that AI
   outputs require client human review. See `reference/ai-agency-clauses.md`.

5. **Write the SOW** to `output/<client-slug>-sow.md`.

6. The SOW is designed to attach to the service agreement as **Annexure A**.
   Tell the user to run `/contract` next if they have not already. Offer PDF
   export via `scripts/export-pdf.sh`.

## Quality bar

- Every deliverable is testable. "Working chatbot" is not testable;
  "Chatbot answers the 20 FAQ questions in the test set correctly" is.
- Dates are dates or explicit week offsets from a defined start date.
- Payment milestones map to deliverable acceptance, not to calendar dates.
- No em dashes. Plain, unambiguous language.

## What a strong SOW must include

Parties, project objective, in-scope deliverables with acceptance criteria,
explicit out-of-scope list, milestones and timeline, client responsibilities
and dependencies, assumptions, payment schedule, revision policy,
change-request process, and a sign-off block. See
`reference/intake-checklist.md` for the full list.
