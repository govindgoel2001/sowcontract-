# AI Agency Clauses

Clauses specific to an AI agency. A generic freelance or software contract
misses these, and they are exactly where AI work goes wrong. Always include
the relevant ones in a Service Agreement and reference them in the SOW.

---

## 1. Third-party AI / LLM sub-processors

You depend on providers like Anthropic, OpenAI, and Google. Their uptime,
pricing, and model versions are outside your control. Say so.

> The Services may use third-party AI services, including providers of large
> language models. Their availability, pricing, model versions, and terms are
> outside the Service Provider's control. The Service Provider is not liable
> for changes, deprecations, or outages of third-party AI services.

Also disclose them as sub-processors under the data-protection clause so the
client cannot later claim they did not know their data passed through a third
party.

## 2. No warranty on AI output accuracy

This is the single most important AI clause. LLM output is probabilistic. If
you warrant accuracy, one hallucination becomes your liability.

> AI-generated output is probabilistic and may be inaccurate, incomplete,
> biased, or fabricated ("hallucinated"). The Service Provider does not
> warrant that AI output is accurate, complete, or fit for a particular
> purpose. AI output is not legal, medical, financial, or other professional
> advice.

## 3. Client human-review obligation

Shift the duty to check outputs onto the client. You build the system; they
own the decision to rely on it.

> The Client is responsible for human review and validation of AI output
> before relying on it or deploying it to production, and for ensuring its
> use complies with all laws and regulations applicable to the Client's
> industry.

## 4. Training-data handling

Clients worry their data will train a public model. Address it directly.

> The Service Provider will not knowingly submit the Client's Confidential
> Information or personal data to AI services that use inputs to train
> publicly available models, and will use available provider settings to opt
> out of such training where the Client's data is involved.

In practice: use API tiers / enterprise settings that exclude data from
training, and avoid pasting client data into consumer chat products.

## 5. Ownership: prompts vs. deliverables vs. your IP

Be precise about three different things:

- **Custom Deliverables** (the chatbot, the automation, code written for this
  client): assigned to the client on full payment.
- **Client-specific prompts and configurations** created under the SOW:
  treated as custom Deliverables, assigned to the client.
- **Your Pre-Existing IP** (reusable frameworks, prompt-engineering methods,
  internal tools, code libraries, know-how): stays yours. You licence it to
  the client as part of the Deliverable, you do not assign it.

> Prompts and configurations created specifically for the Client under a SOW
> are custom Deliverables and are assigned under the IP clause. General
> prompting techniques, methods, frameworks, and reusable components remain
> the Service Provider's Pre-Existing IP, licensed to the Client as part of
> the Deliverable on a perpetual, non-exclusive basis.

Without this, you risk handing every reusable asset to one client and being
unable to use it for the next.

## 6. API / token usage costs

Token costs are variable and can be significant. Never absorb them silently.

> Usage costs for third-party AI services (API and token charges) are [billed
> to the Client at cost / paid directly by the Client using Client-provided
> API keys] and are not included in the fees unless the SOW states otherwise.

Client-provided API keys are cleanest: the client owns the billing
relationship and you never carry the cost risk.

## 7. Accuracy targets (only if you agree one)

If a client insists on a performance number, make it a defined, testable
target against a fixed test set, not a blanket promise.

> Where the SOW states an accuracy target, it is measured only against the
> agreed test set defined in the SOW and does not constitute a warranty of
> performance on any other input.

## 8. Acceptable use

Protect yourself from how the client uses what you built.

> The Client will not use the Deliverables or AI services for any unlawful,
> deceptive, harmful, or infringing purpose, or in breach of any third-party
> AI provider's usage policies. The Client indemnifies the Service Provider
> against claims arising from such use.

## 9. Model and dependency changes

AI moves fast. A model you built on may be retired mid-project.

> If a third-party model or service is deprecated or materially changed
> during a project, any work needed to migrate to a replacement is handled as
> a Change Request.

## 10. Bias and fairness disclaimer

> AI systems can reflect biases present in training data or inputs. The
> Service Provider will apply reasonable care, but does not warrant that
> outputs are free of bias. The Client is responsible for fairness review
> appropriate to its use case.

---

## Quick checklist — did the contract cover the AI risks?

- [ ] Third-party providers named and disclosed as sub-processors
- [ ] No warranty on output accuracy
- [ ] Client human-review obligation
- [ ] Training-data opt-out commitment
- [ ] Prompt / deliverable / Pre-Existing IP split is explicit
- [ ] API / token cost responsibility is assigned
- [ ] Acceptable-use restriction with indemnity
- [ ] Model-deprecation handled via Change Request
- [ ] Bias disclaimer present
