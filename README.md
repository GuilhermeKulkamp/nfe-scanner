# NFe Scanner

[![Project Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow.svg )](https://github.com/GuilhermeKulkamp/nfe-scaner )
[![License](https://img.shields.io/badge/License-MIT-blue.svg )](LICENSE)

## 🚀 Visão Geral

O **NFe Scanner** é um aplicativo desktop desenvolvido para automatizar o processo manual de arquivamento de Notas Fiscais Eletrônicas (NF-e) no site da SEFAZ. Nosso objetivo é eliminar a ineficiência e os erros de transcrição, fornecendo uma ferramenta rápida e confiável para a gestão de dados fiscais.

## ✨ Funcionalidades Principais (MVP)

- **Captura de Dados:** Leitura de NF-e via Chave de Acesso ou QR Code.
- **Raspagem Inteligente:** Utiliza Playwright para lidar com o JavaScript do site da SEFAZ.
- **Armazenamento Local:** Dados de NF-e e itens armazenados em um banco de dados SQLite (via SQLModel).
- **Consulta:** Filtros por data e empresa para gestão dos dados arquivados.

## 🛠️ Stack Tecnológica

| Categoria | Ferramentas |
| :--- | :--- |
| **Linguagem** | Python 3.12 |
| **Interface Gráfica** | PySimpleGUI |
| **Raspagem de Dados** | Playwright, Beautiful Soup |
| **Banco de Dados** | SQLite com SQLModel (ORM) |
| **Qualidade de Código** | Black, isort, Ruff |
| **Gerenciamento** | Poetry |

## ⚙️ Instalação e Setup

### Pré-requisitos

- Python 3.12
- Poetry (Gerenciador de Dependências)

### 1. Clonar o Repositório

\`\`\`bash
git clone https://github.com/GuilhermeKulkamp/nfe-scaner.git
cd nfe-scaner
\`\`\`

### 2. Instalar Dependências

Utilize o Poetry para criar o ambiente virtual e instalar todas as dependências:

\`\`\`bash
poetry install
\`\`\`

### 3. Configurar o Playwright

O Playwright requer a instalação dos *browsers* para funcionar:

\`\`\`bash
poetry run playwright install
\`\`\`

### 4. Executar o Aplicativo

(Ainda não implementado - será a Issue #5 )

## 🤝 Contribuição

Agradecemos o seu interesse em contribuir! Siga o nosso fluxo de trabalho:

1.  **Fork** o projeto.
2.  Crie uma nova *branch* para sua *feature* (`git checkout -b feat/minha-nova-feature`).
3.  Faça suas alterações e garanta que os testes estão passando.
4.  Crie um **Commit Semântico** (ex: `feat: adiciona tela de consulta`).
5.  Crie um **Pull Request (PR)** para a *branch* `main`.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.
