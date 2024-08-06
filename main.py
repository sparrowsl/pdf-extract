import os
import shutil
from pathlib import Path

from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError

books_path = "./books"
defects_path = "./defects"
renames_path = "./renames"


for p in Path().glob(f"{books_path}/*.pdf"):
    try:
        meta = PdfReader(f"{books_path}/{p.name}").metadata

        if meta and meta.title:
            print("===========")
            print(meta.title)
            print("===========")

            if not Path(renames_path).exists():
                os.mkdir(renames_path)

            ext = p.name.split(".")[-1]
            shutil.move(
                f"{books_path}/{p.name}",
                f"{renames_path}/{meta.title}.{ext}",
            )

    except PdfReadError as e:
        if not Path(defects_path).exists():
            os.mkdir(defects_path)

        shutil.move(
            f"{books_path}/{p.name}",
            f"{defects_path}/{p.name}",
        )
        print("Error:", e, p.name)
    finally:
        continue

    # for page in reader.pages[:2]:
    #     text = page.extract_text(0)
    #     if text.strip() == "":
    #         continue

    #     title += f"{text}\n"
    # print(title)
    # except FileNotFoundError:
    #     print(f"{p.name} was not found...")
    #     continue
    # except PdfReadError as e:
    #     print(e)

    # print(f"========= New Title for {p.name} =============")
    # print(title)
