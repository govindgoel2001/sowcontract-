#!/usr/bin/env python3
from docx import Document
from docx.shared import Pt, RGBColor, Inches, Twips
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ---- palette ----
ACCENT      = RGBColor(0xB1, 0x63, 0x27)   # copper (deep, legible on white)
ACCENT_HEX  = "B16327"
WASH_HEX    = "FBEEDD"                      # light copper wash for header rows
TINT_HEX    = "FAF6EE"                      # ivory tint
LINE_HEX    = "DDD6C8"                      # hairline borders
INK         = RGBColor(0x22, 0x24, 0x28)
INK_SOFT    = RGBColor(0x55, 0x57, 0x60)
INK_DIM     = RGBColor(0x8A, 0x8D, 0x96)
GOOD        = RGBColor(0x2F, 0x67, 0x43)

HEAD_FONT = "Georgia"
BODY_FONT = "Calibri"

doc = Document()

# ---- base style ----
normal = doc.styles["Normal"]
normal.font.name = BODY_FONT
normal.font.size = Pt(10.5)
normal.font.color.rgb = INK_SOFT
normal.paragraph_format.space_after = Pt(6)
normal.paragraph_format.line_spacing = 1.18

for section in doc.sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.85)
    section.right_margin = Inches(0.85)

# ============ helpers ============
def set_cell_bg(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)

def set_cell_borders(cell, color=LINE_HEX, sz=4, sides=("top","bottom","left","right")):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    for side in sides:
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), str(sz))
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)
        borders.append(el)
    tcPr.append(borders)

def cell_margins(cell, top=70, bottom=70, left=110, right=110):
    tcPr = cell._tc.get_or_add_tcPr()
    m = OxmlElement("w:tcMar")
    for side, val in (("top",top),("bottom",bottom),("start",left),("end",right)):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:w"), str(val))
        el.set(qn("w:type"), "dxa")
        m.append(el)
    tcPr.append(m)

def style_run(run, size=10.5, color=INK_SOFT, bold=False, italic=False, font=BODY_FONT, caps=False):
    run.font.name = font
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    if caps:
        run.font.all_caps = True
    return run

def para(text="", size=10.5, color=INK_SOFT, bold=False, italic=False, font=BODY_FONT,
         space_after=6, space_before=0, align=None, caps=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    if align is not None:
        p.alignment = align
    if text:
        style_run(p.add_run(text), size=size, color=color, bold=bold, italic=italic, font=font, caps=caps)
    return p

def rich(parts, size=10.5, space_after=6, space_before=0, align=None):
    """parts: list of (text, dict-of-overrides)"""
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    if align is not None:
        p.alignment = align
    for text, opts in parts:
        style_run(p.add_run(text), size=opts.get("size", size),
                  color=opts.get("color", INK_SOFT), bold=opts.get("bold", False),
                  italic=opts.get("italic", False), font=opts.get("font", BODY_FONT),
                  caps=opts.get("caps", False))
    return p

def bullet(text_parts):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(3)
    if isinstance(text_parts, str):
        text_parts = [(text_parts, {})]
    for text, opts in text_parts:
        style_run(p.add_run(text), size=opts.get("size",10.5), color=opts.get("color", INK_SOFT),
                  bold=opts.get("bold", False), italic=opts.get("italic", False), font=opts.get("font", BODY_FONT))
    return p

def section_head(number, title, space_before=16):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(4)
    style_run(p.add_run(number + "  "), size=12, color=ACCENT, bold=True, font=HEAD_FONT)
    style_run(p.add_run(title), size=15.5, color=INK, bold=False, font=HEAD_FONT)
    # thin rule under heading
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single"); bottom.set(qn("w:sz"), "4")
    bottom.set(qn("w:space"), "4"); bottom.set(qn("w:color"), LINE_HEX)
    pbdr.append(bottom); pPr.append(pbdr)
    return p

def subhead(text, accent_label=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    if accent_label:
        style_run(p.add_run(accent_label + "   "), size=10, color=ACCENT, bold=True, font=BODY_FONT)
    style_run(p.add_run(text), size=12, color=INK, bold=True, font=HEAD_FONT)
    return p

def accept_line(label, text, label_color=ACCENT):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Inches(0.0)
    style_run(p.add_run(label + " — "), size=9.5, color=label_color, bold=True)
    style_run(p.add_run(text), size=9.5, color=INK_DIM, italic=True)
    return p

def make_table(headers, rows, widths=None, header_fill=ACCENT_HEX, header_color="FFFFFF",
               total_row=False):
    t = doc.add_table(rows=1, cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.allow_autofit = True
    # header
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]
        c.text = ""
        set_cell_bg(c, header_fill)
        set_cell_borders(c)
        cell_margins(c)
        rp = c.paragraphs[0]
        rp.paragraph_format.space_after = Pt(0)
        style_run(rp.add_run(h), size=9, color=RGBColor.from_string(header_color), bold=True, caps=True)
    # body
    for r_idx, row in enumerate(rows):
        cells = t.add_row().cells
        is_total = total_row and r_idx == len(rows) - 1
        for i, val in enumerate(row):
            c = cells[i]
            c.text = ""
            set_cell_borders(c)
            cell_margins(c)
            if is_total:
                set_cell_bg(c, WASH_HEX)
            elif r_idx % 2 == 1:
                set_cell_bg(c, TINT_HEX)
            cp = c.paragraphs[0]
            cp.paragraph_format.space_after = Pt(0)
            if i == len(headers) - 1 and headers[-1].strip().lower().startswith("amount"):
                cp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            style_run(cp.add_run(str(val)), size=9.5,
                      color=INK if is_total else INK_SOFT, bold=is_total)
    if widths:
        for i, w in enumerate(widths):
            for row in t.rows:
                row.cells[i].width = Inches(w)
    return t

def spacer(pts=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(pts)
    return p

# ============ COVER ============
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(2)
style_run(p.add_run("METEORIFY"), size=12, color=ACCENT, bold=True, caps=True)
style_run(p.add_run("   ·   Studio"), size=11, color=INK_DIM)

p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(10)
p.paragraph_format.space_after = Pt(2)
style_run(p.add_run("Scope of Work"), size=30, color=INK, font=HEAD_FONT)

rich([("Meteorify", {"bold":True,"color":INK,"size":12}),
      ("   ×   ", {"color":INK_DIM,"size":12}),
      ("DecentraLabs", {"bold":True,"color":INK,"size":12})], space_after=2)
para("Phase 1  ·  Sales CRM", size=10.5, color=ACCENT, bold=True, space_after=10)

meta = make_table(
    ["Issued", "Reference", "Status", "Delivery"],
    [["21 June 2026", "MTR-SOW-2026-001", "Draft for review", "By agreement"]],
    header_fill="FFFFFF", header_color=ACCENT_HEX)
spacer(6)
para("Teams who have shipped with us:  Metaframe  ·  Mocho  ·  ACPL  ·  Expressmats",
     size=9.5, color=INK_DIM, italic=True, space_after=2)

# ============ 01 OBJECTIVE ============
section_head("01", "The objective")
para("Give DecentraLabs one secure sales command centre that replaces the patchwork of CRMs and spreadsheets.",
     size=12, color=INK, font=HEAD_FONT, space_after=6)
para("Phase 1 is the sales engine, the part of the business currently holding back revenue. By the end of "
     "the build, the team logs in to a single place where every lead, deal, payment and KPI lives together, "
     "with ad leads flowing in on their own and the floor ranked in real time. The calling and WhatsApp layer "
     "follows as Phase 1.5; the broader ops and AI work is Phases 2 and 3. Only the Phase 1 sales CRM is in "
     "scope and priced here.")

# ============ 02 HOW IT BEHAVES ============
section_head("02", "How the CRM behaves")
para("A lead arrives, lands on the board, gets worked and tracked as a deal, and feeds the leaderboard. "
     "One continuous flow, no re-keying. The calling and WhatsApp layer plugs into the same flow in Phase 1.5.")
rich([("Flow:  ", {"bold":True,"color":ACCENT}),
      ("Lead in  →  Pipeline board (New → Contacted → Qualified → Booked → Closed)  →  Notes & payments "
       "recorded on the lead  →  KPIs and the Arena leaderboard update in real time.", {"color":INK_SOFT})],
     size=10)

# ============ 03 HOW IT IS BUILT ============
section_head("03", "How it is built")
para("A custom, production stack on your own database and subdomain. Phase 1 ships the CRM and ad-lead intake. "
     "The calling and WhatsApp layer plugs into the same app in Phase 1.5, so nothing has to be rebuilt to add it.")
make_table(
    ["Layer", "What it is"],
    [["Next.js app", "Pipeline, lead cards, dashboards, mobile"],
     ["App logic & webhooks", "Lead routing, KPI engine, ad-lead intake"],
     ["PostgreSQL — your database", "Relational, indexed, no spreadsheets"],
     ["Lead sources", "Meta Ads via webhook; CSV import and manual entry go straight into the app"],
     ["Calling & messaging (Phase 1.5)", "Dialer, recordings, transcripts, WhatsApp"],
     ["Access & roles", "Secure login, Founder / Closer / Setter scoping"],
     ["Hosting", "DecentraLabs subdomain, SSL, multi-client"]],
    widths=[2.1, 4.3])

# ============ 04 DELIVERABLES ============
section_head("04", "What we deliver")
para("Each item states what it is, how you confirm it is done, and how many rounds of changes are included.")

deliverables = [
    ("D1", "Access & roles",
     ["Secure multi-user login. No shared or open access.",
      "Role-based access for Founder / Admin, Closer and Setter, each seeing only what it should.",
      "Admin view across the whole floor; reps scoped to their own leads and KPIs."],
     "Each of the three roles logs in and sees exactly its permitted screens and data in a live test; a setter cannot view another rep's leads."),
    ("D2", "Leads, pipeline & lead intake",
     ["Lead card with contact, source, priority, follower count, budget, owner, status, notes and full activity history.",
      "Kanban pipeline with configurable stages (your milestones / qualified / cash-collected).",
      "Lead-source attribution, auto-tagging source and UTM on entry.",
      "Meta / Facebook Ads webhook, so new ad leads flow in automatically with no manual entry.",
      "CSV import with de-duplication to port existing GoHighLevel / Iron Forge data, plus CSV export.",
      "Global search, filters, saved views, bulk actions and round-robin assignment to reps."],
     "A test ad lead arrives via webhook, a sample CSV imports with duplicates flagged, and a lead can be moved across all stages, assigned, filtered and found by search, with every change in its activity history."),
    ("D3", "Payments & deals",
     ["Deal value with split / partial payments, tracking each tranche (e.g. a 50,000 deal with 30,000 collected).",
      "Date-based reminder for the next payment split.",
      "Splits auto-feed the KPIs (cash collected, pending) with no double entry.",
      "Contract value, cash collected, pending / outstanding and deals closed."],
     "A deal recorded with a partial payment updates cash-collected and pending automatically, and a split reminder appears on its due date."),
    ("D4", "KPIs, Arena & graphs",
     ["Arena leaderboard, a gamified per-rep ranking that drives the floor.",
      "Graphical dashboards with daily trend graphs, not just monthly totals.",
      "KPIs auto-computed from activity (bookings and payments) per rep and per team: booking rate, no-show, "
      "deals closed, close rate, revenue, cash collected, pending, collect rate, churn, leaderboard rank and "
      "trends. Call-based KPIs switch on with the dialer in Phase 1.5."],
     "Logging bookings and payments updates the matching KPIs and the leaderboard order in real time, with daily, weekly and monthly trend views available."),
    ("D5", "Platform & deployment",
     ["Multi-client command centre to run several clients' sales from one place.",
      "Mobile-responsive across laptop, tablet and phone.",
      "Hosted on a DecentraLabs subdomain, secured with SSL, on your own database.",
      "Hosting, VPS and domain are included in Phase 1 — we set them up and cover them for the build.",
      "Live deployment and a walkthrough handover call."],
     "The system is reachable on the agreed subdomain over HTTPS, usable on a phone, and demonstrated end-to-end on the handover call."),
]
for did, title, items, accept in deliverables:
    subhead(title, accent_label=did)
    for it in items:
        bullet(it)
    accept_line("Acceptance", accept)
    accept_line("Revisions", "2 rounds")

# ============ PHASE 1.5 ============
section_head("1.5", "Phase 1.5 — Calls & messaging")
para("The calling and messaging layer that sits on top of the Phase 1 CRM. It is scoped and priced separately, "
     "and the budget is to be decided for now, because it depends on the dialer provider, the WhatsApp number "
     "and the per-use costs we confirm with you first. It is built on the same stack, so it bolts onto Phase 1 "
     "without a rebuild.")
subhead("What it adds", accent_label="P1.5")
for it in [
    "Click-to-call dialer from the lead card, no switching to another app.",
    "Call recordings and transcripts saved on the lead's activity history.",
    "WhatsApp send to a lead directly from the CRM.",
    "Call-based KPIs (call rate, connected, call outcomes) light up in the Arena once the dialer is live.",
]:
    bullet(it)
accept_line("Budget", "To be decided. Depends on the chosen dialer provider, WhatsApp number and usage costs, all confirmed with you before any commitment.")
accept_line("Timeline", "Scheduled after Phase 1 acceptance, scoped alongside the pricing.")

# ============ 05 NOT IN PHASE 1 ============
section_head("05", "Not in Phase 1")
para("The following are explicitly excluded. They can be added later through a signed change request "
     "(Section 10) or as part of Phases 2 and 3.")
for parts in [
    [("Calls & messaging: ", {"bold":True,"color":INK}), ("the dialer, recordings, transcripts and WhatsApp are Phase 1.5, scoped and priced separately.", {})],
    [("Phase 2 — Ops / Agency: ", {"bold":True,"color":INK}), ("content and delivery workflow, RevShare calculator, daily snapshot emails and agency delivery ops.", {})],
    [("Phase 3 — Marketing & Revenue: ", {"bold":True,"color":INK}), ("per-creator AI content tools (scriptwriter, hook, DM, competitor), marketing analytics and MRR / health-score.", {})],
    [("Email sequences, nurture automation and marketing-metric pulls (these sit in Phase 2).", {})],
    [("The dialer number, WhatsApp number and any third-party subscription or usage fees (these relate to Phase 1.5).", {})],
    [("Data cleaning beyond a straight import and de-duplication of the files you provide.", {})],
    [("Staff training beyond the single handover walkthrough.", {})],
    [("Any integration not named in Section 04.", {})],
]:
    bullet(parts)

# ============ 06 BUILD SEQUENCE ============
section_head("06", "The build sequence")
para("Work runs in four stages, in this order, starting once the advance is paid and the access in Section 08 "
     "is in hand. The delivery date is agreed with you directly rather than fixed in this document.")
make_table(
    ["Stage", "Focus", "What lands"],
    [["One", "Foundation", "Database and schema, secure login and role-based access, and a full import of your existing CRM data with de-duplication."],
     ["Two", "Pipeline", "Lead cards, configurable Kanban stages, source attribution, search, filters, saved views, round-robin, the Meta Ads webhook and CSV import / export."],
     ["Three", "Revenue", "Deals and split-payment tracking, then the KPI engine, Arena leaderboard and dashboards computed from bookings and payments in real time."],
     ["Four", "Launch", "End-to-end testing, mobile-responsive polish, deployment on your subdomain with SSL, and a live walkthrough handover."]],
    widths=[0.8, 1.3, 4.3])

# ============ 07 SIGN-OFF PROCESS ============
section_head("07", "How sign-off works")
for it in [
    "We tell you when Phase 1 is ready for review.",
    "You have 3 business days to check it against the acceptance criteria in Section 04 and either accept it or send written, specific feedback.",
    "If we hear nothing within that window, Phase 1 is treated as accepted.",
    "Feedback within the included revision rounds is handled at no extra cost. Anything beyond that, or outside the agreed criteria, becomes a change request.",
]:
    bullet(it)

# ============ 08 CLIENT RESPONSIBILITIES ============
section_head("08", "What we need from DecentraLabs")
para("The timeline and the price assume you provide the following promptly at the start, so the build is not "
     "waiting on access.")
for it in [
    "A single named point of contact who can give approvals during the build window.",
    "Export or admin access to your current CRMs (Iron Forge and GoHighLevel) for leads, stages and payments.",
    "Meta / Facebook Ads form and webhook access.",
    "Final stage names and your exact KPI definitions, confirmed against Section 04.",
    "Team list with roles (Admin / Closer / Setter).",
    "The subdomain you would like it hosted on (hosting, VPS and domain are covered by us in Phase 1). The dialer and WhatsApp numbers are needed for Phase 1.5, not Phase 1.",
]:
    bullet(it)
para("Delays in providing access push the timeline out and may affect the price.", size=10, color=INK_DIM, italic=True, space_before=2)

# ============ 09 TOOLS ============
section_head("09", "Tools & running costs")
for parts in [
    [("What we build with: ", {"bold":True,"color":INK}), ("a production stack with a relational database, secure role-based auth and API-first integrations. No spreadsheets behind the scenes.", {})],
    [("Hosting, VPS and domain are included in Phase 1. ", {"bold":True,"color":INK}), ("We set them up and cover them as part of the build price.", {})],
    [("Phase 1.5 third-party costs are yours: ", {"bold":True,"color":INK}), ("the dialer / call-recording service and the WhatsApp number are billed directly to DecentraLabs, not included in the build price. We confirm the exact costs before anything proceeds.", {})],
    [("Call transcripts (Phase 1.5) are AI-generated ", {"bold":True,"color":INK}), ("and may contain errors. They are a convenience, not a verbatim legal record, and should be reviewed before being relied on.", {})],
]:
    bullet(parts)

# ============ 10 CHANGES ============
section_head("10", "Changes to scope")
para("Any change to scope, deliverables, timeline or price is written down in a change request and signed by "
     "both sides before that work starts. Additional work outside the included revisions is quoted before it "
     "begins. Nothing verbal is binding.")

# ============ 11 INVESTMENT ============
section_head("11", "Investment")
para("Phase 1 is the minimum build to get a working sales CRM live. The calling and messaging layer (Phase 1.5) "
     "and the later phases are quoted separately once their scope is agreed.")
make_table(
    ["Phase", "Investment", "Notes"],
    [["Phase 1 — Sales CRM", "$1,200", "Everything in Section 04, delivered to the date agreed with you."],
     ["Phase 1.5 — Calls & messaging", "TBD", "Dialer, recordings, transcripts and WhatsApp. Budget decided once the tooling is confirmed."],
     ["Phases 2 & 3 — later", "$1,300", "Ops, AI tools and marketing layers. Scope and split decided closer to the time."]],
    widths=[2.2, 1.1, 3.2])
spacer(6)
subhead("Phase 1 payment schedule")
make_table(
    ["Stage", "Trigger", "Amount (USD)"],
    [["Advance", "On signing, to lock the build slot and begin", "$200"],
     ["On delivery", "Balance, on acceptance of Phase 1", "$1,000"],
     ["Total — Phase 1", "", "$1,200"]],
    widths=[1.5, 3.7, 1.3], total_row=True)
para("A $200 advance on signing locks the build slot and starts the work; the remaining $1,000 is due on the "
     "delivery day, on acceptance of Phase 1. Phase 1.5 (calls and messaging) and Phases 2 and 3 (the $1,300 "
     "ops, AI and marketing layers) are scoped, priced and scheduled separately once we define them together. "
     "Fees are exclusive of any applicable taxes and third-party tool costs.",
     size=9.5, color=INK_DIM, italic=True, space_before=4)

# ============ 12 WHO BUILDS IT ============
section_head("12", "Who builds it")
para("A small, senior team. You talk to the people doing the work.")
p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(1)
style_run(p.add_run("Govind Goel"), size=12, color=INK, bold=True, font=HEAD_FONT)
style_run(p.add_run("  —  Business Head"), size=10, color=ACCENT, bold=True)
para("Owns the relationship, scope and delivery: requirements, sync calls, sign-off and making sure Phase 1 "
     "lands on time.", size=10, space_after=1)
p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
style_run(p.add_run("LinkedIn: "), size=9.5, color=INK_DIM)
style_run(p.add_run("https://www.linkedin.com/in/govind-goel-08886a194"), size=9.5, color=ACCENT)
p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(1)
style_run(p.add_run("Rupayan"), size=12, color=INK, bold=True, font=HEAD_FONT)
style_run(p.add_run("  —  Tech Head"), size=10, color=ACCENT, bold=True)
para("Owns the build: database and architecture, the integrations (Meta Ads, dialer, WhatsApp), deployment and "
     "the security of your data.", size=10)

# ============ 13 SIGN-OFF ============
section_head("13", "Sign-off")
para("By signing below, both parties accept this Scope of Work for Phase 1.")
t = doc.add_table(rows=0, cols=2)
t.alignment = WD_TABLE_ALIGNMENT.CENTER
hdr = t.add_row().cells
for i, (lbl, who, role) in enumerate([("CLIENT","DecentraLabs","Authorised signatory"),
                                       ("SERVICE PROVIDER","Meteorify","Govind Goel, Business Head")]):
    c = hdr[i]; c.text=""
    set_cell_borders(c); cell_margins(c, top=110, bottom=160)
    p0 = c.paragraphs[0]; p0.paragraph_format.space_after = Pt(2)
    style_run(p0.add_run(lbl), size=8.5, color=INK_DIM, bold=True, caps=True)
    p1 = c.add_paragraph(); p1.paragraph_format.space_after = Pt(0)
    style_run(p1.add_run(who), size=12, color=INK, bold=True, font=HEAD_FONT)
    p2 = c.add_paragraph(); p2.paragraph_format.space_after = Pt(0)
    style_run(p2.add_run(role), size=9.5, color=INK_SOFT)
sig = t.add_row().cells
for i in range(2):
    c = sig[i]; c.text=""
    set_cell_borders(c); cell_margins(c, top=200, bottom=80)
    pp = c.paragraphs[0]; pp.paragraph_format.space_after = Pt(0)
    style_run(pp.add_run("Name, signature & date"), size=9, color=INK_DIM)
for i in range(2):
    t.columns[i].width = Inches(3.2)

# ---- footer ----
foot = doc.sections[0].footer
fp = foot.paragraphs[0]
fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
style_run(fp.add_run("Meteorify  ·  Scope of Work  ·  Phase 1  ·  www.usemeteorify.com"),
          size=8.5, color=INK_DIM)

out = "/home/user/sowcontract-/output/meteorify-decentralabs-sow.docx"
doc.save(out)
print("saved", out)
