# Conversor PDF para TXT

Este pequeno utilitário converte um arquivo PDF em um arquivo de texto (`.txt`) usando a biblioteca `PyPDF2`.

## Requisitos

- Python 3.8+
- `PyPDF2`

## Instalação

```bash
pip install PyPDF2
```

## Uso

Execute o script `main.py` passando o caminho do PDF de entrada.

```bash
python main.py arquivo.pdf
```

Por padrão, o texto extraído será salvo em um arquivo com o mesmo nome e extensão `.txt`.

### Especificar arquivo de saída

```bash
python main.py arquivo.pdf saida.txt
```

## Exemplo

```bash
python main.py documento.pdf documento.txt
```

## Observações

- O script extrai texto de cada página do PDF e junta com quebras de linha duplas.
- Caso o PDF não contenha texto pesquisável, a extração pode produzir saída vazia ou incompleta.

## Passo a passo após a execução

1. Verifique a mensagem no terminal para confirmar que a conversão foi concluída.
2. Abra o arquivo `.txt` gerado no editor de texto de sua preferência.
3. Revise o texto extraído para corrigir eventuais quebras de linha ou caracteres estranhos.
4. Se precisar, copie o conteúdo para outro documento ou processe com outra ferramenta.
5. Se quiser repetir a conversão, execute novamente com outro PDF ou arquivo de saída diferente.
