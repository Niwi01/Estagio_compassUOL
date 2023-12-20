select DISTINCT autor.nome 
from autor
	left join livro 
		on autor.codautor = livro.autor 
where livro.autor is NULL 
order by nome asc