"""Interroge *IDN? sur chaque instrument Siglent déclaré dans instruments.yaml.

Usage :
    python idn_check.py              # tous les instruments
    python idn_check.py multimetre   # un seul
    python idn_check.py --sauver     # écrit aussi idn_<date>.yaml dans logs/

Code de sortie : 0 si tous les instruments interrogés ont répondu, 1 sinon.
"""
from __future__ import annotations

import argparse
import sys
import time
from datetime import datetime
from pathlib import Path

import yaml

from instruments import charger_config, gestionnaire, nom_ressource, ouvrir


def interroger(nom: str, cfg: dict, rm) -> dict:
    resultat = {"modele_attendu": cfg.get("modele"), "ip": cfg.get("ip")}
    if not cfg.get("ip"):
        resultat["erreur"] = "IP non renseignée"
        return resultat

    premier = cfg.get("protocole", "INSTR").upper()
    essais = [premier] + (["SOCKET"] if premier == "INSTR" else [])
    erreurs = []
    for proto in essais:
        try:
            t0 = time.perf_counter()
            inst = ouvrir(cfg, rm, proto)
            try:
                idn = inst.query("*IDN?").strip()
            finally:
                inst.close()
            resultat.update(
                ressource=nom_ressource(cfg, proto),
                idn=idn,
                latence_ms=round((time.perf_counter() - t0) * 1000, 1),
            )
            champs = [c.strip() for c in idn.split(",")]
            if len(champs) == 4:
                resultat.update(fabricant=champs[0], modele=champs[1],
                                numero_serie=champs[2], firmware=champs[3])
            if cfg.get("modele") and cfg["modele"] not in idn:
                resultat["avertissement"] = "modèle inattendu"
            return resultat
        except Exception as e:  # noqa: BLE001 — on rapporte toute erreur de connexion
            erreurs.append(f"{proto}: {type(e).__name__}: {e}")
    resultat["erreur"] = " | ".join(erreurs)
    return resultat


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("noms", nargs="*", help="instruments à interroger (défaut : tous)")
    p.add_argument("--sauver", action="store_true", help="écrire le résultat dans logs/")
    args = p.parse_args()

    config = charger_config()["instruments"]
    noms = args.noms or list(config)
    inconnus = [n for n in noms if n not in config]
    if inconnus:
        print(f"Instrument(s) inconnu(s) : {', '.join(inconnus)}. Choix : {', '.join(config)}")
        return 2

    rm = gestionnaire()
    resultats = {}
    for nom in noms:
        r = interroger(nom, config[nom], rm)
        resultats[nom] = r
        if "idn" in r:
            extra = f"  [{r['avertissement']}]" if "avertissement" in r else ""
            print(f"OK    {nom:<13} {r['ip']:<15} {r['latence_ms']:>7} ms  {r['idn']}{extra}")
        else:
            print(f"ÉCHEC {nom:<13} {str(r['ip']):<15} {r['erreur']}")

    if args.sauver:
        dossier = Path(__file__).with_name("logs")
        dossier.mkdir(exist_ok=True)
        horodatage = datetime.now().astimezone()
        fichier = dossier / f"idn_{horodatage:%Y%m%d-%H%M%S}.yaml"
        with open(fichier, "w", encoding="utf-8") as f:
            yaml.safe_dump({"date": horodatage.isoformat(timespec="seconds"),
                            "instruments": resultats},
                           f, allow_unicode=True, sort_keys=False)
        print(f"\nRésultat enregistré : {fichier}")

    return 0 if all("idn" in r for r in resultats.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
