-- 1. Quali sono il nome, la data di inizio e la data di fine dei WP del progetto di nome‘Pegasus’ ?
select *
from WP wp, Progetto p
where p.nome = 'Pegasus'
	and wp.progetto = p.id;

-- 2. Quali sono il nome, il cognome e la posizione degli strutturati che hanno almeno 
-- una attività nel progetto ‘Pegasus’, ordinati per cognome decrescente?
select distinct p.nome, p.cognome, p.posizione, pr.nome
from Persona p, AttivitaProgetto a, Progetto pr
where p.id = a.persona
	and a.progetto = pr.id
	and pr.nome = 'Pegasus'
order by p.cognome desc

-- 3. Quali sono il nome, il cognome e la posizione degli strutturati che hanno più di
-- una attività nel progetto ‘Pegasus’ ?
select distinct p.nome, p.cognome, p.posizione, pr.nome
from Persona p, AttivitaProgetto a1, AttivitaProgetto a2, Progetto pr
where p.id = a1.persona
	and a1.progetto = pr.id
	and pr.nome = 'Pegasus'
	and a1.giorno <> a2.giorno
	and a1.persona = a2.persona