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
<!-- 
## 🛠️ Configuração do Sistema

### 1. Requisitos
Certifique-se de que tem o Python 3.12 instalado. As dependências podem ser geridas através do ficheiro `pyproject.toml`.

### 2. Backend (Django)
Para iniciar o servidor de desenvolvimento:
```bash
cd backend
python manage.py migrate
python manage.py runserver
```
* **Endpoint de Ramais:** `GET /api/extensions/` para listar ou criar novos ramais.
* **Originação de Chamada:** `POST /api/make-call/` enviando os campos `from` e `to` no corpo da requisição.

### 3. Asterisk
Os ficheiros no diretório `/asterisk` devem ser integrados na configuração do seu servidor Asterisk:
* **`sip.conf`**: Define os ramais SIP (ex: 1001, 1002).
* **`extensions.conf`**: Define o plano de discagem (*dialplan*) interno.
* **`manager.conf`**: Configura o utilizador administrativo para que o Django possa disparar chamadas via AMI.

## 📞 Funcionalidades Implementadas

* **Gestão de Ramais:** Cadastro de números e senhas na base de dados através da API.
* **Integração AGI:** O script `call_handler.py` permite que o Asterisk realize consultas externas via HTTP durante uma chamada.
* **Chamadas via API:** Endpoint que utiliza o protocolo AMI para conectar dois canais automaticamente. -->