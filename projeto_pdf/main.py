import argparse
import sys
from pathlib import Path

try:
    from PyPDF2 import PdfReader
except ImportError:
    print("Erro: a biblioteca PyPDF2 não está instalada. Instale com: pip install PyPDF2")
    sys.exit(1)


def convert_pdf_to_text(pdf_path: Path, txt_path: Path) -> None:
    reader = PdfReader(str(pdf_path))

    text_lines = []
    for page_number, page in enumerate(reader.pages, start=1):
        try:
            page_text = page.extract_text() or ""
        except Exception as exc:
            raise RuntimeError(f"Falha ao extrair texto da página {page_number}: {exc}") from exc
        text_lines.append(page_text)

    txt_path.write_text("\n\n".join(text_lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Converte um arquivo PDF em um arquivo TXT de texto extraído."
    )
    parser.add_argument("pdf_file", help="Caminho do arquivo PDF de entrada")
    parser.add_argument(
        "txt_file",
        nargs="?",
        help="Caminho do arquivo TXT de saída (opcional). Se omitido, usa mesmo nome do PDF.",
    )
    args = parser.parse_args()

    pdf_path = Path(args.pdf_file)
    if not pdf_path.exists():
        print(f"Erro: arquivo PDF não encontrado: {pdf_path}")
        return 1
    if pdf_path.suffix.lower() != ".pdf":
        print(f"Erro: o arquivo de entrada deve ser um PDF. Arquivo informado: {pdf_path}")
        return 1

    txt_path = Path(args.txt_file) if args.txt_file else pdf_path.with_suffix(".txt")
    try:
        convert_pdf_to_text(pdf_path, txt_path)
    except Exception as exc:
        print(f"Erro ao converter PDF para TXT: {exc}")
        return 1

    print(f"Conversão concluída: {txt_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())