-- 1. Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi
-- aeroporti?
select a.codice, a.nome, count(distinct ap.comp)
from Aeroporto a, ArrPart ap
where ap.arrivo = a.codice or
	ap.partenza = a.codice
group by a.codice, a.nome

-- 2. Quanti sono i voli che partono dall’aeroporto ‘HTR’ e hanno una durata di almeno
-- 100 minuti?
select count(v.codice)
from ArrPart ap, Volo v
where v.codice = ap.codice and v.comp = ap.comp and
	ap.partenza = 'HTR' and v.durataMinuti >= 100

-- 3. Quanti sono gli aeroporti sui quali opera la compagnia ‘Apitalia’, per ogni nazione
-- nella quale opera?
select la.nazione, count(distinct la.aeroporto)
from LuogoAeroporto la, ArrPart ap
where ap.partenza = la.aeroporto or
	ap.arrivo = la.aeroporto and
	ap.comp = 'Apitalia'
group by la.nazione

-- 4. Qual è la media, il massimo e il minimo della durata dei voli effettuati dalla
-- compagnia ‘MagicFly’ ?
select avg(v.durataMinuti), max(v.durataMinuti), min(v.durataminuti)
from Volo v
where v.comp = 'MagicFly'

-- 5. Qual è l’anno di fondazione della compagnia più vecchia che opera in ognuno degli
-- aeroporti? da controllare
select a.codice, a.nome, min(c.annoFondaz)
from Compagnia c, Aeroporto a, ArrPart ap
where ap.partenza = a.codice or ap.arrivo = a.codice 
	and ap.comp = c.nome
group by a.codice, a.nome

-- 6. Quante sono le nazioni (diverse) raggiungibili da ogni nazione tramite uno o più
-- voli?

-- 7. Qual è la durata media dei voli che partono da ognuno degli aeroporti?
select a.codice, a.nome, avg(v.durataMinuti)
from ArrPart ap, Volo v, Aeroporto a
where v.comp = ap.comp and v.codice = ap.codice and
	ap.partenza = a.codice or ap.arrivo = a.codice
group by a.codice, a.nome

-- 8. Qual è la durata complessiva dei voli operati da ognuna delle compagnie fondate
-- a partire dal 1950?
select c.nome, sum(v.durataMinuti)
from Compagnia c, Volo v, ArrPart ap
where c.nome = ap.comp and ap.codice = v.codice and
	v.comp = ap.comp and v.comp = c.nome and
	c.annoFondaz >= 1950
group by c.nome