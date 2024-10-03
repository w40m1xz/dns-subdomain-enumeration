import dns.resolver
import dns.exception

def enumerar(dominio, wordlist):
    resolver = dns.resolver.Resolver()
    resolver.timeout = 1
    resolver.lifetime = 1

    for cada_subdominio in wordlist:
        cada_subdominio = cada_subdominio.strip()

        if not cada_subdominio:
            continue

        try:
            subdominio_completo = f"{cada_subdominio}.{dominio}"
            resolver.resolve(subdominio_completo)
            print(f"Subdominio encontrado: {subdominio_completo}")
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            continue
        except Exception:
            print(f"Error al consultar {subdominio_completo}")

if __name__ == "__main__":
    dominio = "google.es"

    try:
        with open("subdomains-top1million-20000.txt", "r") as file:
            wordlist = file.readlines()
    except FileNotFoundError:
        print("El archivo 'subdomains-top1million-20000.txt' no se encuentra.")
        exit(1)

    enumerar(dominio, wordlist)
