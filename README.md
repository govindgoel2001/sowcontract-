# Doc Maker — Proposals, SOWs & Contracts for an AI Agency

A document toolkit for an India-based AI agency. It generates client-ready
**proposals**, **scopes of work**, and **legal agreements** as Claude Code
Skills, with India-specific and AI-specific clauses built in.

## How it works

Three Claude Code Skills live in `.claude/skills/`. Inside Claude Code, run:

| Command | Produces |
|---------|----------|
| `/proposal` | A persuasive sales proposal to win a project |
| `/sow` | A detailed Scope of Work (deliverables, milestones, acceptance) |
| `/contract` | A Service Agreement (MSA) and/or an NDA |

Each skill interviews you for the details it needs, fills the matching
template, and writes the finished document to `output/`. The skills know
about each other: a proposal flows into a SOW, which attaches to the
contract.

## Repository layout

```
.claude/skills/        The three skills (proposal, sow, contract)
templates/             The document templates that get filled
  proposal.md
  sow.md
  service-agreement.md
  nda.md
reference/             Knowledge the skills draw on
  clause-library-india.md   India clauses: GST, TDS, IP, DPDP, arbitration
  ai-agency-clauses.md      AI-specific clauses a generic contract misses
  pricing-models.md         How to price an engagement
  intake-checklist.md       What to include in each document, and why
scripts/
  export-pdf.sh        Convert any generated Markdown doc to PDF
output/                Generated documents land here
```

## Typical workflow

1. **NDA first** — `/contract`, choose NDA, before sharing anything sensitive.
2. **Win the deal** — `/proposal` to draft the sales proposal.
3. **Define the work** — `/sow` to turn the proposal into a precise scope.
4. **Formalise it** — `/contract` for the Service Agreement; the SOW attaches
   as Annexure A.
5. **Export** — `scripts/export-pdf.sh output/<file>.md` for a signable PDF.

## What to include in each document

See `reference/intake-checklist.md` for the full breakdown of every section
of every document and the reasoning behind it. Short version:

- **Proposal:** the problem, the solution, scope summary, deliverables,
  timeline, investment, why-us, assumptions, exclusions, validity, a CTA.
- **SOW:** objective, deliverables with acceptance criteria, an explicit
  out-of-scope list, milestones, client responsibilities, AI/usage costs,
  revisions policy, change-request process, payment schedule, sign-off.
- **Service Agreement:** parties, definitions, fees, taxes (GST + TDS), IP
  assignment, confidentiality, DPDP data protection, AI-specific disclaimers,
  liability cap, termination, dispute resolution, boilerplate.
- **NDA:** parties, purpose, definition of confidential information,
  obligations, term, remedies, governing law.

## Jurisdiction & tax notes

Documents are written for **India**. The contract clauses assume the agency
is **not yet GST-registered**: fees are stated as exclusive of tax, and GST
is added only once the agency registers. The clause library explains GST
thresholds, TDS, stamp duty, and what to set up as the agency grows. See
`reference/clause-library-india.md`.

## Not legal advice

These templates are a strong, structured starting point, not a substitute
for a lawyer. Have a qualified advocate in India review the Service Agreement
and NDA before signing, especially for high-value or high-risk engagements.

## Sources

The templates and clause structure were informed by well-regarded open-source
contract and SOW projects, including:

- [open-agreements/open-agreements](https://github.com/open-agreements/open-agreements)
- [ankane/awesome-legal](https://github.com/ankane/awesome-legal)
- [jackmorgan/the-plain-contract](https://github.com/jackmorgan/the-plain-contract)
- [SixArm/consulting-agreement](https://github.com/SixArm/consulting-agreement)
- [joelparkerhenderson/statement-of-work](https://github.com/joelparkerhenderson/statement-of-work)
- [accordproject/template-archive](https://github.com/accordproject/template-archive)
- Andy Clarke's "Contract Killer" (open freelance contract)

All clauses here were written fresh for an India-based AI agency; the projects
above informed structure and best practice, not verbatim text.
