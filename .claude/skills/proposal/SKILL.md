---
name: proposal
description: >-
  Generate a client-facing project proposal for an AI agency engagement. Use
  when the user wants to create, draft, or write a proposal, pitch, or quote to
  win a new client or project. Produces a persuasive Markdown proposal covering
  the client's problem, the proposed AI solution, scope summary, deliverables,
  timeline, investment/pricing, and next steps. Pairs with the `sow` and
  `contract` skills.
---

# Proposal Generator

You are drafting a **sales proposal** for an AI agency. A proposal is a
pre-sale document: its job is to make the client confident enough to say yes.
It is persuasive, not legal. The binding detail lives in the SOW and contract.

## Workflow

1. **Gather inputs.** Ask the user for anything missing below. Ask in one
   batched message, not one question at a time. If the user says "use
   placeholders" or "fill what you can", proceed and mark gaps with
   `[BRACKETED PLACEHOLDERS]`.

   Required:
   - Agency name, sender name, contact email/phone, website
   - Client name (company + main contact)
   - The client's problem / why they reached out
   - The proposed solution (what the agency will build — e.g. AI chatbot,
     automation pipeline, RAG system, lead-gen agent)
   - High-level deliverables (3-7 items)
   - Timeline estimate (total weeks + rough phases)
   - Pricing: model (fixed / milestone / retainer / hourly) and amount in INR
   - Proposal validity (default: 21 days)

   Optional but strong: known constraints, success metrics the client cares
   about, relevant past work / case study, tools or models to be used.

2. **Read `templates/proposal.md`** and fill every section. Keep the client's
   problem in *their* words. Lead with outcomes, not features.

3. **Pricing.** If the user is unsure how to price, read
   `reference/pricing-models.md` and recommend a model with a short rationale.
   Always state amounts in INR. Add the line: "Fees are exclusive of
   applicable taxes" (the agency is not GST-registered — see
   `reference/clause-library-india.md`).

4. **Write the proposal** to `output/<client-slug>-proposal.md`.

5. **Offer next steps.** Tell the user they can now run `/sow` to produce the
   detailed Scope of Work and `/contract` for the service agreement. Offer to
   export a PDF with `scripts/export-pdf.sh`.

## Quality bar (humaniser rules)

- No em dashes. Use a comma, period, or rewrite.
- No filler: "we are excited to", "in today's fast-paced world",
  "leverage", "synergy", "cutting-edge", "game-changing".
- No rule-of-three padding. One sharp point beats three vague ones.
- Vary sentence length. Concrete numbers over adjectives.
- Write what the client *gets*, not what the agency *does*.
- Keep it to 2-4 pages. A proposal nobody finishes does not sell.

## What a strong proposal must include

Cover page, the problem (their words), proposed solution, scope summary
(detail goes in the SOW), deliverables, timeline/phases, investment,
why this agency, assumptions, what is NOT included, validity date, and a
single clear call to action. See `reference/intake-checklist.md` for the full
list and the reasoning behind each section.
