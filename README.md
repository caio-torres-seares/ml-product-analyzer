# 📊 WebScraping Mercado Livre - Celulares

## O que é este projeto?
Este projeto é uma solução completa para coleta, tratamento e visualização de dados de celulares vendidos no Mercado Livre Brasil. Ele automatiza o processo de extração de informações como marca, modelo, preço, avaliações e quantidade de reviews dos produtos, permitindo análises de mercado de forma rápida e visual.

## Tecnologias Utilizadas
- **Python 3**
- **Scrapy**: Para web scraping dos dados diretamente do Mercado Livre.
- **Pandas**: Para tratamento, limpeza e transformação dos dados extraídos.
- **SQLite**: Para armazenamento local dos dados tratados.
- **Streamlit**: Para criação de um dashboard interativo de visualização dos dados.

## Como rodar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/WebScraping-MercadoLivre.git
cd WebScraping-MercadoLivre
```

### 2. Instale as dependências
Recomenda-se o uso de um ambiente virtual:
```bash
python -m venv venv
# Ative o ambiente virtual:
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
pip install scrapy pandas streamlit
```

### 3. Execute o Web Scraping
```bash
cd src/extraction
scrapy crawl phone -o ../../data/data.jsonl
```
Isso irá coletar os dados das primeiras 10 páginas de celulares no Mercado Livre e salvar em `data/data.jsonl`.

### 4. Transforme e carregue os dados
```bash
cd ../../transform
python transform.py
```
Os dados tratados serão salvos em `data/phones.db`.

### 5. Visualize no Dashboard
```bash
cd ../dashboard
streamlit run app.py
```
Acesse o endereço exibido pelo Streamlit para visualizar os KPIs, gráficos de marcas, preços e avaliações.

---

Sinta-se à vontade para adaptar o projeto para outros produtos ou análises!
