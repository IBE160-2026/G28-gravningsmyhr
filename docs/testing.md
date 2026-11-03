# Testresultater 3 november 2026

## Oppdatert sluttkontroll

Alle kontroller er agentutførte. Den første testloggen under beholdes som historikk; oppdateringen her erstatter dens tidligere åpne status for full offentlig spillflyt og lokale lærer-/breddeprøver.

19 av 19 automatiske tester består på Windows/Python 3.14.3. JavaScript består syntakskontroll. Nye tester dekker samtidige HTTP-forespørsler, replay, input, CSRF-header, eierskap og lukking av database ved oppstartsfeil. En separat kalkulator bruker ankomstmatriser og nettolager for åtte perioder med bestillinger 4,0,10,3,8,2,12,0. Alle historikkfelter samsvarer med motoren for fire roller. Dette er en automatisert krysskontroll, ikke menneskelig validering av undervisningsreglene. Se [utvidet regnegrunnlag](reference-extended.md).

Alle fire roller er gjennomført i 20 perioder på den offentlige siden med bestilling 4 hver periode. Verdiene ble deretter beregnet lokalt og samsvarte:

| Studentrolle | Detaljist | Grossist | Distributør | Fabrikk | Kjedesum |
|---|---:|---:|---:|---:|---:|
| Detaljist | 550 | 44 | 54 | 106 | 754 |
| Grossist | 488 | 3208 | 44 | 80 | 3820 |
| Distributør | 436 | 2732 | 6984 | 80 | 10232 |
| Fabrikk | 360 | 2176 | 6652 | 8412 | 17600 |

Hvert spill viste fullført status, grafer, tabell og regelbasert oppsummering. Detaljistspillet ble gjenopptatt fra PostgreSQL. Offentlig innlogging og utlogging er kontrollert. Fire fullførte testspill beholdes i en fiktiv testkonto.

Lokal lærerflyt: Lærer opprettet klasse, student brukte koden og fullførte 20 perioder, lærer så 20/20 og kostnad 754 og åpnet resultatet. En annen lærer så ingen av klassens spill. Ingen produksjonsroller ble endret. `python tests/local_fixture.py` oppretter isolerte fiktive identiteter; sett BEER_DB til qa-local.sqlite3. Scriptet nekter cloud-database og Vercel.

Resultatvisningen er visuelt inspisert på 360, 768 og 1440 piksler. Dokumentbredde var 345, 753 og 1425, uten horisontal overflyt. Spillbilde er også prøvd på 360. Tastatur: Tab fra rollevalg til klassekode og startknapp, Enter for start, Tab fra bestilling til bekreftelse og Enter for lagring. Etter lagring flyttet fokus til statusmeldingen. Dette er stikkprøver, ikke full tilgjengelighetsrevisjon.

Rettelser: Databaseforbindelsen lukkes også ved initialiseringsfeil. Graflegenden får samme farge og mønster som grafene. Modellkall er utsatt etter studentens valg. Lasttest, reelt modellkall, uavhengig fagkontroll og endelig Canvas-oppgave gjenstår. Se [leveransestatus](leveransestatus.md).

## Opprinnelig testlogg før sluttkontrollen

## Automatiske kontroller

`python -m unittest discover -s tests -v`: 12 av 12 bestått på Windows med Python 3.14.3. Produksjon er konfigurert for 3.12–3.13; GitHub Actions bruker 3.12, men resultatet fra Actions må kontrolleres separat etter push.

Dekning: uforanderlig klargjøring, fire roller i 20 perioder, ikke-negative lager/restordre, kostnadssummer, femperioders håndberegnet forløp, ordreledetid, varetransport, fabrikkproduksjon, inputgrenser, kommando-replay og konflikter, skjult kjedetilstand, innlogging/utlogging, lærer- og studenttilgang, SQLite-rollback og gjenåpning, avvist Vercel-lagring uten PostgreSQL og modell-timeout med reservefunksjon.

JavaScript er syntakskontrollert med `node --check public/app.js`. Dette er ingen garanti mot alle feil i nettleseren.

## Nettleserkontroll

Utført gjennom appens nettleser mot localhost:8000 med en fiktiv testkonto:

1. Registrering og oversikt virket.
2. Start som detaljist viste lager 8, restordre 0 og periodekostnad 4 før første beslutning.
3. Fem perioder med bestilling 4 ble bekreftet.
4. Omlasting beholdt innlogging og viste lagret spill i periode 5.
5. Fortsett åpnet beslutningspunkt for periode 6.
6. Spillet ble fullført til periode 20. Resultatet viste kjedekostnad 754 og rollekostnader 550, 44, 54 og 106, som summerer til 754.
7. Regelbasert oppsummering, tre SVG-grafer og datatabell var tilgjengelige.

En smal nettleservisning er visuelt inspisert. Eksakte tester på 360/768/1440, full tastaturflyt og lærerflyt i nettleser er ikke gjennomført. Ingen offentlig deploy, ekte PostgreSQL eller reelt språkmodellkall er testet. Disse kontrollene må ikke rapporteres som bestått.
