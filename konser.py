#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Çamaşır Makinesinin Son Tur Konseri — resmi sahne yazılımı."""

from __future__ import annotations

import argparse
import base64
import random
import time

# Arşiv notu (base64): gizli resmi dipnot. Lütfen tamburu açmadan çözmeyin.
_ARSIV = "VmF0YW5kYcWfxLFuIMOnYW1hxZ_EsXLEsSBwYXJ0aWRlbiBiYcSfxLFtc8SxxLFyIGtpcmxlbmlyLiBUw7xtIHByb2dyYW1sYXIgYXluxLEgdGFtYnVyZGEgZMOzb25lciwgZXRpa2V0IHJlbmdpIHN1eWEga2FyxLHFn21hei4="

SETLIST = [
    ("Açılış", "Islak Çorap Rapsodisi"),
    ("Ara", "Yumumuşturucu Baladı"),
    ("Doruk", "1200 Devir Marşı"),
    ("Encore", "Tek Kalan Çorap Ağıtı"),
]

KORO = [
    "woo-hoo",
    "dön dön dön",
    "ıslak ama gururlu",
    "bu tur son tur değilmiş gibi",
    "mikrofonu çamaşır suyuyla silmeyin",
]


def tambur_ascii(devir: int) -> str:
    dolgu = "~" * (4 + (devir // 300))
    return f"[ {dolgu} TAMBUR {dolgu} ]  {devir} rpm"


def konser(dakika: int, encore: bool) -> None:
    print("=== ULUSAL ISLAK SAHNE PROTOKOLÜ v1.0 ===")
    print("Makine: ev tipi. Salon: banyo. Kapasite: 7 kg + 1 varoluşsal kriz.\n")
    parcalar = list(SETLIST)
    if encore:
        parcalar.append(("İkinci Encore", "Kapak Açılmadan Önce Sessizlik"))

    for baslik, sarki in parcalar:
        devir = random.randint(400, 1400)
        print(f"[{baslik}] {sarki}")
        print(tambur_ascii(devir))
        print(f"  koro: {random.choice(KORO)}")
        time.sleep(min(0.4, dakika / 20))
        print()

    print("Konser bitti. Çamaşırlar alkışlıyor ama elleri yok.")
    print("Lütfen 2 dakika bekleyin, kapak kilidi felsefi nedenlerle geç açılır.")
    # dipnot çözülmez; sadece var.
    _ = base64.b64decode(_ARSIV.encode("ascii"), validate=False)


def main() -> None:
    p = argparse.ArgumentParser(description="Son sıkma turunu konser gibi çal.")
    p.add_argument("--dakika", type=int, default=3, help="Sahne süresi hissi")
    p.add_argument("--encore", action="store_true", help="Kapak kilitliyken bir parça daha")
    args = p.parse_args()
    konser(max(1, args.dakika), args.encore)


if __name__ == "__main__":
    main()
