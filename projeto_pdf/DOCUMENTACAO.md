# Documentação do Conversor PDF/DOCX para TXT

## 📋 Visão Geral
Programa em Python que converte arquivos PDF ou DOCX em arquivo TXT extraindo o texto.

---

## 🔧 Funções

### 1. Função `convert_pdf_to_text()`

| Aspecto | Descrição |
|--------|-----------|
| **Nome** | `convert_pdf_to_text` |
| **Parâmetro 1** | `pdf_path: Path` |
| **Parâmetro 2** | `txt_path: Path` |
| **Retorno** | `None` |
| **Descrição** | Lê um arquivo PDF e extrai todo o texto em um arquivo TXT |
| **Exceção** | `RuntimeError` - Se houver erro ao extrair texto |

#### Fluxo Interno

| Etapa | Ação |
|-------|------|
| 1 | Cria um objeto `PdfReader` a partir do arquivo PDF |
| 2 | Itera sobre todas as páginas do PDF |
| 3 | Extrai o texto de cada página |
| 4 | Combina todo o texto com quebras de linha duplas |
| 5 | Escreve o resultado no arquivo TXT com codificação UTF-8 |

---

### 2. Função `convert_docx_to_text()`

| Aspecto | Descrição |
|--------|-----------|
| **Nome** | `convert_docx_to_text` |
| **Parâmetro 1** | `docx_path: Path` |
| **Parâmetro 2** | `txt_path: Path` |
| **Retorno** | `None` |
| **Descrição** | Lê um arquivo DOCX e extrai texto + tabelas |
| **Exceção** | `RuntimeError` - Se `python-docx` não estiver instalado |

#### Fluxo Interno

| Etapa | Ação |
|-------|------|
| 1 | Valida se a biblioteca `docx` está disponível |
| 2 | Carrega o documento DOCX |
| 3 | Extrai texto de todos os parágrafos |
| 4 | Extrai conteúdo de todas as tabelas (com tabulações) |
| 5 | Combina todo o conteúdo com quebras duplas |
| 6 | Escreve no arquivo TXT com codificação UTF-8 |

---

### 3. Função `main()`

| Aspecto | Descrição |
|--------|-----------|
| **Nome** | `main` |
| **Parâmetros** | Nenhum (lê argumentos da linha de comando) |
| **Retorno** | `int` - Código de saída (0 = sucesso, 1 = erro) |
| **Descrição** | Função principal que orquestra o processo |

#### Argumentos de Linha de Comando

| Argumento | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `input_file` | string | ✅ Sim | Caminho do arquivo PDF ou DOCX |
| `txt_file` | string | ❌ Não | Caminho do arquivo TXT de saída (opcional) |

#### Fluxo do `main()`

| Etapa | Ação | Código de Saída |
|-------|------|-----------------|
| 1 | Parse dos argumentos CLI | - |
| 2 | Valida se arquivo de entrada existe | 1 se não existe |
| 3 | Valida se extensão é `.pdf` ou `.docx` | 1 se inválida |
| 4 | Define caminho do arquivo de saída | - |
| 5 | Chama função de conversão apropriada | - |
| 6 | Exibe mensagem de sucesso | 0 |
| 7 | Captura exceções e exibe erro | 1 |

---

## 📦 Dependências

| Biblioteca | Importação | Obrigatória | Uso |
|-----------|-----------|------------|-----|
| `PyPDF2` | `from PyPDF2 import PdfReader` | ✅ Sim | Extração de texto de PDFs |
| `python-docx` | `import docx` | ❌ Não | Extração de texto de DOCX |
| `argparse` | `import argparse` | ✅ Sim | Parse de argumentos CLI |
| `sys` | `import sys` | ✅ Sim | Controle de saída do programa |
| `pathlib` | `from pathlib import Path` | ✅ Sim | Manipulação de caminhos |

---

## 🚀 Casos de Uso

| Caso | Comando | Resultado |
|------|---------|-----------|
| Converter PDF com nome automático | `python main.py arquivo.pdf` | Cria `arquivo.txt` |
| Converter PDF com nome customizado | `python main.py arquivo.pdf output.txt` | Cria `output.txt` |
| Converter DOCX com nome automático | `python main.py documento.docx` | Cria `documento.txt` |
| Converter DOCX com nome customizado | `python main.py documento.docx saida.txt` | Cria `saida.txt` |

---

## ⚠️ Tratamento de Erros

| Situação | Mensagem | Código |
|----------|----------|--------|
| PyPDF2 não instalado | "Erro: a biblioteca PyPDF2 não está instalada..." | 1 |
| Arquivo de entrada não existe | "Erro: arquivo de entrada não encontrado..." | 1 |
| Extensão inválida | "Erro: o arquivo de entrada deve ser um PDF ou DOCX..." | 1 |
| python-docx não instalado (DOCX) | "Erro: a biblioteca python-docx não está instalada..." | 1 |
| Erro na extração de PDF | "Erro ao converter {arquivo} para TXT: ..." | 1 |
| Conversão bem-sucedida | "Conversão concluída: {arquivo}" | 0 |

---

## 💾 Estrutura de Dados

| Variável | Tipo | Escopo | Descrição |
|----------|------|--------|-----------|
| `text_lines` | `list[str]` | Local | Acumula linhas de texto extraído |
| `reader` | `PdfReader` | Local | Objeto leitor de PDF |
| `document` | `Document` | Local | Objeto documento DOCX |
| `input_path` | `Path` | Local | Caminho do arquivo de entrada |
| `txt_path` | `Path` | Local | Caminho do arquivo de saída |
| `extension` | `str` | Local | Extensão do arquivo (`.pdf` ou `.docx`) |

---

## 🔄 Fluxograma Geral

```
Início
   ↓
Parse Argumentos CLI
   ↓
Arquivo existe?
   ├─ Não → Erro (código 1)
   ↓ Sim
Extensão válida? (.pdf ou .docx)
   ├─ Não → Erro (código 1)
   ↓ Sim
Extensão é .pdf?
   ├─ Sim → convert_pdf_to_text()
   ├─ Não → convert_docx_to_text()
   ↓
Conversão bem-sucedida?
   ├─ Não → Exibe erro (código 1)
   ↓ Sim
Sucesso (código 0)
   ↓
Fim
```
