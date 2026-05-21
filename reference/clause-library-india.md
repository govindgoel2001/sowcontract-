# India Clause Library

Reference wording for an India-based AI agency. The `contract` skill draws
from this. Plain language, current as of 2026. Not legal advice — have an
advocate review before signing.

---

## GST (agency not yet registered)

You said you do not have GST registration. India requires GST registration
once turnover crosses the threshold (₹20 lakh for services in most states,
₹10 lakh in special-category states) or if you make inter-state taxable
supplies in certain cases. Until then you do not charge GST. Use this clause
so the position is clear and you are protected when you do register:

> All fees are exclusive of Goods and Services Tax and other indirect taxes.
> As at the Effective Date the Service Provider is not registered under GST
> and does not charge GST. If the Service Provider becomes liable to register
> for GST, applicable GST will be charged on invoices issued on or after the
> date of registration, and the Client will pay it in addition to the fees.

Practical notes:
- Track your turnover. Register before you cross the threshold; late
  registration creates back-tax exposure.
- Export of services (overseas clients, paid in foreign currency) can be a
  zero-rated supply once registered — useful, but it still needs registration
  and LUT filing. Mention this to your CA when you onboard international
  clients.
- An "exclusive of taxes" clause means the client owes GST on top later, so
  registering does not force you to absorb the cost.

## TDS (tax deducted at source)

Business clients in India often must deduct TDS on professional/technical
fees (commonly 10% under section 194J, or 2% under 194C for contract work,
depending on the nature of service). This is normal and creditable against
your income tax.

> If the Client is required to deduct tax at source under the Income-tax Act,
> 1961, it may do so and will issue the Service Provider a TDS certificate
> (Form 16A) within the statutory period. The Service Provider's PAN is
> [PAN].

Always give clients your PAN — without it, TDS is deducted at a higher rate.

## Governing law

> This Agreement is governed by the laws of India, including the Indian
> Contract Act, 1872.

## Jurisdiction

Pick the city where you operate. Indian courts enforce an exclusive
jurisdiction clause if the chosen court has a genuine connection to the
contract.

> Subject to the arbitration clause, the courts at [CITY, STATE] have
> exclusive jurisdiction over disputes arising out of this Agreement.

## Dispute resolution (arbitration)

Arbitration is faster than litigation for commercial disputes. Use a sole
arbitrator to keep costs down for small engagements.

> The Parties will first attempt to resolve any dispute by good-faith
> discussion for 15 days. If unresolved, the dispute will be referred to
> arbitration by a sole arbitrator under the Arbitration and Conciliation
> Act, 1996. The seat and venue is [CITY], the language is English, and the
> award is final and binding.

## Payment terms

- **Advance:** 30-50% advance is standard for agencies. State it as
  non-refundable once work begins.
- **Invoice due window:** 7-15 days. Shorter is better for cash flow.
- **Late interest:** 1.5-2% per month is common and enforceable if not
  unconscionable.
- **Suspension right:** the right to pause work on unpaid invoices is your
  main leverage. Keep it.

> Overdue amounts carry interest at 1.5% per month from the due date until
> paid. The Service Provider may suspend the Services on 7 days' written
> notice of non-payment.

## IP assignment on full payment

Under the Copyright Act, 1957, assignment of copyright must be in writing.
Tie the assignment to full payment so unpaid work does not transfer.

> On receipt of full payment for the relevant SOW, the Service Provider
> assigns to the Client all intellectual property rights in the custom
> Deliverables created specifically for the Client under that SOW. Until full
> payment is received, all such rights remain with the Service Provider.

Keep your reusable tools, frameworks, and code components as "Pre-Existing
IP" that you licence rather than assign — see `ai-agency-clauses.md`.

## Data protection (DPDP Act, 2023)

India's Digital Personal Data Protection Act, 2023 governs personal data.
When you handle a client's customer data, you are usually a Data Processor
acting for the client (the Data Fiduciary).

> Where the Service Provider processes personal data on the Client's behalf,
> it acts as a Data Processor and the Client as the Data Fiduciary under the
> Digital Personal Data Protection Act, 2023. The Service Provider processes
> personal data only on the Client's documented instructions and applies
> reasonable security safeguards.

Put the burden of having valid consent on the client — they collected the
data, so they must have the lawful basis for you to process it.

## Limitation of liability

Cap your liability at fees received. Without a cap, a small project can
expose you to an unlimited claim.

> The Service Provider's total aggregate liability under this Agreement and
> any SOW is limited to the total fees paid by the Client under the SOW
> giving rise to the claim. Neither Party is liable for indirect or
> consequential loss.

## Independent contractor status

State plainly that you are not an employee. This avoids the client being
treated as your employer and avoids employee-benefit and PF/ESI arguments.

> The Service Provider is an independent contractor. Nothing in this
> Agreement creates employment, partnership, or agency between the Parties.

## Stamp duty

Service agreements are generally stampable. Stamp duty is a state subject and
the amount is usually small (often a fixed nominal value for an agreement).
For high-value contracts, get the agreement stamped in the relevant state so
it is admissible as evidence. Ask your CA or advocate for the current rate in
your state. E-stamping is available in most states.

## Things to set up as the agency grows

- **Register the business** (sole proprietorship is simplest to start; an LLP
  or Pvt Ltd gives you limited liability and looks more credible to larger
  clients).
- **GST registration** before you cross the turnover threshold.
- **A current bank account** in the business name.
- **Professional indemnity insurance** once deals get large — it backs your
  liability cap.
- **ISO 27001** is not legally required, but enterprise clients increasingly
  ask for it in security questionnaires. Until you have it, a short
  written "information security practices" note often satisfies smaller
  clients. Do not claim certifications you do not hold.
