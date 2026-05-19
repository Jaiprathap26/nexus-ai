import io, contextlib
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

def run_nexus_sim():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(open("nexus_sim.py").read())
    return buf.getvalue()

@app.get("/", response_class=HTMLResponse)
def dashboard():
    output = run_nexus_sim()
    lines = output.split("\n")
    rows = "".join(f"<tr><td style='font-family:monospace;white-space:pre;padding:2px 8px'>{l}</td></tr>" for l in lines)
    return f"""<!DOCTYPE html>
<html><head><title>NEXUS</title>
<style>body{{background:#0d1117;color:#e6edf3;padding:20px}}
table{{border-collapse:collapse;width:100%}}
td{{border-bottom:1px solid #21262d}}
h1{{color:#58a6ff}}.badge{{background:#238636;color:#fff;padding:3px 8px;border-radius:4px;font-size:12px}}</style>
</head><body>
<h1>NEXUS <span class="badge">LIVE</span></h1>
<p style="color:#8b949e">Autonomous Competitive Revenue Intelligence</p>
<table>{rows}</table>
</body></html>"""

@app.get("/health")
def health():
    return {"status": "ok"}