import time, random

COMPLAINTS = [
    {"reviewer": "Kevin O.", "title": "Engineering VP", "company": "ScaleUp Tech",
     "source": "G2", "rating": 1, "score": 82, "is_dm": True,
     "text": "LambdaTest has constant session timeouts. cc @BrowserStack -- sending you our contract renewal."},
    {"reviewer": "Aisha B.", "title": "CTO", "company": "Fintech Startup",
     "source": "Capterra", "rating": 1, "score": 66, "is_dm": True,
     "text": "Parallel test execution is broken. Promised 100 parallel sessions, getting 20."},
    {"reviewer": "Neha K.", "title": "VP Engineering", "company": "E-commerce Co",
     "source": "Twitter", "rating": 2, "score": 56, "is_dm": True,
     "text": "LambdaTest support takes 3 days to respond. Unacceptable. Moving platforms."},
    {"reviewer": "Paul H.", "title": "QA Manager", "company": "Enterprise Firm",
     "source": "Trustpilot", "rating": 2, "score": 69, "is_dm": False,
     "text": "The grid is unreliable. Tests that pass locally fail randomly on LambdaTest."},
    {"reviewer": "Raj P.", "title": "QA Lead", "company": "TechCorp India",
     "source": "G2", "rating": 1, "score": 63, "is_dm": False,
     "text": "Constant session timeouts. Zero response from support for 2 weeks."},
    {"reviewer": "Chen W.", "title": "Senior Dev", "company": "SaaS Startup",
     "source": "Reddit", "rating": 2, "score": 45, "is_dm": False,
     "text": "LambdaTest was down for 4 hours during our product launch. No compensation."},
    {"reviewer": "Maria G.", "title": "QA Engineer", "company": "HealthTech",
     "source": "Glassdoor", "rating": 2, "score": 41, "is_dm": False,
     "text": "Dashboard is confusing and pricing went up 40% without notice."},
    {"reviewer": "Tom B.", "title": "Dev Manager", "company": "Startup",
     "source": "Reddit", "rating": 3, "score": 28, "is_dm": False,
     "text": "LambdaTest is okay I guess, just not as polished as others."},
]

EMAIL = """Hi Kevin,

I came across your review of LambdaTest -- your point about 'cc @BrowserStack -- sending you our contract renewal.'

That's exactly the frustration we built BrowserStack to solve.

We offer:
- 99.9% uptime SLA with auto-credits for any incident
- Guaranteed parallel sessions -- no throttling mid-contract
- 24/7 enterprise support, 2-hour response SLA

Teams moving from LambdaTest see stability go from 60% to 98%+ in week one.

Free 15-min demo this week? https://browserstack.com/demo

Team BrowserStack"""

WHATSAPP = "Hi Kevin! Saw your LambdaTest review -- 'cc @BrowserStack -- sending you our contract renewal.' We built BrowserStack for this. 99.9% uptime SLA + guaranteed parallel sessions. Free demo? https://browserstack.com/demo"

def sep(c="=", n=68): print(c * n)

def run():
    print(); sep()
    print("  NEXUS -- AUTONOMOUS COMPETITIVE REVENUE INTELLIGENCE")
    print("  SIMULATION MODE -- Full Pipeline Demo")
    sep(); print()

    print("[1/6] Initializing database...")
    time.sleep(0.3)
    print("      [OK] Tables: complaints, targets, outreach, leads, deals")
    print("      [OK] Client: BrowserStack | Competitor: LambdaTest"); print()

    print("[2/6] SOURCE MONITOR -- Scanning 8 platforms...")
    for p in ["G2","Trustpilot","Capterra","Reddit","Twitter/X","Glassdoor","Google Maps","LinkedIn"]:
        time.sleep(0.1); print(f"        {p:15} -- {random.randint(1,3)} complaint(s) found")
    print(); print("      [OK] 8 total complaints captured")
    for c in COMPLAINTS[:3]:
        print(f"        [{c['source']:10}] {c['reviewer']:18} ({c['rating']}/5) -- {c['text'][:60]}..."); print()

    print("[3/6] INTENT SCORER -- Scoring decision-maker probability...")
    time.sleep(0.5)
    q = [c for c in COMPLAINTS if c["score"] >= 40]
    print(f"      [OK] Qualified: {len(q)}/{len(COMPLAINTS)} (threshold: 40/100)"); print()
    print("      TOP TARGETS:")
    for t in sorted(q, key=lambda x: -x["score"])[:5]:
        dm = "[DM]" if t["is_dm"] else "    "
        print(f"        {dm} [{t['score']:3}/100] {t['reviewer']:20} {t['title']:25} @ {t['company']}"); print()

    print("[4/6] OUTREACH WRITER -- Generating personalized messages...")
    time.sleep(0.6)
    print("      [OK] 2 messages for Kevin O. (Engineering VP, ScaleUp Tech)"); print()
    print("      -- EMAIL --"); print()
    for line in EMAIL.split("\n"): print(f"      {line}")
    print(); print("      -- WHATSAPP --"); print(f"      {WHATSAPP}"); print()

    print("[5/6] CHANNEL DISPATCHER -- Dispatching...")
    time.sleep(0.3)
    print("      Mode: DRY RUN (add API keys in .env to go live)")
    print("        email     --> queued"); print("        whatsapp  --> queued"); print()

    print("[6/6] SUMMARY"); print()
    print(f"      Platforms scanned     : 8")
    print(f"      Complaints detected   : {len(COMPLAINTS)}")
    print(f"      Qualified targets     : {len(q)}")
    print(f"      Decision-makers found : {sum(1 for c in q if c['is_dm'])}")
    print(f"      Outreach messages     : {len(q) * 2}"); print()
    sep("-"); print()
    print("  WEEKLY REPORT: 47 LambdaTest complaints tracked. 12 decision-makers.")
    print("  Kevin O. (VP Eng, ScaleUp Tech) replied -- demo booked Friday.")
    print("  1 deal closed: $24,000 ARR from QA Manager who switched from LambdaTest.")
    print(); sep("-"); print()
    print("  [OK] Simulation complete.")
    print(); sep(); print()

run()