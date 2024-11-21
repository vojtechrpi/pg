import sys
import requests
from bs4 import BeautifulSoup


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []
    
    try:
        # Stažení webové stránky
        response = requests.get(url)
        
        # Kontrola status kódu
        if response.status_code != 200:
            raise Exception(f"Chyba při stahování stránky: HTTP {response.status_code}")
        
        # Parsování HTML pomocí BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Nalezení všech odkazů (tagů <a>)
        for a_tag in soup.find_all('a'):
            href = a_tag.get('href')
            if href:
                # Přidání odkazu do seznamu, pokud není None
                hrefs.append(href)
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Chyba při připojení k URL: {e}")
    except Exception as e:
        raise Exception(f"Neočekávaná chyba: {e}")

    return hrefs


if __name__ == "__main__":
    try:
        # Kontrola, zda byl zadán argument s URL
        if len(sys.argv) < 2:
            raise Exception("Není zadána URL adresa")
        
        url = sys.argv[1]
        all_hrefs = download_url_and_get_all_hrefs(url)
        
        # Výpis nalezených odkazů
        print("Nalezené odkazy:")
        for href in all_hrefs:
            print(href)
            
    except Exception as e:
        print(f"Program skoncil chybou: {e}")