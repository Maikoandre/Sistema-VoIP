# Sistema VoIP

Este projeto é uma plataforma de gestão de telefonia IP que integra o **Asterisk PBX** com um backend **Django**. O sistema permite a gestão de ramais via API e a originação de chamadas através de comandos AMI (*Asterisk Manager Interface*).

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3.12
* **Framework Web:** Django 6.0.3
* **API Toolkit:** Django REST Framework 3.16.1
* **Telefonia:** Asterisk PBX (configurações SIP, AMI e AGI)
* **Base de Dados:** SQLite

## 📂 Estrutura do Projeto

* **`/asterisk`**: Contém os ficheiros de configuração do Asterisk (`sip.conf`, `extensions.conf`, `manager.conf`) e scripts AGI.
* **`/backend`**: Core do sistema desenvolvido em Django, responsável pela API de gestão.
* **`/backend/ramais`**: Aplicação Django que gere o modelo de dados de extensões/ramais.




# ✅ Requisitos

Antes de começar, instale:

* Asterisk
  👉 https://www.asterisk.org/downloads/

* uv
  👉 https://docs.astral.sh/uv/

* Python 3.10+

* OpenSSL (já vem na maioria dos sistemas Linux)

---

# ⚙️ Instalação

## 1. Clonar o projeto

```bash
git clone <seu-repo>
cd <seu-repo>
```

---

## 2. Configurar variáveis de ambiente

Copie o arquivo de exemplo:

```bash
mv .env-example .env
```

Edite o `.env` com seu IP e domínio:

```bash
SERVER_HOST=192.168.0.0
SERVER=192.168.0.0/24
```

---

## 3. Deploy das configurações do Asterisk

Execute o script:

```bash
chmod +x ./asterisk/generate_keys.sh
sudo ./asterisk/generate_keys.sh
```

Esse script irá:

* Copiar arquivos `.conf` para `/etc/asterisk`
* Substituir variáveis `${ENV}`
* Gerar certificados TLS

---

## 4. Iniciar o Asterisk

```bash
sudo asterisk -cvvv
```
- Na CLI do Asterisk, rode:
```CLI
core restart now
```
---


Antes de usar o sistema:

👉 Acesse no navegador e aceite o certificado:

```
https://SEU_IP:8089/ws
```

Exemplo:

```
https://192.168.0.137:8089/ws
```


---

# 🌐 Rodando o Django

Instale dependências:

```bash
uv sync
```

Execute o servidor:

```bash
uv run python manage.py runserver_plus --cert-file cert.crt 0.0.0.0:8000
```

---

# 🚀 Acessar o sistema

Depois de aceitar o certificado do Asterisk:

👉 Acesse:

```
https://SEU_IP:8000
```

---

# 👤 Ramais disponíveis

| Ramal | Senha |
| ----- | ----- |
| 1001  | 1234  |
| 1002  | 1234  |
| 1003  | 1234  |
| 1004  | 1234  |
| 1005  | 1234  |

---


