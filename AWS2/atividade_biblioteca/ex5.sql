SELECT DISTINCT autor.nome
From autor 
	left join livro on autor.codautor =livro.autor 
where livro.editora != 13
order by autor.nome asc