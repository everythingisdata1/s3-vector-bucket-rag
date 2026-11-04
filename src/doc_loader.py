def loal_docs():
    print("Loading documents.....")

    with open(".././data/finance.txt", encoding="utf-8") as data:
        txt = data.read()

    docs = [doc.strip()
            for doc in txt.split("\n\n")
            if doc.strip()
            ]

    print(f"Document loaded.. {len(docs)}")

    return docs
