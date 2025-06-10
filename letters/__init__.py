import check50


@check50.check()
def exists():
    """letters.py exists"""
    check50.exists("letters.py")

@check50.check(exists)
def test5():
    """input of hello yields output of 5"""
    check50.run("python3 letters.py").stdin("hello").stdout("Letters: 5").exit()
