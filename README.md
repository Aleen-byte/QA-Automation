# QA Automation — Petstore API & SauceDemo Web

Projeto de automação de testes com cobertura de API REST e fluxo E2E web, integrado a pipelines de CI via GitHub Actions.

---

## 📁 Estrutura do Repositório

```
qa-automation/
├── api-tests/                  # Automação de API (Petstore)
│   ├── tests/
│   │   ├── test_pet.py
│   │   ├── test_store.py
│   │   └── test_user.py
│   ├── utils/
│   │   └── client.py
│   ├── conftest.py
│   ├── pytest.ini
│   └── requirements.txt
│
├── web-tests/                  # Automação Web (SauceDemo)
│   ├── pages/                  # Page Objects
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   ├── tests/
│   │   └── test_saucedemo.py
│   ├── utils/
│   │   └── driver_factory.py
│   ├── conftest.py
│   ├── pytest.ini
│   └── requirements.txt
│
└── .github/
    └── workflows/
        ├── api-tests.yml
        └── web-tests.yml
```

---

## 🛠️ Tecnologias Utilizadas

| Projeto     | Tecnologia         | Finalidade                        |
|-------------|--------------------|---------------------------------|
| API Tests   | Python 3.11        | Linguagem principal              |
| API Tests   | pytest             | Framework de testes              |
| API Tests   | requests           | Cliente HTTP                     |
| API Tests   | pytest-html        | Geração de relatórios            |
| Web Tests   | Selenium 4         | Automação de browser             |
| Web Tests   | webdriver-manager  | Gerenciamento do ChromeDriver    |
| CI/CD       | GitHub Actions     | Pipeline de integração contínua  |

---

## ⚙️ Instalação e Execução

### Pré-requisitos

- Python 3.11+
- Google Chrome instalado (para os testes web)
- pip

---

### 🔌 Testes de API (Petstore)

```bash
cd api-tests
pip install -r requirements.txt
pytest
```

O relatório HTML será gerado em `api-tests/report.html`.

---

### 🌐 Testes Web (SauceDemo)

```bash
cd web-tests
pip install -r requirements.txt
pytest
```

O relatório HTML será gerado em `web-tests/report.html`.

> Os testes rodam em modo **headless** por padrão. Para ver o browser abrir, edite `conftest.py` e altere `headless=True` para `headless=False`.

---

## 🧪 Cenários Cobertos

### API — Petstore (`https://petstore.swagger.io/v2`)

| Módulo | Cenário                                |
|--------|----------------------------------------|
| Pet    | Criar pet                              |
| Pet    | Buscar pet por ID                      |
| Pet    | Atualizar pet (PUT)                    |
| Pet    | Buscar pets por status                 |
| Pet    | Atualizar pet via form                 |
| Pet    | Upload de imagem do pet                |
| Pet    | Buscar pet inexistente (404)           |
| Pet    | Deletar pet                            |
| Store  | Consultar inventário                   |
| Store  | Realizar pedido                        |
| Store  | Buscar pedido por ID                   |
| Store  | Buscar pedido inexistente (404)        |
| Store  | Deletar pedido                         |
| Store  | Deletar pedido inexistente (404)       |
| User   | Criar usuário                          |
| User   | Criar usuários com lista               |
| User   | Criar usuários com array               |
| User   | Buscar usuário por username            |
| User   | Atualizar usuário                      |
| User   | Login                                  |
| User   | Logout                                 |
| User   | Buscar usuário inexistente (404)       |
| User   | Deletar usuário                        |

### Web — SauceDemo (`https://www.saucedemo.com`)

| Classe         | Cenário                                              |
|----------------|------------------------------------------------------|
| TestLogin      | Login com credenciais válidas                        |
| TestLogin      | Login com credenciais inválidas                      |
| TestLogin      | Login com usuário bloqueado                          |
| TestCart       | Adicionar um item ao carrinho                        |
| TestCart       | Adicionar múltiplos itens ao carrinho                |
| TestCart       | Verificar itens exibidos no carrinho                 |
| TestCheckout   | Fluxo E2E completo: login → produtos → checkout → confirmação |

---

## 🔄 CI/CD — GitHub Actions

As pipelines são disparadas automaticamente em **push** e **pull request** para as respectivas pastas, e podem ser executadas manualmente via `workflow_dispatch`.

| Workflow        | Arquivo                            | Trigger                    |
|-----------------|------------------------------------|---------------------------|
| API Tests       | `.github/workflows/api-tests.yml`  | Mudanças em `api-tests/`  |
| Web Tests       | `.github/workflows/web-tests.yml`  | Mudanças em `web-tests/`  |

Ao final de cada execução, o relatório HTML é salvo como **artifact** no GitHub Actions.

---

## 🎨 Design Patterns

- **Page Object Model (POM):** cada página da aplicação web é representada por uma classe em `pages/`, isolando os seletores e ações da lógica de teste.
- **Base Page:** classe pai com métodos reutilizáveis de interação com o Selenium (`find`, `click`, `type`, `get_text`).
- **Driver Factory:** criação do WebDriver centralizada em `utils/driver_factory.py`, facilitando a troca de browser ou configuração headless.
- **Client Wrapper:** cliente HTTP encapsulado em `utils/client.py`, reutilizado em todos os testes de API via fixture do pytest.
- **Fixtures com escopos:** fixture `client` com escopo `session` (uma instância por execução) e `driver` com escopo `function` (browser limpo por teste).
