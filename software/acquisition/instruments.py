"""Accès aux instruments de banc décrits dans instruments.yaml (pyvisa + pyvisa-py)."""
from __future__ import annotations

from pathlib import Path

import pyvisa
import yaml

CONFIG = Path(__file__).with_name("instruments.yaml")


def charger_config(chemin: Path = CONFIG) -> dict:
    with open(chemin, encoding="utf-8") as f:
        return yaml.safe_load(f)


def nom_ressource(cfg: dict, protocole: str | None = None) -> str:
    """Construit la chaîne de ressource VISA d'un instrument."""
    ip = cfg.get("ip")
    if not ip:
        raise ValueError(f"Adresse IP manquante pour {cfg.get('modele', '?')}")
    protocole = (protocole or cfg.get("protocole", "INSTR")).upper()
    if protocole == "SOCKET":
        return f"TCPIP::{ip}::{cfg.get('port', 5025)}::SOCKET"
    return f"TCPIP::{ip}::INSTR"


def gestionnaire() -> pyvisa.ResourceManager:
    """Gestionnaire VISA en Python pur (pas besoin de NI-VISA pour le LAN)."""
    return pyvisa.ResourceManager("@py")


def ouvrir(cfg: dict, rm: pyvisa.ResourceManager, protocole: str | None = None,
           timeout_ms: int = 5000):
    """Ouvre la connexion à un instrument et règle terminaisons et délai."""
    inst = rm.open_resource(nom_ressource(cfg, protocole))
    inst.timeout = timeout_ms
    inst.read_termination = "\n"
    inst.write_termination = "\n"
    return inst
