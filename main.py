from books import Biblioteca

if __name__ == "__main__":

    catalogo_biblioteca = [
        {"titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "ano": 1954},
        {"titulo": "1984", "autor": "George Orwell", "ano": 1949},
        {"titulo": "O Guia do Mochileiro das Galáxias", "autor": "Douglas Adams", "ano": 1979}
    ]

    biblioteca = Biblioteca()
    biblioteca.adicionar_catalogo(catalogo_biblioteca)

    biblioteca.listar_livros()

    biblioteca.adicionar_livro("A Hora da Estrela", "Clarice Lispector", 1977)
    biblioteca.listar_livros()

    biblioteca.buscar_livro_por_titulo("1984")
    biblioteca.buscar_livro_por_titulo("senhor")
    biblioteca.buscar_livro_por_titulo("harry potter")