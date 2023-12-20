select distinct cdcli, nmcli, sum(qtd*vrunt) as 'gasto'
from tbvendas
where status = 'Concluído' 
group by cdcli, nmcli
order by gasto desc
limit 1