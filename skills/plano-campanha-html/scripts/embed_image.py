#!/usr/bin/env python3
"""Converte uma imagem (logo, foto) em data URI base64 para embutir no HTML.

Uso:
    python embed_image.py caminho/logo.png              # imprime o data URI no stdout
    python embed_image.py caminho/logo.png -o logo.txt  # salva em arquivo (melhor para logos grandes)
"""
import argparse
import base64
import mimetypes
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("image")
    ap.add_argument("-o", "--out")
    args = ap.parse_args()

    mime = mimetypes.guess_type(args.image)[0]
    if not mime or not mime.startswith("image/"):
        sys.exit(f"Tipo de imagem nao reconhecido: {args.image}")
    with open(args.image, "rb") as f:
        data = f.read()
    uri = f"data:{mime};base64,{base64.b64encode(data).decode()}"
    if args.out:
        with open(args.out, "w", encoding="ascii") as f:
            f.write(uri)
        print(f"OK: {args.out} ({len(uri)//1024} KB)", file=sys.stderr)
    else:
        print(uri)


if __name__ == "__main__":
    main()


