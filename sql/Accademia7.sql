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