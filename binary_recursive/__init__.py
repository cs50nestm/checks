import check50
import check50.c


@check50.check()
def exists():
    """binary.c exists"""
    check50.exists("binary.c")

      
@check50.check(exists)
def compiles():
    """binary.c compiles"""
    check50.c.compile("binary.c", lcs50=True)
             
             
@check50.check(compiles)
def finds_2():
    """binary search finds 2"""
    check50.run("./binary").stdin("2").stdout("Found\n").exit(0)

    
@check50.check(compiles)
def finds_14():
    """binary search finds 10"""
    check50.run("./binary").stdin("10").stdout("Found\n").exit(0)

    
@check50.check(compiles)
def finds_9():
    """binary search does not fine 33"""
    check50.run("./binary").stdin("33").stdout("Not found!\n").exit(0)
