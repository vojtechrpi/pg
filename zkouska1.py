# Příklad 1: Práce s podmínkami a řetězci
# Zadání:
# Napište funkci `process_strings`, která přijme seznam řetězců. 
# Funkce vrátí nový seznam, který obsahuje pouze řetězce delší než 3 znaky, převedené na velká písmena.
# Pokud seznam obsahuje řetězec "STOP", ukončete zpracování seznamu a vraťte dosud vytvořený seznam.

def process_strings(strings):
    result = []  # Vytvořit prázdný seznam pro výsledky
    for string in strings:
        if string == "STOP":  # Zkontrolovat, zda je řetězec "STOP"
            break  # Ukončit zpracování
        if len(string) > 3:  # Zkontrolovat, zda je řetězec delší než 3 znaky
            result.append(string.upper())  # Převést na velká písmena a přidat do výsledků
    return result  # Vrátit výsledný seznam

# Pytest testy pro Příklad 2
def test_process_strings():
    assert process_strings(["abc", "abcd", "STOP", "efgh"]) == ["ABCD"]
    assert process_strings(["hello", "world", "STOP", "python"]) == ["HELLO", "WORLD"]
    assert process_strings(["hi", "ok", "go"]) == []
    assert process_strings(["code", "test", "debug"]) == ["CODE", "TEST", "DEBUG"]
