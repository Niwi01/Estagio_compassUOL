select tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc,
		sum(tbvendas.qtd*tbvendas.vrunt) as 'valor_total_vendas'
from tbdependente right join tbvendas 
				on tbdependente.cdvdd = tbvendas.cdvdd
where status = "Concluído"
group by tbdependente.cddep
order by 'valor_total_vendas' desc
limit 1