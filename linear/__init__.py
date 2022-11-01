import check50
import check50.c


@check50.check()
def exists():
    """linear.c exists"""
    check50.exists("linear.c")

    
@check50.check(exists)
def compiles():
    """linear.c compiles"""
    check50.c.compile("linear.c", lcs50=True)

    
@check50.check(compiles)
def finds_22:
    """linear search finds 22"""
    check50.run("./linear").stdin("22").stdout("Found your number! Bingo!\n").exit(0)

    
@check50.check(compiles)
def finds_7:
    """linear search finds 22"""
    check50.run("./linear").stdin("7").stdout("Found your number! Bingo!\n").exit(0)
    
@check50.check(compiles)
def finds_64:
    """linear search finds 22"""
    check50.run("./linear").stdin("64").stdout("Found your number! Bingo!\n").exit(0)
    
    
@check50.check(compiles)
def does_not_find_50:
    """linear search does not find 50"""
    check50.run("./linear").stdin("64").stdout("Sorry better luck next time!\n").exit(0)
