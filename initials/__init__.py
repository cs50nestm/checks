import check50
import check50.c
import re

@check50.check()
def exists():
    """initials.c exists."""
    check50.exists("initials.c")

@check50.check(exists)
def compiles():
    """initials.c compiles."""
    check50.c.compile("initials.c", lcs50=True)

@check50.check(compiles)
def uppercase():
    """Outputs HLJ for Hailey Lynn James"""
    check50.run("./initials").stdin("Hailey Lynn James").stdout(match("Initials: HLJ"), "HLJ\n").exit(0)

@check50.check(compiles)
def lowercase():
    """Outputs HLJ for hailey lynn james"""
    check50.run("./initials").stdin("hailey lynn james").stdout(match("Initials: HLJ"), "HLJ\n").exit(0)

@check50.check(compiles)
def mixed_case():
    """Outputs HJ for hailey James"""
    check50.run("./initials").stdin("hailey James", prompt=False).stdout(match(Initials: "HJ"), "HJ\n").exit(0)

@check50.check(compiles)
def all_uppercase():
    """Outputs B for BRIAN"""
    check50.run("./initials").stdin("BRIAN", prompt=False).stdout(match("Initials: B"), "B\n").exit(0)

def match(initials):
    return "^(.*\n)?{}\n".format(initials)
