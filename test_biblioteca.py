import pytest
from io import StringIO
import sys
from books import Biblioteca


class TestBiblioteca:
    """Testes para a classe Biblioteca utilizando pytest"""
    
    def setup_method(self):
        """Setup executado antes de cada teste"""
        self.biblioteca = Biblioteca()
        self.catalogo_exemplo = [
            {"titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "ano": 1954},
            {"titulo": "1984", "autor": "George Orwell", "ano": 1949},
            {"titulo": "O Guia do Mochileiro das Galáxias", "autor": "Douglas Adams", "ano": 1979}
        ]
    
    def test_init_biblioteca_vazia(self):
        """Testa inicialização de biblioteca vazia"""
        biblioteca = Biblioteca()
        assert biblioteca.catalogo_biblioteca == []
    
    def test_init_biblioteca_com_catalogo(self):
        """Testa inicialização de biblioteca com catálogo"""
        biblioteca = Biblioteca(self.catalogo_exemplo)
        assert biblioteca.catalogo_biblioteca == self.catalogo_exemplo
        assert len(biblioteca.catalogo_biblioteca) == 3
    
    def test_adicionar_catalogo(self):
        """Testa adição de catálogo à biblioteca"""
        self.biblioteca.adicionar_catalogo(self.catalogo_exemplo)
        assert len(self.biblioteca.catalogo_biblioteca) == 3
        assert self.biblioteca.catalogo_biblioteca == self.catalogo_exemplo
    
    def test_adicionar_catalogo_vazio(self):
        """Testa adição de catálogo vazio"""
        self.biblioteca.adicionar_catalogo([])
        assert self.biblioteca.catalogo_biblioteca == []
    
    def test_adicionar_catalogo_existente(self):
        """Testa adição de catálogo a biblioteca que já possui livros"""
        self.biblioteca.adicionar_catalogo(self.catalogo_exemplo)
        catalogo_adicional = [
            {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899}
        ]
        self.biblioteca.adicionar_catalogo(catalogo_adicional)
        assert len(self.biblioteca.catalogo_biblioteca) == 4
        assert catalogo_adicional[0] in self.biblioteca.catalogo_biblioteca
    
    def test_adicionar_livro(self, capsys):
        """Testa adição de um livro individual"""
        self.biblioteca.adicionar_livro("A Hora da Estrela", "Clarice Lispector", 1977)
        
        # Verifica se o livro foi adicionado
        assert len(self.biblioteca.catalogo_biblioteca) == 1
        livro_adicionado = self.biblioteca.catalogo_biblioteca[0]
        assert livro_adicionado["titulo"] == "A Hora da Estrela"
        assert livro_adicionado["autor"] == "Clarice Lispector"
        assert livro_adicionado["ano"] == 1977
        
        # Verifica se a mensagem de sucesso foi impressa
        captured = capsys.readouterr()
        assert "Livro 'A Hora da Estrela' adicionado com sucesso!" in captured.out
    
    def test_adicionar_multiplos_livros(self):
        """Testa adição de múltiplos livros"""
        self.biblioteca.adicionar_livro("Livro 1", "Autor 1", 2020)
        self.biblioteca.adicionar_livro("Livro 2", "Autor 2", 2021)
        
        assert len(self.biblioteca.catalogo_biblioteca) == 2
        assert self.biblioteca.catalogo_biblioteca[0]["titulo"] == "Livro 1"
        assert self.biblioteca.catalogo_biblioteca[1]["titulo"] == "Livro 2"
    
    def test_listar_livros_biblioteca_vazia(self, capsys):
        """Testa listagem de biblioteca vazia"""
        self.biblioteca.listar_livros()
        captured = capsys.readouterr()
        assert "A biblioteca está vazia." in captured.out
    
    def test_listar_livros_com_catalogo(self, capsys):
        """Testa listagem de biblioteca com livros"""
        self.biblioteca.adicionar_catalogo(self.catalogo_exemplo)
        self.biblioteca.listar_livros()
        
        captured = capsys.readouterr()
        assert "--- Catálogo da Biblioteca ---" in captured.out
        assert "O Senhor dos Anéis" in captured.out
        assert "J.R.R. Tolkien" in captured.out
        assert "1954" in captured.out
        assert "1984" in captured.out
        assert "George Orwell" in captured.out
    
    def test_buscar_livro_por_titulo_encontrado(self, capsys):
        """Testa busca por título que existe na biblioteca"""
        self.biblioteca.adicionar_catalogo(self.catalogo_exemplo)
        self.biblioteca.buscar_livro_por_titulo("1984")
        
        captured = capsys.readouterr()
        assert "--- Livros encontrados com o título '1984' ---" in captured.out
        assert "Título: 1984 | Autor: George Orwell | Ano: 1949" in captured.out
        assert "---------------------------------------------" in captured.out
    
    def test_buscar_livro_por_titulo_parcial(self, capsys):
        """Testa busca por título parcial (case insensitive)"""
        self.biblioteca.adicionar_catalogo(self.catalogo_exemplo)
        self.biblioteca.buscar_livro_por_titulo("senhor")
        
        captured = capsys.readouterr()
        assert "--- Livros encontrados com o título 'senhor' ---" in captured.out
        assert "O Senhor dos Anéis" in captured.out
        assert "J.R.R. Tolkien" in captured.out
    
    def test_buscar_livro_por_titulo_case_insensitive(self, capsys):
        """Testa busca case insensitive"""
        self.biblioteca.adicionar_catalogo(self.catalogo_exemplo)
        self.biblioteca.buscar_livro_por_titulo("SENHOR")
        
        captured = capsys.readouterr()
        assert "O Senhor dos Anéis" in captured.out
    
    def test_buscar_livro_nao_encontrado(self, capsys):
        """Testa busca por título que não existe"""
        self.biblioteca.adicionar_catalogo(self.catalogo_exemplo)
        self.biblioteca.buscar_livro_por_titulo("Harry Potter")
        
        captured = capsys.readouterr()
        assert "Nenhum livro encontrado com o título 'Harry Potter'." in captured.out
    
    def test_buscar_livro_biblioteca_vazia(self, capsys):
        """Testa busca em biblioteca vazia"""
        self.biblioteca.buscar_livro_por_titulo("Qualquer Livro")
        
        captured = capsys.readouterr()
        assert "Nenhum livro encontrado com o título 'Qualquer Livro'." in captured.out
    
    def test_buscar_multiplos_livros_mesmo_titulo(self, capsys):
        """Testa busca que retorna múltiplos livros"""
        catalogo_duplicado = [
            {"titulo": "O Senhor dos Anéis: A Sociedade do Anel", "autor": "J.R.R. Tolkien", "ano": 1954},
            {"titulo": "O Senhor dos Anéis: As Duas Torres", "autor": "J.R.R. Tolkien", "ano": 1954}
        ]
        self.biblioteca.adicionar_catalogo(catalogo_duplicado)
        self.biblioteca.buscar_livro_por_titulo("senhor")
        
        captured = capsys.readouterr()
        assert "A Sociedade do Anel" in captured.out
        assert "As Duas Torres" in captured.out
    
    def test_fluxo_completo_biblioteca(self, capsys):
        """Testa fluxo completo de uso da biblioteca"""
        # Adiciona catálogo inicial
        self.biblioteca.adicionar_catalogo(self.catalogo_exemplo)
        
        # Adiciona um livro individual
        self.biblioteca.adicionar_livro("Dom Casmurro", "Machado de Assis", 1899)
        
        # Verifica se todos os livros estão na biblioteca
        assert len(self.biblioteca.catalogo_biblioteca) == 4
        
        # Lista todos os livros
        self.biblioteca.listar_livros()
        captured = capsys.readouterr()
        assert "Dom Casmurro" in captured.out
        
        # Busca por livro existente
        self.biblioteca.buscar_livro_por_titulo("Dom Casmurro")
        captured = capsys.readouterr()
        assert "Machado de Assis" in captured.out


if __name__ == "__main__":
    pytest.main([__file__])