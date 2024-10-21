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