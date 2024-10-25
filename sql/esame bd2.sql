-- QUERY 1 Quali sono gli aeroporti (restituire codice e nome) della città di Roma
select a.*
from Aeroporto a, LuogoAeroporto la
where a.codice = la.aeroporto and la.citta = 'Roma'

-- QUERY 2 Quali sono le compagnie (restituire nome e anno di fondazione) che hanno voli di durata di almeno 3 ore
select distinct c.*
from Volo v, Compagnia c
where v.comp = c.nome and v.durataMinuti > 180
-- QUERY 3 Qual è la durata più lunga di un volo di ogni compagnia (restituire nome della compagnia e durata di tale volo)
select distinct v.comp, max(v.durataMinuti)
from Volo v
group by v.comp

-- QUERY 4 Quali sono le compagnie che hanno voli che atterrano in un qualche aeroporto di New York
select distinct v.comp
from Volo v, ArrPart ap, LuogoAeroporto la
where v.comp = ap.comp and v.codice = ap.codice and
	la.aeroporto = ap.arrivo and la.citta = 'New York'

-- QUERY 5 Quali sono i piani di volo con un cambio che collegano
-- Roma a New York in al più 6 ore (escludendo il tempo del cambio)
select ap1.comp, ap1.codice as codice_partenza, ap1.partenza, ap1.arrivo as scalo, ap2.codice as codice_arrivo, ap2.arrivo, (v1.durataminuti + v2.durataminuti) as ore_tot
from ArrPart ap1, ArrPart ap2, LuogoAeroporto la1, LuogoAeroporto la2, Volo v1, Volo v2
where ap1.partenza = la1.aeroporto
	and ap2.arrivo = la2.aeroporto
    and ap1.arrivo = ap2.partenza
	and la1.citta = 'Roma'
	and la2.citta = 'New York'
	and v1.comp = ap1.comp and v1.codice = ap1.codice
	and v2.comp = ap2.comp and v2.codice = ap2.codice
	and (v1.durataminuti + v2.durataminuti) > 360

-- QUERY 6 Quanti sono, per ogni compagnia, i piani di volo con un cambio
-- (con entrambi i voli di quella compagnia) che collegano Roma a New York in al più 6 ore
select ap1.comp, count(*)
from ArrPart ap1, ArrPart ap2, LuogoAeroporto la1, LuogoAeroporto la2, Volo v1, Volo v2
where ap1.partenza = la1.aeroporto
	and ap2.arrivo = la2.aeroporto
	and la1.citta = 'Roma'
	and la2.citta = 'New York'
	and ap2.partenza = ap1.arrivo
	and ap1.comp = ap2.comp
	and v1.comp = ap1.comp and v1.codice = ap1.codice
	and v2.comp = ap2.comp and v2.codice = ap2.codice
	and (v1.durataminuti + v2.durataminuti) > 360
group by ap1.comp

-- QUERY 7 Quali sono i piani di volo con un cambio in Germania che collegano Roma a New York in al più 6 ore di volo
-- (escludendo il tempo di cambio in Germania). Ordinare i voli per durata di volo complessiva (escludendo il tempo di cambio) crescente
select ap1.comp, ap1.codice, ap1.partenza, ap1.arrivo as scalo, ap2.codice, ap2.arrivo, (v1.durataminuti + v2.durataminuti) as ore_tot
from ArrPart ap1, ArrPart ap2, LuogoAeroporto la1, LuogoAeroporto la2, Volo v1, Volo v2, LuogoAeroporto la3
where ap1.partenza = la1.aeroporto
	and ap2.arrivo = la2.aeroporto
	and la3.aeroporto = ap1.arrivo
	and la3.aeroporto = ap2.partenza
	and la1.citta = 'Roma'
	and la2.citta = 'New York'
	and la3.nazione = 'Germania'
	and v1.comp = ap1.comp and v1.codice = ap1.codice
	and v2.comp = ap2.comp and v2.codice = ap2.codice
	and (v1.durataminuti + v2.durataminuti) > 360
    order by (v1.durataminuti + v2.durataminuti) asc

-- QUERY 8 Qual è l’anno nel quale è stata fondata la prima compagnia aerea presente nel db
select min(annoFondaz)
from compagnia

-- QUERY 9 Quante sono le compagnie aeree di cui non si conosce l’anno di fondazione
select *
from compagnia
where annoFondaz is null

-- QUERY 10 Quante sono le compagnie aeree fondate ogni anno. Per ogni anno nel quale è stata fondata almeno una
-- compagnia, restituire l’anno e il numero di compagnie fondate in quell’anno
select annoFondaz, count(*)
from compagnia
where annoFondaz is not null
group by annoFondaz