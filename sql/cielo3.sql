-- 1. Qual è la durata media, per ogni compagnia, dei voli che partono da un aeroporto
-- situato in Italia?
select v.comp, avg(v.durataMinuti)
from Volo v, Aeroporto a, LuogoAeroporto la, ArrPart ap
where v.comp = ap.comp and v.codice = ap.codice and
	ap.partenza = a.codice and
	a.codice = la.aeroporto and la.nazione = 'Italy'
group by v.comp

-- 2. Quali sono le compagnie che operano voli con durata media maggiore della durata
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
select v.citta, v.numero_voli
from VoliArriviPerCitta v, MediaVoliArrivi m
where v.numero_voli > m.media_voli;

-- 4. Quali sono le compagnie aeree che hanno voli in partenza da aeroporti in Italia con
-- una durata media inferiore alla durata media di tutti i voli in partenza da aeroporti in Italia?
with MediaPartenzaIT as (
	select avg(v.durataMinuti) as media
	from Volo v, ArrPart ap, LuogoAeroporto la
	where v.comp = ap.comp and v.codice = ap.codice and 
	ap.partenza = la.aeroporto and la.nazione = 'Italy'
),
DurataMediaPerComp as (
	select v.comp, avg(v.durataMinuti) as media
	from Volo v, LuogoAeroporto la, ArrPart ap
	where v.comp = ap.comp and v.codice = ap.codice and
		ap.partenza = la.aeroporto and la.nazione = 'Italy'
	group by v.comp
)
select d.comp, d.media
from MediaPartenzaIt m, DurataMediaPerComp d
where d.media < m.media
group by d.comp, d.media

-- 5. Quali sono le città i cui voli in arrivo hanno una durata media che differisce di più
-- di una deviazione standard dalla durata media di tutti i voli? Restituire città e
-- durate medie dei voli in arrivo.
with MediaArrivi as (
	select la.citta, avg(v.durataMinuti) as media
	from Volo v, ArrPart ap, LuogoAeroporto la
	where v.comp = ap.comp and v.codice = ap.codice and la.aeroporto = ap.arrivo
	group by la.citta
),
DeviazioneVoli as (
	select stddev(v.durataMinuti) as deviazionetot, avg(v.durataMinuti) as mediatot
	from Volo v
)
select ma.citta, ma.media
from MediaArrivi ma, DeviazioneVoli dv
where (dv.mediatot - ma.media) > dv.deviazionetot