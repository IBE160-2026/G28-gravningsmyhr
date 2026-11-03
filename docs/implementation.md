# Implementering og arkitekturbeslutning

3. november 2026. Denne beslutningen erstatter det foreløpige stack-forslaget i `planning/architecture.md`. Planleggingshistorikken beholdes.

## Endring og begrunnelse

Implementasjonen bruker Python med standardbibliotekets HTTP-server, et JavaScript-grensesnitt uten byggeprosess, SQLite lokalt og PostgreSQL via psycopg på Vercel. Det gir kjørbarhet uten installasjon av JavaScript-avhengigheter eller lokal container. Python støttes av Vercel, jf. [offisiell dokumentasjon](https://vercel.com/docs/functions/runtimes/python). Vercel-konfigurasjonen er skrevet, men ekstern deploy er ikke kontrollert.

Supabase Auth, Next.js og separate relasjonelle historikktabeller fra forslaget er ikke implementert. Autentisering er egne e-post/passord-kontoer med PBKDF2-HMAC-SHA256, tilfeldig salt og 300 000 iterasjoner. Tilfeldige sesjonstokens lagres kun hashet og utløper etter ett døgn. Nettkapsler er HttpOnly, SameSite Strict og Secure på Vercel. POST krever en egen header, og serveren tilbyr ikke CORS. Tilgang avgjøres på serveren for hver handling.

Én transaksjon låser den samlede tilstanden. SQLite bruker BEGIN IMMEDIATE; PostgreSQL bruker SELECT FOR UPDATE. Beregning, historikk, ordre og kommando-ID skrives samlet. Samme kommando med annet innhold avvises. Ingen lokal fil brukes som varig database på Vercel. Kapasitetskostnaden ved den samlede låsen er eksplisitt akseptert for den første undervisningsversjonen; den er ikke validert under offentlig last.

## Kravstatus

F01–F09 og F11–F14 har lokal implementering. Spill, lagring og resultater er prøvd via nettleseren. Lærervisning og separasjon er kontrollert på tjenestenivå; full lærerflyt i nettleser gjenstår. F10 har en valgfri Claude-adapter, som ikke er prøvd med ekte nøkkel. API bruker [Anthropic Messages](https://platform.claude.com/docs/en/api/messages), kilde lest 3. november 2026. F14 bruker ordinære lokale kontoer i SQLite uten ekstern autentisering; det finnes ingen usikker produksjonsbryter for demoidentiteter.

Andre ledds tall skjules i spillresponsen, men standardetterspørselen er åpent dokumentert i reglene. Dette er en pedagogisk forenkling og et presisert avvik fra PRD-ordlyden om skjult framtidig etterspørsel. Ingen garanti om blind strategiutprøving gis.

## Faktisk prosess

Agenten skrev motor og lagring, deretter HTTP-lag og grensesnitt. Tester avdekket en miljøbegrensning ved midlertidige mapper på Windows; databasekontrollen ble endret til en unik midlertidig fil og bestod. En uklar periodegrense i PRD ble tidligere presisert til et klargjort, ikke-lagret beslutningspunkt før bekreftelse. Modellsvikt er testet med simulert timeout. Nettleserkontrollen omfattet registrering, fem perioder, omlasting, gjenopptak og fullføring av 20 perioder.

Det er ikke gjennomført studentintervjuer, selvstendig studenttesting, måling av læring eller faglærergodkjenning. Refleksjonsrapporten må senere beskrive faktiske vurderinger og erfaringer fra studenten, ikke tilskrives studenten ut fra dette agentarbeidet.

## Åpne leveransekontroller

- PostgreSQL-integrasjon med riktig tilkoblingsadresse og reell transaksjonstest.
- Vercel-bygg, ruting, HTTPS-cookie og publisert kjerneflyt.
- Ekte KI-kall hvis tjenesten skal brukes; prisgrense og menneskelig vurdering.
- Lærerflyt i nettleser, breddeprøver på 360/768/1440 og systematisk tastaturkontroll.
- Dataoppbevaring, sletting og kontoenes begrensninger før ekte studentbruk.
- Kontroll av emnets faktiske PRD-mal og spillregler.
