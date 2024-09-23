-- 1. Quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore?
select codice, comp
from Volo
where DurataMinuti > 180

-- 2. Quali sono le compagnie che hanno voli che superano le 3 ore?
select distinct comp
from Volo 
where durataminuti > 180

-- 3. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto con codice ‘CIA’ ?
select ap.codice, ap.comp
from ArrPart ap
where ap.partenza = 'CIA'

-- 4. Quali sono le compagnie che hanno voli che arrivano all’aeroporto con codice ‘FCO’ ?
select distinct ap.comp
from ArrPart ap
where ap.arrivo = 'FCO'

-- 5. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto ‘FCO’
-- e arrivano all’aeroporto ‘JFK’ ?
select distinct ap.codice, ap.comp
from ArrPart ap
where ap.arrivo = 'JFK' and ap.partenza = 'FCO'

-- 6. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’ e atterrano all’aeroporto ‘JFK’ ?
select distinct ap.comp
from ArrPart ap
where ap.arrivo = 'JFK' and ap.partenza = 'FCO'

-- 7. Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla città di ‘New York’ ?
select distinct ap.comp 
from ArrPart ap, LuogoAeroporto la1, LuogoAeroporto la2
where ap.partenza = la1.aeroporto
	and ap.arrivo = la2.aeroporto
	and la1.aeroporto <> la2.aeroporto
	and la1.citta = 'Roma'
	and la2.citta = 'New York'

-- 8. Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli della compagnia di nome ‘MagicFly’ ?
select distinct a.codice, a.nome, la.citta
from Aeroporto a, LuogoAeroporto la, Compagnia c
where a.codice = la.aeroporto
	and c.nome = a.comp
	and c.comp = 'MagicFly'

-- 9. Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’ e
-- atterrano ad un qualunque aeroporto della città di ‘New York’? Restituire: codice
-- del volo, nome della compagnia, e aeroporti di partenza e arrivo.
select ap.codice, ap.comp, ap.partenza, ap.arrivo
from ArrPart ap, LuogoAeroporto la1, LuogoAeroporto la2
where ap.partenza = la1.aeroporto
	and ap.arrivo = la2.aeroporto
	and la1.citta = 'Roma'
	and la2.citta = 'New York'
	
-- 10. Quali sono i possibili piani di volo con esattamente un cambio (utilizzando solo
-- voli della stessa compagnia) da un qualunque aeroporto della città di ‘Roma’ ad un
-- qualunque aeroporto della città di ‘New York’ ? Restituire: nome della compagnia,
-- codici dei voli, e aeroporti di partenza, scalo e arrivo.
select ap1.comp, ap1.codice, ap1.partenza, ap1.arrivo as scalo, ap2.codice, ap2.arrivo
from ArrPart ap1, ArrPart ap2, LuogoAeroporto la1, LuogoAeroporto la2
where ap1.partenza = la1.aeroporto
	and ap2.arrivo = la2.aeroporto
	and la1.citta = 'Roma'
	and la2.citta = 'New York'
	and ap2.partenza = ap1.arrivo
	and ap1.comp = ap2.comp

-- 11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, 
-- atterrano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione?
select v.comp
from Volo v, ArrPart ap, Compagnia c
where v.codice = ap.codice and v.comp = ap.comp and v.comp = c.nome
	and ap.partenza = 'FCO' and ap.arrivo = 'JFK'
	and c.annoFondaz IS NOT NULL