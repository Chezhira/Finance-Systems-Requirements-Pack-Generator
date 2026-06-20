from __future__ import annotations

from html import escape
from pathlib import Path

from finance_requirements_generator.schemas import ProcessMapFlow, RequirementsPack


def pack_process_map_html_bytes(pack: RequirementsPack) -> bytes:
    flow = _require_flow(pack)
    title = f"{pack.process_name} - Process Map"
    subtitle = (
        f"{pack.process_name} control flow from process trigger through validation, exception "
        "resolution, approval, reporting, and implementation readiness."
    )
    source = escape(pack.mermaid_process_map)
    public_safe_note = escape(
        pack.public_safe_sample_data_note
        or "This public-safe sample output contains no confidential business information."
    )
    source_download_name = f"{pack.process_key.replace('_', '-')}-process-map.mmd"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escape(title)}</title>
  <style>
    :root {{
      --ink:#0f1b2d; --ink-soft:#3a4659; --muted:#7c8597;
      --bg:#eef1f5; --card:#ffffff; --line:#dde3ea; --connector:#a9b6c8;
      --gate:#0f1b2d; --step:#0e7c66; --decide:#b45309; --fix:#b91c1c;
      --mono:ui-monospace,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace;
      --sans:ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,
        Arial,sans-serif;
    }}
    * {{ box-sizing:border-box; }}
    html {{ -webkit-text-size-adjust:100%; }}
    body {{
      margin:0; padding:48px 24px 64px; background:var(--bg); color:var(--ink);
      font-family:var(--sans); line-height:1.55;
    }}
    .wrap {{ max-width:1180px; margin:0 auto; }}
    .eyebrow {{
      display:flex; align-items:center; gap:10px; margin:0 0 12px; color:var(--step);
      font-family:var(--mono); font-size:11.5px; font-weight:600; letter-spacing:.22em;
      text-transform:uppercase;
    }}
    .eyebrow::before {{ content:""; width:26px; height:2px; background:var(--step); }}
    h1 {{ margin:0 0 8px; color:var(--ink); font-size:30px; font-weight:650; }}
    .sub {{ max-width:72ch; margin:0; color:var(--ink-soft); font-size:15.5px; }}
    .card {{
      margin-top:30px; overflow:hidden; background:var(--card); border:1px solid var(--line);
      border-radius:8px;
      box-shadow:0 1px 2px rgba(16,24,40,.04), 0 18px 40px -24px rgba(16,24,40,.18);
    }}
    .card-head {{
      display:flex; justify-content:space-between; align-items:center; gap:16px;
      padding:16px 22px; border-bottom:1px solid var(--line); background:#fbfcfe;
    }}
    .card-head h2 {{ margin:0; color:var(--ink-soft); font-size:13px; font-weight:600; }}
    .flow-tag {{
      color:var(--muted); font-family:var(--mono); font-size:11px; letter-spacing:.06em;
    }}
    .flow-scroll {{ padding:34px 22px; overflow-x:auto; background:#fff; }}
    .flow-track {{
      display:flex; min-width:1680px; align-items:center; justify-content:flex-start;
    }}
    .flow-node {{
      display:flex; width:180px; min-height:94px; flex:0 0 180px; flex-direction:column;
      align-items:center; justify-content:center; padding:14px 13px; border:2px solid var(--step);
      border-radius:6px; background:#fff; color:var(--ink); text-align:center;
    }}
    .flow-node.gate {{
      width:158px; flex-basis:158px; border-color:var(--gate); background:var(--gate); color:#fff;
    }}
    .flow-node.decide {{
      width:170px; flex-basis:170px; border-color:var(--decide); background:#fef3c7;
      color:#7c2d12;
    }}
    .flow-node.fix {{
      width:178px; min-height:78px; flex-basis:178px; border-color:var(--fix);
      background:#fee2e2; color:#7f1d1d;
    }}
    .node-kind {{
      margin-bottom:6px; font-family:var(--mono); font-size:9px; font-weight:700;
      letter-spacing:.12em; text-transform:uppercase; opacity:.72;
    }}
    .node-label {{ font-size:13px; font-weight:600; line-height:1.35; }}
    .connector {{
      position:relative; width:32px; height:2px; flex:0 0 32px; background:var(--connector);
    }}
    .connector::after {{
      content:""; position:absolute; top:-4px; right:-1px; border-width:5px 0 5px 7px;
      border-style:solid; border-color:transparent transparent transparent var(--connector);
    }}
    .branch-stage {{
      position:relative; width:290px; height:180px; flex:0 0 290px;
    }}
    .branch-connectors {{
      position:absolute; inset:0; width:290px; height:180px; overflow:visible;
    }}
    .branch-connectors > path {{
      fill:none; stroke:var(--connector); stroke-width:2; vector-effect:non-scaling-stroke;
    }}
    .branch-label {{
      position:absolute; z-index:2; padding:2px 5px; background:#fff; color:var(--muted);
      font-family:var(--mono); font-size:10px; font-weight:700; text-transform:uppercase;
    }}
    .branch-label.no {{ top:18px; left:132px; }}
    .branch-label.yes {{ top:69px; left:12px; }}
    .branch-stage .flow-node.fix {{
      position:absolute; z-index:3; top:51px; left:55px; width:178px; min-height:78px;
    }}
    .legend {{
      display:flex; flex-wrap:wrap; gap:10px 26px; padding:18px 22px;
      border-top:1px solid var(--line); background:#fbfcfe;
    }}
    .key {{ display:flex; align-items:center; gap:9px; color:var(--ink-soft); font-size:13px; }}
    .key b {{ color:var(--ink); font-weight:600; }}
    .swatch {{ width:15px; height:15px; border-radius:4px; flex:0 0 auto; }}
    .swatch.gate {{ background:var(--gate); }}
    .swatch.step {{ background:#fff; border:1.5px solid var(--step); }}
    .swatch.decide {{ background:#fef3c7; border:1.5px solid var(--decide); }}
    .swatch.fix {{ background:#fee2e2; border:1.5px solid var(--fix); }}
    .toolbar {{ display:flex; flex-wrap:wrap; gap:10px; margin-top:22px; }}
    button {{
      padding:10px 17px; cursor:pointer; background:#fff; border:1px solid var(--line);
      border-radius:8px; color:var(--ink); font:inherit; font-size:14px; font-weight:550;
    }}
    button:hover {{ border-color:var(--step); color:var(--step); }}
    button.primary {{ background:var(--ink); border-color:var(--ink); color:#fff; }}
    .source {{
      margin-top:22px; background:var(--card); border:1px solid var(--line); border-radius:8px;
    }}
    .source summary {{ padding:14px 18px; cursor:pointer; color:var(--ink-soft); font-weight:600; }}
    .source-note {{ margin:0; padding:0 18px 14px; color:var(--muted); font-size:13px; }}
    pre.raw-source {{
      margin:0; padding:18px; overflow:auto; border-top:1px solid var(--line);
      background:#f8fafc; color:#243247; font-family:var(--mono); font-size:12px; white-space:pre;
    }}
    footer {{ margin-top:20px; color:var(--muted); font-family:var(--mono); font-size:12px; }}
    footer p {{ margin:5px 0; }}
    @media (max-width:640px) {{
      body {{ padding:32px 16px 48px; }}
      h1 {{ font-size:24px; }}
      .card-head {{ align-items:flex-start; flex-direction:column; }}
    }}
    @media print {{
      @page {{ size:landscape; margin:.4in; }}
      body {{ padding:0; background:#fff; }}
      .card {{ box-shadow:none; }}
      .toolbar, .source {{ display:none; }}
      .flow-scroll {{ overflow:visible; padding:22px 12px; }}
      .flow-track {{ min-width:1680px; zoom:.62; }}
      footer {{ margin-top:12px; }}
    }}
  </style>
</head>
<body>
  <main class="wrap">
    <p class="eyebrow">Finance Operations &middot; Control Flow</p>
    <h1>{escape(pack.process_name)} &mdash; Process Map</h1>
    <p class="sub">{escape(subtitle)}</p>

    <section class="card" aria-labelledby="flow-heading">
      <div class="card-head">
        <h2 id="flow-heading">Process flow</h2>
        <span class="flow-tag">trigger &rarr; sign-off</span>
      </div>
      <div class="flow-scroll">
        <div class="flow-track" role="img" aria-label="{escape(title)}">
          {_node(flow.trigger, "gate", "Start")}
          <span class="connector" aria-hidden="true"></span>
          {_node(flow.source, "step", "Intake")}
          <span class="connector" aria-hidden="true"></span>
          {_node(flow.validation, "step", "Validate")}
          <span class="connector" aria-hidden="true"></span>
          {_node(flow.decision, "decide", "Decision")}
          {_branch_stage(flow.exception_resolution)}
          {_node(flow.approval, "step", "Approve")}
          <span class="connector" aria-hidden="true"></span>
          {_node(flow.reporting, "step", "Evidence")}
          <span class="connector" aria-hidden="true"></span>
          {_node(flow.signoff, "gate", "Sign-off")}
        </div>
      </div>
      {_legend()}
    </section>

    <div class="toolbar">
      <button class="primary" type="button" onclick="window.print()">Print / Save as PDF</button>
      <button type="button" onclick="copySource()">Copy Mermaid source</button>
      <button type="button" onclick="downloadSource()">Download Mermaid source</button>
    </div>

    <details class="source">
      <summary>Advanced: Mermaid source</summary>
      <p class="source-note">
        Technical users can copy or download this source for Mermaid-compatible tools.
      </p>
      <pre class="raw-source" id="raw-source">{source}</pre>
    </details>

    <footer>
      <p>{public_safe_note}</p>
      <p>
        Generated by Chez Solutions &middot; deterministic finance systems implementation artefact
      </p>
    </footer>
  </main>
  <script>
    function getSource() {{
      return document.getElementById('raw-source').textContent;
    }}
    async function copySource() {{
      const source = getSource();
      if (navigator.clipboard && window.isSecureContext) {{
        await navigator.clipboard.writeText(source);
        return;
      }}
      const field = document.createElement('textarea');
      field.value = source;
      field.style.position = 'fixed';
      field.style.opacity = '0';
      document.body.appendChild(field);
      field.select();
      document.execCommand('copy');
      field.remove();
    }}
    function downloadSource() {{
      const url = URL.createObjectURL(new Blob([getSource()], {{type:'text/plain;charset=utf-8'}}));
      const anchor = document.createElement('a');
      anchor.href = url;
      anchor.download = '{source_download_name}';
      document.body.appendChild(anchor);
      anchor.click();
      anchor.remove();
      URL.revokeObjectURL(url);
    }}
  </script>
</body>
</html>
"""
    return html.encode("utf-8")


def export_process_map_html(pack: RequirementsPack, output_path: str | Path) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(pack_process_map_html_bytes(pack))
    return path


def _require_flow(pack: RequirementsPack) -> ProcessMapFlow:
    if pack.process_map_flow is None:
        raise ValueError("RequirementsPack does not contain structured process-map flow data")
    return pack.process_map_flow


def _node(label: str, css_class: str, kind: str) -> str:
    return (
        f'<div class="flow-node {css_class}">'
        f'<span class="node-kind">{escape(kind)}</span>'
        f'<span class="node-label">{escape(label)}</span>'
        "</div>"
    )


def _legend() -> str:
    return """<div class="legend" aria-label="Process map legend">
        <div class="key"><span class="swatch gate"></span><b>Gateway</b> &mdash; start / end</div>
        <div class="key"><span class="swatch step"></span><b>Process step</b> &mdash; sequence</div>
        <div class="key">
          <span class="swatch decide"></span><b>Decision</b> &mdash; control check
        </div>
        <div class="key"><span class="swatch fix"></span><b>Exception</b> &mdash; remediate</div>
      </div>"""


def _branch_stage(exception_label: str) -> str:
    return f"""<div class="branch-stage" aria-label="Exception decision routes">
            <svg class="branch-connectors" viewBox="0 0 290 180" aria-hidden="true">
              <defs>
                <marker id="branch-arrow" viewBox="0 0 10 10" refX="9" refY="5"
                  markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                  <path d="M 0 0 L 10 5 L 0 10 z" fill="#a9b6c8" stroke="none"></path>
                </marker>
              </defs>
              <path d="M 0 90 H 32 V 30 H 270 V 90 H 290" marker-end="url(#branch-arrow)"></path>
              <path d="M 0 90 H 55" marker-end="url(#branch-arrow)"></path>
              <path d="M 233 90 H 290" marker-end="url(#branch-arrow)"></path>
            </svg>
            <span class="branch-label no">No &middot; continue</span>
            <span class="branch-label yes">Yes</span>
            {_node(exception_label, "fix", "Remediate")}
          </div>"""
