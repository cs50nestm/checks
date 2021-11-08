import check50
import check50.c
import re


@check50.check()
def exists():
    """linear.c exists"""
    check50.exists("linear.c")

@check50.check(exists)
def compiles():
  """linear.c compiles"""
  check50.c.compile("linear.c", lcs50=True)

@check("compiles")
def test_handles_addition(self):
  """linear search finds Malan"""
  self.spawn("./linear").stdin("Malan").stdout("Calling Malan\n").exit(0)

@check("compiles")
def test_handles_subtraction(self):
  """linear search finds Smith"""
  self.spawn("./linear").stdin("Smith").stdout("Calling Smith\n").exit(0)

@check("compiles")
def test_handles_division(self):
  """linear search does not fine Tanzosh"""
  self.spawn("./linear").stdin("Tanzosh").stdout("Quitting\n").exit(0)
