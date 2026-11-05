from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.clients import SEP


def load_docs():
    print(SEP + " Loading documents " + SEP)

    with open("../data/data.txt", encoding="utf-8") as data:
        txt = data.read()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", ". ", " ", ""],
        length_function=len,
        strip_whitespace=True
    )
    chucks = splitter.split_text(txt)

    print(f"Document loaded.. {len(chucks)}")

    return chucks


if __name__ == '__main__':
    load_docs()
