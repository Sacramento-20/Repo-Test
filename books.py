class Biblioteca:

    def __init__(self, catalogo_biblioteca=None):
        self.catalogo_biblioteca = catalogo_biblioteca or []

    def adicionar_catalogo(self, catalogo):
        self.catalogo_biblioteca.extend(catalogo)

    def adicionar_livro(self, titulo, autor, ano):
        novo_livro = {"titulo": titulo, "autor": autor, "ano": ano}
        self.catalogo_biblioteca.append(novo_livro)
        print(f"Livro '{titulo}' adicionado com sucesso!")

    def listar_livros(self):
        if not self.catalogo_biblioteca:
            print("A biblioteca está vazia.")
        else:
            print("\n--- Catálogo da Biblioteca ---")
            for livro in self.catalogo_biblioteca:
                print(f"Título: {livro['titulo']} | Autor: {livro['autor']} | Ano: {livro['ano']}")

    def buscar_livro_por_titulo(self, titulo):
        encontrados = [livro for livro in self.catalogo_biblioteca if titulo.lower() in livro['titulo'].lower()]

        if not encontrados:
            print(f"Nenhum livro encontrado com o título '{titulo}'.")
        else:
            print(f"\n--- Livros encontrados com o título '{titulo}' ---")
            for livro in encontrados:
                print(f"Título: {livro['titulo']} | Autor: {livro['autor']} | Ano: {livro['ano']}")
            print("-" * 45)