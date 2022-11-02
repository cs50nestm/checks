import check50
import check50.c


@check50.check()
def exists(self):
    """bubble.c exists."""
    check50.exists("bubble.c")

    
@check50.check(exists)
def compiles(self):
    """bubble.c compiles."""
     check50.c.compile("bubble.c", lcs50=True).exit(0)

        
@check50.check(compiles)
def sorts():
    """sorts {64, 34, 25, 12, 22, 11, 90}"""
    check50.run("./bubble").stdout("11 12 22 25 34 64 90 \n").exit(0)
