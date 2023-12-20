SELECT autor.codautor, 
		autor.nome, 	
		count(livro.autor) as 'quantidade_publicacoes'
FROM livro JOIN autor 	
			on livro.autor = autor.codautor 
			JOIN editora 
			on livro.editora = editora.codeditora
group by autor.codautor, autor.nome
having count(livro.edicao) >= 7