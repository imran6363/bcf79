from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import track
import socket, requests, time, os

console = Console()

USERNAME = "admin"
PASSWORD = "1234"

def login():
    user = input("Username: ")
    pw = input("Password: ")
    if user == USERNAME and pw == PASSWORD:
        console.print("[green]Access Granted ✔[/green]")
        time.sleep(1)
    else:
        console.print("[red]Access Denied ❌[/red]")
        exit()

def intro():
    os.system("clear")
    console.print("[green]Initializing system...[/green]")
    for i in track(range(20), description="Bypassing security..."):
        time.sleep(0.05)
    console.print("[bold green]ACCESS GRANTED ✔[/bold green]")
    console.print("[cyan]Creator: Imran[/cyan]")
    time.sleep(1)

def banner():
    os.system("clear")
    console.print(Panel.fit(
        "[bold green]BANGLADESH CYBER FORCE 79[/bold green]\n"
        "[white]Cyber Intelligence Tool[/white]\n"
        "[yellow]━━━━━━━━━━━━━━━━━━━━[/yellow]\n"
        "[cyan]👑 Creator: Imran[/cyan]",
        border_style="green"
    ))

def save(data):
    with open("results.txt","a") as f:
        f.write(data+"\n"+"="*40+"\n")

def ip_info():
    ip = Prompt.ask("Enter IP")
    res = requests.get(f"http://ip-api.com/json/{ip}").json()
    out=""
    for k,v in res.items():
        console.print(f"{k}: {v}")
        out += f"{k}: {v}\n"

    lat=res.get("lat")
    lon=res.get("lon")
    if lat and lon:
        link=f"https://maps.google.com/?q={lat},{lon}"
        console.print(f"[cyan]Map:[/cyan] {link}")
        out+=link

    save(out)

def website():
    site = Prompt.ask("Enter website")
    ip = socket.gethostbyname(site)
    console.print(f"IP: {ip}")
    save(f"{site} -> {ip}")

def port():
    target = Prompt.ask("Enter IP")
    txt=""
    for p in range(1,101):
        s=socket.socket()
        s.settimeout(0.3)
        if s.connect_ex((target,p))==0:
            console.print(f"[red]OPEN {p}")
            txt+=f"{p} open\n"
        s.close()
    save(txt)

def whois():
    d = Prompt.ask("Domain")
    data=os.popen(f"whois {d}").read()
    console.print(data[:1000])
    save(data)

def menu():
    console.print("""
[green]
1 → IP Info
2 → Website Info
3 → Port Scan
4 → WHOIS
5 → Exit
[/green]
""")

def main():
    login()
    intro()
    while True:
        banner()
        menu()
        c=Prompt.ask("Select")

        if c=="1": ip_info()
        elif c=="2": website()
        elif c=="3": port()
        elif c=="4": whois()
        elif c=="5": break

        input("Enter...")

if __name__=="__main__":
    main()
