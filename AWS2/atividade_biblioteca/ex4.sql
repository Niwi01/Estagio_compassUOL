SELECT autor.nome, autor.codautor, autor.nascimento, 
		count((case when livro.autor is not null then 0 end)) as "quantidade"
From livro full join autor on livro.autor = codautor 
group by livro.autor, autor.nome
order by autor.nome asc