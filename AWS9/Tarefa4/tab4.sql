create table avaliacoes as
SELECT
  CONCAT(id_json, ',', id_csv) AS avaliacao_id,
  notamedia_json,
  notamedia_csv,
  numerovotos_json,
  numerovotos_csv
FROM refinando
