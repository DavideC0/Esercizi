-- Qual è la durata media, per ogni compagnia, dei voli che partono da un aeroporto
-- situato in Italia?
select v.comp, avg(v.durataMinuti)
from Volo v, Aeroporto a, LuogoAeroporto la, ArrPart ap
where v.comp = ap.comp and v.codice = ap.codice and
	ap.partenza = a.codice and
	a.codice = la.aeroporto and la.nazione = 'Italy'
group by v.comp

-- Quali sono le compagnie che operano voli con durata media maggiore della durata
-- media di tutti i voli?
select v.comp, avg(v.durataMinuti)
from Volo v,(
				select avg(durataMinuti) as media
				from volo
			) as m
group by v.comp, m.media
having avg(v.durataMinuti) > m.media

-- 3. Quali sono le città dove il numero totale di voli in arrivo è maggiore del numero
-- medio dei voli in arrivo per ogni città?
with VoliArriviPerCitta as (
    select la.citta, count(*) as numero_voli
    from ArrPart ap, Aeroporto a, LuogoAeroporto la
	where ap.arrivo = a.codice and la.aeroporto = a.codice
    group by la.citta
),
MediaVoliArrivi as (
    select avg(numero_voli) as media_voli
    from VoliArriviPerCitta
)
SELECT v.citta, v.numero_voli
FROM VoliArriviPerCitta v, MediaVoliArrivi m
WHERE v.numero_voli > m.media_voli;

-- 4. Quali sono le compagnie aeree che hanno voli in partenza da aeroporti in Italia con
-- una durata media inferiore alla durata media di tutti i voli in partenza da aeroporti in Italia?
with TotalePartenzaIT as (
	select v.comp, la.nazione, sum(v.durataMinuti) as tot
	from Volo v, Aeroporto a, LuogoAeroporto la, ArrPart ap
	where v.comp = ap.comp and v.codice = ap.codice and
	ap.partenza = a.codice and
	a.codice = la.aeroporto and la.nazione = 'Italy'
	group by v.comp, la.nazione
),
MediaPartenzaIT as (
	select avg(t.tot) as media
	from  TotalePartenzaIT t
),
DurataMediaPerComp as (
	select v.comp, avg(v.durataMinuti) as media
	from Volo v, Aeroporto a, LuogoAeroporto la, ArrPart ap
	where v.comp = ap.comp and v.codice = ap.codice and
		ap.partenza = a.codice and
		a.codice = la.aeroporto and la.nazione = 'Italy'
	group by v.comp
)
select t.comp, d.media
from TotalePartenzaIT t, MediaPartenzaIt m, DurataMediaPerComp d
where d.media < m.media
group by t.comp, d.media
