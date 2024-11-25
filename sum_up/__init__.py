import check50
import check50.c


@check50.check()
def exists():
    """sumup.c exists"""
    check50.exists("sumup.c")

      
@check50.check(exists)
def compiles():
    """sumup.c compiles"""
    check50.c.compile("sumup.c", lcs50=True)
             
             
@check50.check(compiles)
def sums_to_5():
    """sumup sums to 5"""
    check50.run("./sumup").stdin("5").stdout("The sum from 1 to 5 is 15").exit(0)

    
@check50.check(compiles)
def sums_to_10():
    """sumup sums to 10"""
    check50.run("./sumup").stdin("19").stdout("The sum from 1 to 10 is 55").exit(0)

  
