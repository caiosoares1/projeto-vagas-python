import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_fake_jobs():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Erro ao acessar o site: {response.status_code}")
        return pd.DataFrame()

    soup = BeautifulSoup(response.text, "html.parser")
    job_elements = soup.find_all("div", class_="card-content")

    vagas = []
    for job_elem in job_elements:
        titulo = job_elem.find("h2", class_="title")
        empresa = job_elem.find("h3", class_="company")
        local = job_elem.find("p", class_="location")
        link_elem = job_elem.find("a", text="Apply")

        vagas.append({
            "titulo": titulo.text.strip() if titulo else "",
            "empresa": empresa.text.strip() if empresa else "",
            "local": local.text.strip() if local else "",
            "link": link_elem["href"] if link_elem else ""
        })

    return pd.DataFrame(vagas)

if __name__ == "__main__":
    df = get_fake_jobs()

    if df.empty:
        print("⚠️ Nenhuma vaga encontrada!")
    else:
        df.to_csv("vagas_fake.csv", index=False)
        print(f"✅ {len(df)} vagas salvas em 'vagas_fake.csv'")
