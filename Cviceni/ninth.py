def dec_to_bin(cislo):
  
    cislo = int(cislo)
    
    if cislo == 0:
        return "0"
    
    
    binary = ""
    
    #
    while cislo > 0:
        
        binary = str(cislo % 2) + binary
        
        cislo //= 2
    
    return binary

def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"
    assert dec_to_bin(167) == "10100111"  