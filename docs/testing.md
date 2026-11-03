# Testresultater 3 november 2026

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
