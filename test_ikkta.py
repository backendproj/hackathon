from  ikkta_birxil import main

def test_main():
    assert main("somsa") == "1om1a"
    assert main("qaymoq") == "1aymo1"
    assert main("gozaaaal") == "goz1111l"
    assert main("sharshara") == "1har1hara"
    assert main("sigir") == "s1g1r"

