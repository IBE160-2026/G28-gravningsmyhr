# Første kjørbare Beer Game

## 2026-11-03 kl. 12:02 — KI-assistent på bestilling fra Andreas

### Oppgave
Brukeren ba om å fortsette og gjøre arbeidet ferdig. Arbeidet omfatter implementering og klargjøring for publisering. Ingen selvstendig studenttesting påstås.

### Plan
Bygg lokal motor, lagring, kontoer, lærerflyt og resultater. Test før deling. Dokumenter stack-endring og faktiske begrensninger. Forsøk å kontrollere Vercel-tilgang etter at bruker oppga New Project-siden.

### Resultat
Implementasjonscommit: 6e7302a8ee57d590c80956bda9b7a5cd67219d51 i PR 1. Python og JavaScript erstatter foreløpig Next.js-forslag. Standardbibliotek og SQLite gir lokal kjøring uten installasjon; PostgreSQL-adapter er skrevet for Vercel.
12 automatiske tester består lokalt. Nettleser: registrering, fem perioder, omlasting, gjenopptak og fullføring av 20 perioder. Kjedekostnad 754, rollekostnader 550/44/54/106. JavaScript syntakskontroll består. KI-timeout er simulert; ingen reelle modellkall.
PR-tittel og beskrivelse er oppdatert til faktisk implementering. GitHub Actions viste ingen kjøringer ved kontrollen.
Brave-styring ble stoppet fordi verktøyet ikke kunne bekrefte nettadressen sikkert. Ingen Vercel-import, databaseopprettelse eller offentlig deploy er utført.

### Åpne punkter
- Ekte PostgreSQL og Vercel-bygg/ruting/HTTPS-cookie/publisert spillflyt må prøves.
- Valgfri KI trenger brukerens nøkkel, modellvalg, prisgrense og reell kvalitetskontroll.
- Systematisk bredde-/tastaturkontroll og lærerflyt i nettleser gjenstår.
- Detaljerte emneregler/PRD-mal og en uavhengig fullkjedefasit med varierende bestillinger gjenstår.
- Kontoer mangler passordgjenoppretting, verifisering og selvbetjent sletting; dataoppbevaring må avklares før ekte studentbruk.
