-- 1. Qual è media e deviazione standard degli stipendi per ogni categoria di strutturati?
select avg(p.stipendio), stddev(p.stipendio), p.posizione
from Persona p
group by p.posizione

-- 2. Quali sono i ricercatori (tutti gli attributi) con uno stipendio superiore alla media
-- della loro categoria?
select *
from Persona p, (
		select avg(p.stipendio) as stipendio
		from Persona p
		where p.posizione = 'Ricercatore'
	) as media
where p.posizione = 'Ricercatore' and
	media.stipendio < p.stipendio

-- 3. Per ogni categoria di strutturati quante sono le persone con uno stipendio che
-- differisce di al massimo una deviazione standard dalla media della loro categoria?
select p.posizione, count(p)
from Persona p, (
				select avg(p.stipendio) as media, stddev(p.stipendio) as dev_standard
				from Persona p
				group by p.posizione
				) as q
where p.stipendio <= (q.media + q.dev_standard) and p.stipendio >= (q.media - q.dev_standard)
group by p.posizione

-- 4. Chi sono gli strutturati che hanno lavorato almeno 20 ore complessive in attività
-- progettuali? Restituire tutti i loro dati e il numero di ore lavorate.
select p.*, sum(ap.oreDurata)
from Persona p, AttivitaProgetto ap
where p.id = ap.persona
group by p.id
having sum(ap.oreDurata) >= 20

-- 5. Quali sono i progetti la cui durata è superiore alla media delle durate di tutti i
-- progetti? Restituire nome dei progetti e loro durata in giorni.
select pr.nome, (pr.fine-pr.inizio)
from Progetto pr, (select avg(pr.fine-pr.inizio) as media from Progetto pr) as q
where (pr.fine-pr.inizio) > q.media

-- 6. Quali sono i progetti terminati in data odierna che hanno avuto attività di tipo
-- “Dimostrazione”? Restituire nome di ogni progetto e il numero complessivo delle
-- ore dedicate a tali attività nel progetto.
select pr.id, pr.nome, sum(ap.oreDurata)
from Progetto pr, AttivitaProgetto ap
where ap.tipo = 'Dimostrazione' and pr.id = ap.progetto
group by pr.id

-- 7. Quali sono i professori ordinari che hanno fatto più assenze per malattia del numero 
-- di assenze medio per malattia dei professori associati? Restituire id, nome e
-- cognome del professore e il numero di giorni di assenza per malattia.