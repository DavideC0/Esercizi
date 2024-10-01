--1. Quanti sono gli strutturati di ogni fascia?

select p.posizione, count (*) as numero
from Persona p
group by p.posizione;

--2. Quanti sono gli strutturati con stipendio ≥ 40000?

select count (*) as numero
from Persona p
where p.stipendio >= 40000;

--3. Quanti sono i progetti già finiti che superano il budget di 50000?

select count(*) as numero
from Progetto p
where p.fine <= current_date
	and p.budget > 50000;

--4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto ‘Pegasus’ ?

select avg(ap.oreDurata) as media, min(ap.oreDurata) as minimo, max(ap.oreDurata) as massimo
from Progetto p, AttivitaProgetto ap
where p.nome = 'Pegasus'
	and p.id = ap.id;

--5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto ‘Pegasus’ da ogni singolo docente?

select per.id as id_persona, per.nome, per.cognome, avg(ap1.oreDurata) as media, min(ap1.oreDurata) as minimo, max(ap1.oreDurata) as massimo
from Persona per, Progetto p, AttivitaProgetto ap1, AttivitaProgetto ap2
where p.nome = 'Pegasus'
	and p.id = ap1.id
	and per.posizione = 'Professore Ordinario' or per.posizione = 'Professore Associato'
group by per.id, per.nome, per.cognome;

--6. Qual è il numero totale di ore dedicate alla didattica da ogni docente?

select per.id, per.nome, per.cognome, sum(anp.oreDurata) as ore_didattica
from Persona per, AttivitaNonProgettuale anp
where per.id = anp.persona
	and anp.tipo = 'Didattica'
group by per.id, per.nome, per.cognome;

--7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?

select avg(per.stipendio) as media, min(per.stipendio) as minimo, max(per.stipendio) as massimo
from Persona per
where per.posizione = 'Ricercatore';

--8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori associati e dei professori ordinari?

select per.posizione, avg(per.stipendio) as media, min(per.stipendio) as minimo, max(per.stipendio) as massimo
from Persona per
group by per.posizione;

--9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?

select pro.id, pro.nome, sum(ap.oreDurata) as totale_ore
from Persona per, AttivitaProgetto ap, Progetto pro
where per.nome = 'Ginevra' 
	and per.cognome = 'Riva' 
	and ap.persona = per.id
	and pro.id = ap.progetto
group by pro.id, pro.nome;

--10. Qual è il nome dei progetti su cui lavorano più di due strutturati?

select pro.id, pro.nome
from Progetto pro, AttivitaProgetto ap
where pro.id = ap.progetto
group by pro.id, pro.nome 
having count (distinct ap.persona) > 2;

--11. Quali sono i professori associati che hanno lavorato su più di un progetto?

select per.id, per.nome, per.cognome
from Persona per, AttivitaProgetto ap
where per.posizione = 'Professore Associato'
	and per.id = ap.persona
group by per.id, per.nome, per.cognome
having count (distinct ap.progetto) > 1;

