SELECT tbvendedor.cdvdd, tbvendedor.nmvdd
FROM tbvendedor 	
	LEFT JOIN tbvendas on tbvendas.cdvdd = tbvendedor.cdvdd 
WHERE status = "Concluído"
group by tbvendedor.nmvdd
order by count(tbvendas.status = "Concluído") desc
limit 1