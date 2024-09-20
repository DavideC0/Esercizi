-- 1. Quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore?
select codice, comp
from Volo
where DurataMinuti > 180

-- 2. Quali sono le compagnie che hanno voli che superano le 3 ore?
select distinct comp
from Volo 
where durataminuti > 180

-- 3. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto con codice ‘CIA’ ?
select v.codice, v.comp
from Volo v, Aeroporto a, ArrPart ap
where v.codice = ap.codice and v.comp = ap.comp
	and ap.partenza = 'CIA'

-- 4. Quali sono le compagnie che hanno voli che arrivano all’aeroporto con codice ‘FCO’ ?
select distinct v.comp
from Volo v, Aeroporto a, ArrPart ap
where v.codice = ap.codice and v.comp = ap.comp
	and ap.arrivo = 'FCO'

-- 5. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto ‘FCO’
-- e arrivano all’aeroporto ‘JFK’ ?
select distinct v.codice, v.comp
from Volo v, Aeroporto a, ArrPart ap
where v.codice = ap.codice and v.comp = ap.comp
	and ap.arrivo = 'JFK' and ap.partenza = 'FCO'

-- 6. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’ e atterrano all’aeroporto ‘JFK’ ?
select distinct v.comp
from Volo v, Aeroporto a, ArrPart ap, LuogoAeroporto l
where v.codice = ap.codice and v.comp = ap.comp
	and ap.arrivo = 'JFK' and ap.partenza = 'FCO'

-- 7. Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla città di ‘New York’ ?
select distinct v.comp 
from Volo v, ArrPart ap, LuogoAeroporto la1, LuogoAeroporto la2
where v.codice = ap.codice and v.comp = ap.comp
	and ap.partenza = la1.aeroporto
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

