def bin_to_dec(binarni_cislo):
    bin_str = str(binarni_cislo)
    vysledek = 0
    for i, bit in enumerate(reversed(bin_str)):
        if bit == '1':
            vysledek += 2 ** i
    return vysledek


def test_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128

    #1101   = 1*(2^3) + 1*(2^2) + 0*(2^1) + 1*(2^0)
    #       = 1*8 + 1*4 + 0*2 + 1*1 
      #      = 8 + 4 + 0 + 1 
    #      = 13


if __name__ == "__main__":
    # Test konkrétního čísla
    print(f"10011101 -> {bin_to_dec('10011101')}")  # Mělo by vypsat 157
    print(f"010101 -> {bin_to_dec('010101')}")  # Mělo by vypsat 21
    
    # Spustíme testy
    test_funkce()
    print("Testy proběhly úspěšně")