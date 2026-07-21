#!/usr/bin/env python3
"""Gera blocos @font-face com a fonte embutida em base64 (Google Fonts).

Uso:
    python embed_font.py --family "Poppins" --weights 400,500,600,700 -o fonts.css

O resultado deve ser colado no lugar do marcador /* {{FONT_FACES}} */ do template.
Requer internet. Para fontes fora do Google Fonts, use arquivos locais:
    python embed_font.py --family "MinhaFonte" --local peso=caminho.ttf,peso=caminho.ttf -o fonts.css
"""
import argparse
import base64
import re
import sys
import urllib.request

UA_WOFF2 = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/125.0 Safari/537.36")


def fetch(url, ua=None):
    req = urllib.request.Request(url, headers={"User-Agent": ua or UA_WOFF2})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def font_face(family, weight, data, fmt):
    mime = {"woff2": "font/woff2", "truetype": "font/ttf"}[fmt]
    b64 = base64.b64encode(data).decode()
    return (f"  @font-face {{\n"
            f"    font-family: '{family}';\n"
            f"    font-style: normal;\n"
            f"    font-weight: {weight};\n"
            f"    font-display: swap;\n"
            f"    src: url(data:{mime};base64,{b64}) format('{fmt}');\n"
            f"  }}\n")


def from_google(family, weights):
    fam = family.replace(" ", "+")
    css_url = (f"https://fonts.googleapis.com/css2?family={fam}:wght@"
               + ";".join(str(w) for w in weights) + "&display=swap")
    css = fetch(css_url).decode()
    blocks = []
    # Um @font-face por peso; pega o bloco latin (último de cada peso costuma ser latin,
    # mas filtramos pelo comentário do subset quando presente)
    faces = re.findall(r"/\*\s*(\S+)\s*\*/\s*@font-face\s*\{(.*?)\}", css, re.S)
    seen = set()
    for subset, body in faces:
        if subset != "latin":
            continue
        m_w = re.search(r"font-weight:\s*(\d+)", body)
        m_u = re.search(r"src:\s*url\((\S+?)\)", body)
        if not (m_w and m_u):
            continue
        weight = int(m_w.group(1))
        if weight in seen or weight not in weights:
            continue
        seen.add(weight)
        data = fetch(m_u.group(1))
        blocks.append(font_face(family, weight, data, "woff2"))
        print(f"  peso {weight}: {len(data)//1024} KB", file=sys.stderr)
    missing = set(weights) - seen
    if missing:
        print(f"AVISO: pesos nao encontrados no Google Fonts: {sorted(missing)}", file=sys.stderr)
    return blocks


def from_local(family, pairs):
    blocks = []
    for pair in pairs.split(","):
        weight, path = pair.split("=", 1)
        with open(path, "rb") as f:
            data = f.read()
        fmt = "woff2" if path.lower().endswith(".woff2") else "truetype"
        blocks.append(font_face(family, int(weight), data, fmt))
        print(f"  peso {weight}: {len(data)//1024} KB ({path})", file=sys.stderr)
    return blocks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)
    ap.add_argument("--weights", default="400,500,600,700")
    ap.add_argument("--local", help="peso=arquivo.ttf,peso=arquivo.woff2 ...")
    ap.add_argument("-o", "--out", default="fonts.css")
    args = ap.parse_args()

    if args.local:
        blocks = from_local(args.family, args.local)
    else:
        weights = [int(w) for w in args.weights.split(",")]
        blocks = from_google(args.family, weights)

    if not blocks:
        sys.exit("Nenhum @font-face gerado.")
    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(blocks))
    print(f"OK: {args.out} ({len(blocks)} blocos @font-face)", file=sys.stderr)


if __name__ == "__main__":
    main()
