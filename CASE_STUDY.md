# Case Study: Where This Tool Comes From

This generator is not a thought experiment. It encodes the method I used to keep multi-entity ERP migrations from breaking at the point most of them break — the moment finance discovers that requirements, controls, and UAT were never specified clearly enough to test against.

## Context

I spent four years as group finance lead for a three-entity group spanning agribusiness, food processing, and an environmental venture, operating in a TZS statutory environment (TRA filings, VAT/EFDMS, payroll statutory deductions, multi-currency exposure). Over that period the group moved off two legacy stacks — a desktop accounting package and a cloud bookkeeping tool — onto a single multi-company ERP.

On paper, migrations like this are a configuration exercise. In practice, the configuration is the easy part. What sinks them is everything that was assumed rather than written down.

## The failure mode

The pattern repeats across finance systems projects, and I watched it play out first-hand:

- Requirements were described as outcomes ("we need accurate stock") rather than as testable behaviour ("the inventory subledger must reconcile to the GL control account at period end, with variances above tolerance owned and aged").
- Controls lived in people's heads. Who approves a supplier master change? What evidence proves a bank reconciliation was reviewed, not just prepared? None of it was documented in a form the implementation team could configure or the auditor could trace.
- UAT was treated as a sign-off formality at the end, not as a set of scenarios written *from the finance risks* at the start. So the system passed UAT and then failed the first real close.

The cost of that gap is concrete. Before the work was structured this way, a core supplier payment cycle ran at 46 days end to end; reconciliations did not tie cleanly month to month; foreign-exchange differences sat unexplained; and VAT control accounts could not be evidenced to the satisfaction of a review.

## What I did

I stopped treating requirements, controls, and UAT as separate documents owned by separate people and started treating them as one traceable chain:

1. **Structured intake** of each finance process — the actual trigger, owner, systems, steps, approvals, handoffs, exceptions, and evidence — rather than a wish-list of features.
2. **Requirements written as testable behaviour**, with scope boundaries made explicit so the implementation team knew what was *out* as clearly as what was in.
3. **A control-risk view** for each process: the risk, the control objective, the control activity, its type and frequency, the owner, and — critically — the evidence required to prove it ran.
4. **UAT scenarios derived from those risks**, so every test traced back to a control and a requirement instead of being invented at the end.
5. **A readiness check** before cutover — data, controls, configuration questions, and open decisions surfaced while there was still time to act on them.

That chain — intake → requirements → controls → UAT → readiness, with traceability running through all of it — is what turned a fragile migration into one that survived contact with a live close.

## How the tool encodes the method

Every part of that method maps onto something the generator produces:

| Method step | Tool output |
|---|---|
| Structured intake | Manual intake, SOP/workflow upload, or guided SOP builder across eight finance processes |
| Testable requirements | Requirements pack with functional/non-functional requirements, data requirements, scope boundaries, and acceptance criteria |
| Control-risk view | Control-risk matrix (CSV/XLSX) with owner, control type, frequency, evidence required, and requirement traceability |
| Risk-derived UAT | UAT test cases tied back to controls and requirements |
| Readiness before cutover | Separate implementation readiness pack covering data, controls, configuration workshop questions, and open decisions |
| Implementation planning | Curated, deliberately cautious target-system fit-gap mapping (candidate notes, not guarantees) |

The tool is deterministic by design. It does not call an external model and invent an answer; it structures finance process knowledge into outputs that finance and systems stakeholders can review, challenge, and validate. That is the same discipline the real work demanded.

## Outcomes

The structured approach is what made the difference between a system that passed sign-off and one that held up in use. On the real engagements behind this method, the most visible result was the core supplier payment cycle moving from 46 days to 2, alongside reconciliations that tied month to month, foreign-exchange differences that could be explained, and statutory control accounts that could be evidenced on demand.

## A note on the data

Everything in this repository uses fictional company names and public-safe sample inputs. No employer, client, supplier, bank, VAT, payroll, HR, customer, or operational data appears anywhere in the code, the examples, or this case study. The figures above are process and performance metrics, deliberately stated without the underlying account balances they relate to.
