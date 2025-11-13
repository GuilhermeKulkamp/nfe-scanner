# Product Requirements Document (PRD) - Arquivamento de NF-e

## 1. Visão Geral e Problema

| Item | Descrição |
| :--- | :--- |
| **Problema Principal** | A dificuldade e o tempo gasto no processo manual de acesso, coleta e arquivamento de dados de Notas Fiscais Eletrônicas (NF-e) no site da SEFAZ. O processo atual é repetitivo, ineficiente e propenso a erros de transcrição. |
| **Usuários-Alvo** | Indivíduos ou pequenos negócios que precisam rastrear e arquivar dados de NF-e, atualmente utilizando um processo manual que envolve acesso ao site da SEFAZ e anotação dos dados em planilhas. |
| **Solução Proposta** | Desenvolver um aplicativo desktop com interface gráfica (GUI) que permite ao usuário inserir a chave de acesso ou ler o QR Code de uma NF-e. O aplicativo fará a "raspagem" (scraping) dos dados no site da SEFAZ, lidando com a execução de scripts JavaScript, e armazenará as informações de forma segura em um banco de dados local (SQLite). |

## 2. Objetivos e Métricas de Sucesso

| Item | Descrição |
| :--- | :--- |
| **Objetivos de Produto** | **1. Economia de Tempo:** Reduzir drasticamente o tempo que o usuário gasta no processo de arquivamento de NF-e. **2. Redução de Erros:** Eliminar os erros de digitação e transcrição associados ao processo manual. **3. Centralização de Dados:** Fornecer um repositório local e organizado para os dados das NF-e. |
| **Métricas de Sucesso** | **1. Performance de Arquivamento:** O tempo total para o arquivamento de uma NF-e (desde a entrada da chave/QR Code até o salvamento no banco de dados) deve ser **inferior a 20 segundos**. **2. Precisão de Dados:** O sistema deve ter **zero erros de digitação/transcrição** dos dados da NF-e, garantindo a fidelidade das informações extraídas. |

## 3. Requisitos Funcionais (O que o sistema deve fazer?)

| Categoria | História de Usuário |
| :--- | :--- |
| **Interface** | Como um usuário, eu quero ter uma interface gráfica intuitiva para escolher o método de entrada da NF-e (chave ou QR Code). |
| **Entrada de Dados (Chave)** | Como um usuário, eu quero digitar a chave de acesso da NF-e em um campo que garanta a formatação correta (grupos de 4 dígitos), para evitar erros de digitação. |
| **Entrada de Dados (QR Code)** | Como um usuário, eu quero que o programa leia o QR Code da nota fiscal, para que eu não precise digitar a chave de acesso. |
| **Tratamento de Erro (QR Code)** | Como um usuário, caso a leitura do QR Code falhe, eu quero ser informado da falha e ser direcionado para a opção de digitação da chave de acesso. |
| **Processamento** | Como um usuário, eu quero que o sistema acesse o site da SEFAZ, realize a raspagem dos dados da NF-e (incluindo itens) e os armazene no banco de dados local. |
| **Validação** | Como um usuário, eu quero que o sistema verifique se a NF-e já foi lida e arquivada, para evitar duplicidade de registros. |
| **Tratamento de Indisponibilidade** | Como um usuário, caso o site da SEFAZ esteja indisponível, eu quero ser informado imediatamente e que a data e hora da indisponibilidade sejam registradas para consulta posterior. |
| **Gestão de Dados** | Como um usuário, eu quero poder consultar as notas fiscais arquivadas, filtrando por data e por empresa (CNPJ/Razão Social). |
| **Análise de Itens** | Como um usuário, eu quero ter um banco de dados dos itens das notas, para que eu possa consultar por descrição e comparar preços, locais e datas de compra. |
| **Manutenção** | Como um usuário, eu quero poder excluir uma nota fiscal arquivada, caso seja necessário corrigir ou remover um registro. |
| **Anotações** | Como um usuário, eu quero poder incluir uma observação em uma nota fiscal que foi lida, para adicionar informações contextuais importantes. |

## 4. Requisitos Não-Funcionais (Como o sistema deve ser?)

| Item | Descrição |
| :--- | :--- |
| **Performance** | **Raspagem de Dados:** O processo de raspagem de dados no site da SEFAZ deve ser concluído em, no máximo, **20 segundos**. Caso esse tempo seja excedido, o sistema deve registrar a ocorrência como "site instável", anotando a data e hora da instabilidade para consulta futura. |
| **Usabilidade** | O aplicativo deve possuir uma Interface Gráfica de Usuário (GUI) intuitiva e de fácil compreensão, permitindo que **usuários leigos** possam utilizá-lo sem a necessidade de treinamento extensivo. |
| **Segurança** | O foco da segurança será na **integridade dos dados** armazenados localmente (SQLite) e na **proteção contra falhas** durante o processo de *scraping*. |
| **Plataforma** | O sistema será desenvolvido como um **aplicativo desktop** (multiplataforma, mas focado inicialmente em **Ubuntu** como ambiente de desenvolvimento). |
| **Arquitetura** | O projeto seguirá uma **estrutura base (padrão MVC simplificado)**, com separação clara entre a lógica da interface e as regras de negócio, para garantir baixo acoplamento. |

## 5. Fora do Escopo (Versão 1.0)

| Item | Descrição |
| :--- | :--- |
| **Sincronização** | Não haverá sincronização de dados com a nuvem ou qualquer serviço externo. O armazenamento será estritamente local (SQLite). |
| **Usuários** | Não haverá suporte para múltiplos usuários ou perfis de acesso. O aplicativo é destinado a um único usuário. |
| **Relatórios** | Não haverá geração de relatórios ou exportação de dados em formatos como PDF ou Excel. A visualização e consulta dos dados será feita exclusivamente através da interface do aplicativo. |
| **Backup** | Não haverá rotinas automáticas de backup do banco de dados local. O usuário será responsável por gerenciar o backup do arquivo SQLite. |
| **Outras Plataformas** | O foco inicial é um aplicativo desktop, sem planos para versões web ou mobile nesta versão. |

---

# Contexto Técnico e Metodologia

## Stack Técnica (A Stack)

| Categoria | Ferramentas |
| :--- | :--- |
| **Linguagem/Ambiente** | Python 3.12, VSCode 1.1 com Co-Pilot, SO Ubuntu. |
| **Raspagem de Dados** | Playwright (para lidar com JS) e Beautiful Soup. |
| **Interface Gráfica** | PySimpleGUI. |
| **Banco de Dados** | SQLite (local) com SQLModel (ORM). |
| **Leitura de QR Code** | OpenCV (`opencv-python`) e Pyzbar. |

## DevOps e Boas Práticas de Engenharia

| Categoria | Práticas e Ferramentas |
| :--- | :--- |
| **Gestão de Projetos** | GitHub Projects (Kanban: `Backlog`, `To Do`, `In Progress`, `Done`). |
| **Qualidade de Código** | Black, isort, Ruff (Formatação e Linting). |
| **Testes Automatizados** | pytest, Testes Unitários, Testes de Integração (scraper + DB), pytest-cov. |
| **Versionamento** | Commits Semânticos, GitHub Flow, Code Review. |
| **Gerenciamento de Dependências** | Poetry. |
| **Automação (CI/CD)** | GitHub Actions (rodar testes e linters a cada Pull Request). |
| **Documentação** | Docstrings (Google Style), MkDocs, README.md. |

## Estrutura de Projeto

*   **Padrão:** MVC simplificado.
*   **Princípios:** Separar lógica da interface (PySimpleGUI) e evitar acoplamento entre UI e regras de negócio.
