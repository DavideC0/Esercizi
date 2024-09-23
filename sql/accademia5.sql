-- 1. Quali sono il nome, la data di inizio e la data di fine dei WP del progetto di nome ‘Pegasus’ ?
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
where a1.id <> a2.id
	and a1.persona = a2.persona
	and pr.id = a1.progetto
	and pr.id = a2.progetto
	and pr.nome = 'Pegasus'
	and p.id = a1.persona

-- 4. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
-- fatto almeno una assenza per malattia?
select distinct p.nome, p.cognome, p.posizione
from Persona p, Assenza a
where p.id = a.persona
	and p.posizione = 'Professore Ordinario'
	and a.tipo = 'Malattia'

-- 5. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
-- fatto più di una assenza per malattia?
select distinct p.nome, p.cognome, p.posizione
from Persona p, Assenza a1, Assenza a2
where p.id = a1.persona
	and p.posizione = 'Professore Ordinario'
    and a1.persona = a2.persona
	and a1.tipo = 'Malattia'
	and a2.tipo = 'Malattia'

-- 6. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno almeno
-- un impegno per didattica?
select distinct p.nome, p.cognome, p.posizione
from Persona p, AttivitaNonProgettuale a
where p.id = a.persona
	and p.posizione = 'Ricercatore'
	and a.tipo = 'Didattica'

-- 8. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
-- attività progettuali che attività non progettuali?
select distinct p.nome, p.cognome, p.posizione
from Persona p, AttivitaNonProgettuale anp, AttivitaProgetto ap
where p.id = anp.persona
	and p.id = ap.persona
	and anp.persona = ap.persona
	and anp.giorno = ap.giorno

-- 9. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
-- attività progettuali che attività non progettuali? Si richiede anche di proiettare il
-- giorno, il nome del progetto, il tipo di attività non progettuali e la durata in ore di entrambe le attività.
select distinct p.nome, p.cognome, ap.giorno, pr.nome, ap.oreDurata, anp.tipo, anp.oreDurata
from Persona p, AttivitaNonProgettuale anp, AttivitaProgetto ap, Progetto pr
where p.id = anp.persona
	and p.id = ap.persona
	and anp.persona = ap.persona
	and anp.giorno = ap.giorno
	and ap.progetto = pr.id

-- 10. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
-- assenti e hanno attività progettuali?
select p.nome, p.cognome
from Persona p, AttivitaProgetto ap, Assenza a
where p.id = ap.persona
	and p.id = a.persona
	and ap.giorno = a.giorno

-- 11. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
-- assenti e hanno attività progettuali? Si richiede anche di proiettare il giorno, il
-- nome del progetto, la causa di assenza e la durata in ore della attività progettuale
select p.nome, p.cognome, ap.giorno, a.tipo, pg.nome, ap.oreDurata
from Persona p, AttivitaProgetto ap, Assenza a, Progetto pg
where p.id = ap.persona
	and p.id = a.persona
	and pg.id = ap.progetto
	and ap.giorno = a.giorno

-- 12. Quali sono i WP che hanno lo stesso nome, ma appartengono a progetti diversi?
SELECT distinct wp1.nome, wp1.id, wp2.id
FROM WP wp1, WP wp2
WHERE wp1.nome = wp2.nome
AND wp1.progetto <> wp2.progetto