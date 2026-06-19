from __future__ import annotations

from html import escape
from pathlib import Path

from finance_requirements_generator.schemas import RequirementsPack

MERMAID_CDN_URL = "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs"


def pack_process_map_html_bytes(pack: RequirementsPack) -> bytes:
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
    filename_base = pack.process_key.replace("_", "-")
    svg_download_name = f"{filename_base}-process-map.svg"
    source_download_name = f"{filename_base}-process-map.mmd"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escape(title)}</title>
  <style>
    :root {{
      --ink:#0f1b2d; --ink-soft:#3a4659; --muted:#7c8597;
      --bg:#eef1f5; --card:#ffffff; --line:#dde3ea;
      --gate:#0f1b2d; --step:#0e7c66; --decide:#b45309; --fix:#b91c1c;
      --mono:ui-monospace,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace;
      --sans:ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,
        Arial,sans-serif;
    }}
    * {{ box-sizing:border-box; }}
    html {{ -webkit-text-size-adjust:100%; }}
    body {{
      margin:0; padding:48px 24px 64px; font-family:var(--sans); color:var(--ink);
      background:var(--bg); line-height:1.55;
    }}
    .wrap {{ max-width:1180px; margin:0 auto; }}
    .eyebrow {{
      display:flex; align-items:center; gap:10px; margin:0 0 12px;
      color:var(--step); font-family:var(--mono); font-size:11.5px;
      font-weight:600; letter-spacing:.22em; text-transform:uppercase;
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
    .diagram {{
      display:flex; min-height:220px; align-items:center; padding:30px 22px; overflow-x:auto;
    }}
    .diagram svg {{
      display:block; width:100%; min-width:980px; height:auto; margin:0 auto; max-width:100%;
    }}
    .render-status {{ margin:0; padding:12px 22px; color:var(--muted); font-size:12px; }}
    .diagram-message {{ width:100%; margin:0; color:var(--muted); text-align:center; }}
    .render-fallback {{
      width:100%; max-width:720px; margin:0 auto; padding:18px 20px; text-align:center;
      background:#f8fafc; border:1px solid var(--line); border-radius:8px; color:var(--ink-soft);
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
    button:disabled {{ cursor:not-allowed; opacity:.5; }}
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
      body {{ padding:0; background:#fff; }}
      .card {{ box-shadow:none; }}
      .toolbar, .source, .render-status {{ display:none; }}
      .diagram {{ overflow:visible; }}
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
      <div class="diagram" id="diagram">
        <p class="diagram-message">Rendering process map&hellip;</p>
      </div>
      <p class="render-status" id="render-status">
        Browser rendering uses Mermaid when internet access is available.
      </p>
      <div class="legend" aria-label="Process map legend">
        <div class="key"><span class="swatch gate"></span><b>Gateway</b> &mdash; start / end</div>
        <div class="key">
          <span class="swatch step"></span><b>Process step</b> &mdash; controlled sequence
        </div>
        <div class="key">
          <span class="swatch decide"></span><b>Decision</b> &mdash; control check
        </div>
        <div class="key">
          <span class="swatch fix"></span><b>Exception</b> &mdash; resolve and re-enter
        </div>
      </div>
    </section>

    <div class="toolbar">
      <button class="primary" type="button" onclick="window.print()">Print / Save as PDF</button>
      <button id="download-svg" type="button" onclick="downloadSVG()" disabled>Download SVG</button>
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
      <p>
        Diagram rendering uses Mermaid's browser renderer and may require internet access.
      </p>
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
    function downloadSVG() {{
      const svg = document.querySelector('#diagram svg');
      if (!svg) return;
      const data = new XMLSerializer().serializeToString(svg);
      const url = URL.createObjectURL(new Blob([data], {{type:'image/svg+xml'}}));
      const anchor = document.createElement('a');
      anchor.href = url;
      anchor.download = '{svg_download_name}';
      document.body.appendChild(anchor);
      anchor.click();
      anchor.remove();
      URL.revokeObjectURL(url);
    }}
  </script>
  <script type="module">
    document.addEventListener('DOMContentLoaded', async () => {{
      const diagram = document.getElementById('diagram');
      const status = document.getElementById('render-status');
      try {{
        const {{ default: mermaid }} = await import('{MERMAID_CDN_URL}');
        mermaid.initialize({{
          startOnLoad:false,
          securityLevel:'strict',
          theme:'base',
          flowchart:{{htmlLabels:true,curve:'basis',useMaxWidth:true}},
          themeVariables:{{fontFamily:'Segoe UI, Arial, sans-serif',lineColor:'#94a3b8'}}
        }});
        const rendered = await mermaid.render('finance-process-map', getSource());
        diagram.innerHTML = rendered.svg;
        if (rendered.bindFunctions) rendered.bindFunctions(diagram);
        status.textContent = 'Rendered in your browser.';
        document.getElementById('download-svg').disabled = false;
      }} catch (error) {{
        diagram.innerHTML = `
          <div class="render-fallback" role="status">
            Diagram could not render automatically. Use Copy Mermaid source or Download Mermaid
            source to open it in a Mermaid-compatible tool.
          </div>`;
        status.textContent = 'The technical source remains available from the controls below.';
      }}
    }});
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
