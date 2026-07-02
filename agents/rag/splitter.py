class TextSplitter:

    def split(

        self,

        documents,

        chunk_size=1000,

        overlap=200,
    ):

        chunks = []

        for document in documents:

            start = 0

            while start < len(document):

                chunks.append(

                    document[
                        start:start + chunk_size
                    ]
                )

                start += chunk_size - overlap

        return chunks