import check50
import check50.c


@check50.check()
def exists(self):
    """bubble.c exists."""
    check50.exists("bubble.c")

    
@check50.check(exists)
def compiles(self):
    """bubble.c compiles."""
     check50.c.compile("bubble.c", lcs50=True)

        
@check50.check(compiles)
def sorts():
    """sorts {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}"""
    check50.run("./bubble").stdout("0 1 2 3 4 5 6 7 8 9 \n").exit(0)
