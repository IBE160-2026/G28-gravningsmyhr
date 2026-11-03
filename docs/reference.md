# Referanseforløp og ledetider

Manuelt utledet av prosjektreglene, ikke eksportert som fasit fra motoren. Agentutført kontroll; studenten har ikke uavhengig bekreftet forløpet.

## Fem perioder med nullbestilling fra detaljisten

Alle ledd starter med 12. Detaljisten bestiller null. De andre har ingen innkommende ordre og har allerede mållager 12, slik at de også bestiller null. Ingen sendinger mellom ledd oppstår. Grossist, distributør og fabrikk har derfor lager 12, restordre 0 og kostnad 6 hver periode.

| Periode | Kundeetterspørsel | Detaljist lager | Detaljist restordre | Detaljist periodekostnad | Kjedens periodekostnad |
|---|---:|---:|---:|---:|---:|
| 1 | 4 | 8 | 0 | 4 | 22 |
| 2 | 4 | 4 | 0 | 2 | 20 |
| 3 | 4 | 0 | 0 | 0 | 18 |
| 4 | 4 | 0 | 4 | 4 | 22 |
| 5 | 8 | 0 | 12 | 12 | 30 |

Sum kjedekostnad er 112, og detaljistens kostnad er 22. Dette kontrolleres med faste forventningsverdier i testene.

## Separat ledetidsfasit

Detaljisten bestiller 4 i periode 1. Grossisten mottar ordren i periode 2, sender 4 fra sitt startlager og mottar ikke en ny ordre i periode 3 hvis detaljisten nå bestiller 0. Den sendingen ankommer detaljisten i periode 4, ikke periode 2 eller 3.

Fabrikken som student bestiller produksjon 7 i periode 1 og 0 i periode 2. Produksjonen fra periode 1 ankommer i periode 3. Ingen produksjon ankommer i periode 2. Disse forløpene kontrollerer ordre, transport og produksjon hver for seg.

Et mer omfattende, uavhengig kontrollert regneark med varierende bestillinger og alle fire ledd vil styrke domenekontrollen før endelig innlevering.
