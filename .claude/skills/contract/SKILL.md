---
name: contract
description: >-
  Generate legal agreements for an AI agency operating in India: a Service
  Agreement / Master Services Agreement (MSA) and a Non-Disclosure Agreement
  (NDA). Use when the user wants to create, draft, or write a contract, legal
  document, client agreement, service agreement, MSA, or NDA. Produces
  India-jurisdiction documents with AI-specific clauses. Pairs with the `sow`
  and `proposal` skills.
---

# Contract / Legal Document Generator

You draft **legal agreements** for an India-based AI agency. These documents
are binding. Precision and completeness matter more than persuasion.

> **Not legal advice.** These are well-structured templates, not a substitute
> for a lawyer. Always tell the user, in the final output, to have a qualified
> Indian advocate review the document before signing, especially for
> high-value deals. State this clearly every time.

## Which document?

- **Service Agreement / MSA** — the umbrella contract for a client
  relationship. The SOW attaches as Annexure A. Use `templates/service-agreement.md`.
- **NDA** — standalone, signed *before* sharing proposals or client data.
  Use `templates/nda.md`. Default to a mutual NDA.

Ask the user which they need, or generate both if starting a fresh client
relationship.

## Workflow

1. **Gather inputs**, batched into one message:
   - Agency legal name, type (sole proprietorship / LLP / Pvt Ltd),
     registered address, PAN, authorised signatory
   - Client legal name, type, registered address, authorised signatory
   - Effective date
   - Governing city + state for jurisdiction (e.g. "courts at Bengaluru,
     Karnataka")
   - Whether a SOW exists to attach (check `output/` for `*-sow.md`)
   - Payment terms: advance %, milestone split, invoice due days, late
     interest %
   - Termination notice period (default: 15 days for convenience)
   - Liability cap (default: total fees paid under the relevant SOW)
   - For NDA: mutual or one-way, confidentiality term (default: 3 years)

2. **Read the template AND `reference/clause-library-india.md`.** The clause
   library is the source of truth for India-specific wording: GST (agency is
   currently *unregistered* — fees exclusive of tax, GST added only if/when
   the agency registers), TDS deduction, Indian Contract Act 1872 governing
   law, Arbitration and Conciliation Act 1996, DPDP Act 2023 data protection,
   and IP assignment on full payment.

3. **Always include the AI-specific clauses** from
   `reference/ai-agency-clauses.md`: third-party LLM sub-processors, no
   warranty on AI output accuracy, client human-review obligation, training-
   data handling, and ownership of prompts vs. deliverables vs. pre-existing
   agency IP. These are what a generic contract template misses and what an
   AI agency most needs.

4. **Fill every placeholder you can** from the inputs. Leave genuine unknowns
   as `[BRACKETED PLACEHOLDERS]` and list them at the end so the user knows
   what to complete.

5. **Write** to `output/<client-slug>-service-agreement.md` and/or
   `output/<client-slug>-nda.md`.

6. Append the "Have a lawyer review this" disclaimer and the list of
   remaining placeholders. Offer PDF export via `scripts/export-pdf.sh`.

## Quality bar

- Defined terms are capitalised and used consistently.
- Clauses are numbered. Cross-references point to the right number.
- No em dashes. No clause left as a vague intention.
- Parties' legal names are identical across the MSA, SOW, and NDA.

## What a strong service agreement must include

Parties and recitals, definitions, scope (via SOW), term, fees and payment,
taxes (GST + TDS), IP ownership and assignment, confidentiality, data
protection (DPDP), warranties and disclaimers, AI-specific disclaimers,
limitation of liability, indemnity, termination, force majeure, independent-
contractor status, non-solicitation, dispute resolution and governing law,
notices, and boilerplate (entire agreement, amendment, severability,
assignment, counterparts/e-signature). See `reference/intake-checklist.md`.
