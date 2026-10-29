#!/usr/bin/env python3
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "profile" / "assets"

EARS = '<path d="M20 16l-4-7M44 16l4-7" stroke="#3ddc84" stroke-width="4" stroke-linecap="round"/>'
GROUND = '<rect x="4" y="48" width="56" height="8" rx="4" fill="#3ddc84"/>'
SNOUT = '<ellipse cx="32" cy="39" rx="5" ry="3.5" fill="#d9b48f"/><circle cx="32" cy="38" r="1.8" fill="#1b1b1b"/>'
LEFT = '<path d="M32 16c-13.3 0-24 10.7-24 24v8h24z" fill="#8a5a3c"/><circle cx="23" cy="32" r="3.5" fill="#1b1b1b"/>'
RIGHT_HALF = "M32 16a24 24 0 0 1 24 24v8H32z"


def half(fill, extra=""):
    return f'<path d="{RIGHT_HALF}" fill="{fill}"/>{extra}'


GLOBE = '<path d="M32 16a12 24 0 0 1 11.31 32M32 28h20.78M32 40h24" stroke="#fff" stroke-opacity=".6" stroke-width="2"/>'

RIGHTS = {
    "holtdroid": '<path d="M32 16c13.3 0 24 10.7 24 24v8H32z" fill="#8a5a3c"/><circle cx="41" cy="32" r="3.5" fill="#1b1b1b"/>',
    "holtdroid-webview": half("#4285f4", GLOBE),
    "holtdroid-tunnel": half(
        "#8e949a",
        '<path d="M32 24h17.89M32 32h22.63M44 19.22v4.78M38 24v8M50 24.13v7.87M44 32v8" stroke="#000" stroke-opacity=".25" stroke-width="1.2"/>'
        '<path d="M35 48v-7a9 9 0 0 1 18 0v7z" fill="#d3d6da"/><path d="M38 48v-7a6 6 0 0 1 12 0v7z" fill="#1b1b1b"/>'
        '<circle cx="44" cy="44" r="1.6" fill="#ffe08a"/>',
    ),
    "holtdroid-redroid": half(
        "#e5533d",
        '<path d="M37 21v27M42 18.5v29.5M47 19.5v28.5M52 25v23" stroke="#000" stroke-opacity=".22" stroke-width="2"/>'
        '<path d="M32 30h24" stroke="#fff" stroke-opacity=".55" stroke-width="2"/>',
    ),
    "holtdroid-sync": half(
        "#8b6cff",
        '<path d="M45 22v16M39.5 32.5 45 38l5.5-5.5" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M38 43h14" stroke="#fff" stroke-opacity=".6" stroke-width="2.4" stroke-linecap="round"/>',
    ),
    "chromium-builds": half(
        "#1a73e8",
        '<path d="M32 26a12 12 0 0 1 0 24" stroke="#fff" stroke-opacity=".85" stroke-width="3" fill="none"/>'
        '<path d="M32 33a5 5 0 0 1 0 10z" fill="#fff"/>'
        '<path d="M44 20l6 6" stroke="#fbbc04" stroke-width="3" stroke-linecap="round"/>',
    ),
}


def icon(repo):
    if repo == "holtdroid":
        body = '<path d="M8 40c0-13.3 10.7-24 24-24s24 10.7 24 24v8H8z" fill="#8a5a3c"/><circle cx="23" cy="32" r="3.5" fill="#1b1b1b"/><circle cx="41" cy="32" r="3.5" fill="#1b1b1b"/>'
    else:
        clip = f"half-{repo}"
        body = f'<clipPath id="{clip}"><path d="{RIGHT_HALF}"/></clipPath>{LEFT}<g clip-path="url(#{clip})">{RIGHTS[repo]}</g>'
    return f'<g fill="none">{body}{EARS}{SNOUT}{GROUND}</g>'


REPOS = [
    {
        "repo": "holtdroid",
        "title": "Holtdroid",
        "accent": "#3ddc84",
        "lines": ["A cozy holt for your test Androids.", "Device screen, WebView DevTools, clipboard", "and VPN for any APK, in one browser tab."],
        "chips": ["Go", "React", "Kubernetes", "Apache-2.0"],
    },
    {
        "repo": "holtdroid-webview",
        "title": "WebView",
        "accent": "#4285f4",
        "lines": ["An Android WebView playground", "with DevTools unlocked, presets", "and adb control."],
        "chips": ["Kotlin", "WebView", "GeckoView"],
    },
    {
        "repo": "holtdroid-tunnel",
        "title": "Tunnel",
        "accent": "#b9bec4",
        "lines": ["All of a phone's traffic over USB", "to the host. No root, no Wi-Fi,", "no mobile data."],
        "chips": ["Kotlin", "VpnService", "SOCKS5"],
    },
    {
        "repo": "holtdroid-redroid",
        "title": "Redroid images",
        "accent": "#e5533d",
        "lines": ["Android in a container, one image", "per version, with ARM64 translation", "for Holtdroid sessions."],
        "chips": ["Android 11–15", "redroid", "x86_64"],
    },
    {
        "repo": "holtdroid-sync",
        "title": "Sync",
        "accent": "#8b6cff",
        "lines": ["Brings APKs into Holtdroid", "from Slack, S3 buckets", "and GitHub releases."],
        "chips": ["Go", "Slack", "S3", "GitHub"],
    },
    {
        "repo": "chromium-builds",
        "title": "Chromium builds",
        "accent": "#1a73e8",
        "lines": ["Chromium and WebView for Android", "from release tags, with proprietary", "codecs, for x86_64 and arm64."],
        "chips": ["Chromium", "WebView", "APK"],
    },
]

FONT = "Helvetica Neue, Helvetica, Arial, sans-serif"
MONO = "Menlo, SF Mono, monospace"


def background(w, h, accent, cx=0.2, cy=0.55):
    return f"""<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#0c110f"/><stop offset="1" stop-color="#121c17"/>
  </linearGradient>
  <radialGradient id="glow" cx="{w * cx}" cy="{h * cy}" r="{h * 0.75}" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="{accent}" stop-opacity=".22"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/>
  </radialGradient>
  <pattern id="dots" width="32" height="32" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.4" fill="#fff" fill-opacity=".05"/>
  </pattern>
</defs>
<rect width="{w}" height="{h}" fill="url(#bg)"/>
<rect width="{w}" height="{h}" fill="url(#dots)"/>
<rect width="{w}" height="{h}" fill="url(#glow)"/>
<rect y="{h - 10}" width="{w}" height="10" fill="#3ddc84"/>"""


def chips(x, y, items, accent):
    out, cx = [], x
    for c in items:
        width = 26 + len(c) * 14.5
        out.append(
            f'<rect x="{cx}" y="{y}" width="{width}" height="44" rx="22" fill="{accent}" fill-opacity=".14" stroke="{accent}" stroke-opacity=".5"/>'
            f'<text x="{cx + width / 2}" y="{y + 29}" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="500" fill="#dfe7e2">{c}</text>'
        )
        cx += width + 12
    return "".join(out)


def social(r):
    w, h = 1280, 640
    lines = "".join(
        f'<text x="520" y="{318 + i * 46}" font-family="{FONT}" font-size="34" fill="#b9c4be">{l}</text>' for i, l in enumerate(r["lines"])
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
{background(w, h, r["accent"])}
<g transform="translate(96 160) scale(5.4)">{icon(r["repo"])}</g>
<text x="520" y="188" font-family="{MONO}" font-size="30" fill="#3ddc84">holtdroid/<tspan fill="#8fa197">{r["repo"]}</tspan></text>
<text x="520" y="268" font-family="{FONT}" font-size="80" font-weight="700" fill="#f4f7f5">{r["title"]}</text>
{lines}
{chips(520, 488, r["chips"], r["accent"])}
<text x="1220" y="590" text-anchor="end" font-family="{MONO}" font-size="22" fill="#6f817a">holtdroid.github.io/holtdroid</text>
</svg>"""


def profile_banner():
    w, h = 1280, 420
    row = "".join(
        f'<g transform="translate({540 + i * 118} 282) scale(1.5)">{icon(r["repo"])}</g>' for i, r in enumerate(REPOS)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
{background(w, h, "#3ddc84")}
<g transform="translate(110 70) scale(4.4)">{icon("holtdroid")}</g>
<text x="540" y="150" font-family="{FONT}" font-size="92" font-weight="700" fill="#f4f7f5">Holtdroid</text>
<text x="544" y="208" font-family="{FONT}" font-size="34" fill="#b9c4be">A cozy holt for your test Androids.</text>
<text x="544" y="252" font-family="{FONT}" font-size="24" fill="#7f9189">Self-hosted Android sandboxes for APK testing, in your browser.</text>
{row}
</svg>"""


def avatar():
    w = 512
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{w}" viewBox="0 0 {w} {w}">
{background(w, w, "#3ddc84", 0.5, 0.5).replace(f'<rect y="{w - 10}" width="{w}" height="10" fill="#3ddc84"/>', "")}
<g transform="translate(64 61) scale(6)">{icon("holtdroid")}</g>
</svg>"""


def write(name, svg, width):
    path = OUT / f"{name}.svg"
    path.write_text(svg)
    subprocess.run(["rsvg-convert", "-w", str(width), "-o", str(OUT / f"{name}.png"), str(path)], check=True)


OUT.mkdir(parents=True, exist_ok=True)
write("banner", profile_banner(), 1280)
write("avatar", avatar(), 512)
for r in REPOS:
    write(f"social-{r['repo']}", social(r), 1280)
    write(f"icon-{r['repo']}", f'<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 64 64">{icon(r["repo"])}</svg>', 128)
