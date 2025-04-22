FIAP - Faculdade de Informática e Administração Paulista  

Nome do projeto: 🌿 Capítulo 06 - Sistema de Cultivo Indoor com Python & Oracle  

Nome do grupo:  

👨‍🎓 Integrantes:  

Thomaz Requena  

👩‍🏫 Professores:  
Tutor(a)  
Nome do Tutor  
Coordenador(a)  
Nome do Coordenador  

# 🌿 Capítulo 06 - Sistema de Cultivo Indoor com Python & Oracle

Este projeto faz parte do **Capítulo 06** do curso, abordando um sistema completo para controle de **fases de cultivo indoor de cannabis**. A solução inclui cadastro, monitoramento e checklist automatizado de parâmetros de cultivo utilizando **Python** com **banco de dados Oracle**.

## 🔗 Repositório
Acesse o projeto: [github.com/thomazrequena/cap06_Python](https://github.com/thomazrequena/cap06_Python)

---

## 🎯 Objetivo

Criar um sistema de apoio ao **cultivo indoor automatizado**, com funcionalidades para:

- Cadastrar fases do ciclo de cultivo (germinação, vegetativo, floração, etc.)
- Registrar parâmetros ideais e atuais (umidade, temperatura, nutrientes, luz)
- Monitorar e validar esses parâmetros
- Sugerir ajustes automaticamente por meio de um **checklist inteligente**

---

## 🧩 Funcionalidades

### 🔧 CRUD de Fases de Cultivo (`Cap06_CrudFases.py`)
- Cadastra, edita e remove fases de cultivo
- Define parâmetros ideais por fase (ex: umidade mínima e máxima, nutrientes)

### 📋 Monitoramento de Parâmetros
- Registra os parâmetros ambientais **atuais**
- Compara os valores monitorados com os ideais
- Aciona automaticamente o checklist se houver divergências

### ✅ Checklist Automatizado (`Cap06_Checklist.py`)
- Valida os parâmetros coletados
- Gera orientações para ajustes quando detecta valores fora do ideal

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Oracle Database** (Conexão via `oracledb`)
- **PL/SQL** para estruturação das tabelas
- Execução local via terminal ou IDE

---

## 🗃️ Estrutura do Banco de Dados

### 📄 Tabela: `FASES_CULTIVO`
Contém os parâmetros ideais de cultivo para cada fase.

### 📄 Tabela: `MONITORAMENTO_PARAMETROS`
Registra os valores ambientais monitorados periodicamente, com data/hora.

---

## ▶️ Como Executar o Projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/thomazrequena/cap06_Python.git
   cd cap06_Python
