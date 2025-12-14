from __future__ import annotations
from typing import Iterable, Tuple
from .schema import Intent, Constraint

def normalize_goal(goal: str) -> str:
    return " ".join(goal.strip().lower().split())

def _canon_constraint(c: Constraint) -> Tuple[str,str,str,str]:
    # structural canonical form: normalize key, keep operator, value as string representation, type
    key = c.key.strip().lower()
    op = c.operator
    ctype = c.type
    val = str(c.value)
    return (ctype, key, op, val)

def equivalent(uil1: Intent, uil2: Intent) -> bool:
    if uil1.type != uil2.type:
        return False
    if normalize_goal(uil1.goal) != normalize_goal(uil2.goal):
        return False
    if set(uil1.entities) != set(uil2.entities):
        return False
    s1 = set(_canon_constraint(c) for c in uil1.constraints)
    s2 = set(_canon_constraint(c) for c in uil2.constraints)
    return s1 == s2
