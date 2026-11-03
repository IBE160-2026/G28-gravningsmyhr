# Beer Game for G28

Norsk læringssimulering for IBE160 26H Programmering med KI. Spill én av fire roller mot regelbaserte medspillere, lagre og fortsett, se hele kjedens resultater og la en lærer følge egne klasser.

## Status

Første kjørbare versjon. Lokal SQLite-versjon er testet. PostgreSQL-adapter, Vercel-konfigurasjon og valgfri Claude-integrasjon er skrevet, men er ikke verifisert mot brukerens eksterne tjenester. Det finnes foreløpig ingen bekreftet offentlig nettadresse. Dette er et undervisningsprosjekt, ikke et ferdig driftet system for sensitive studentdata.

## Lokal oppstart

Installer Python 3.12 eller 3.13. Åpne terminalen i repoets rot:

```powershell
python server.py
```

Åpne http://127.0.0.1:8000. Opprett en testkonto med en fiktiv e-postadresse og passord på minst ti tegn. Det sendes ingen e-post. Lokal oppstart krever ingen tilleggspakker, API-nøkkel eller cloud-konto. Databasen `beergame.sqlite3` opprettes automatisk i arbeidsmappen og holdes utenfor Git. Stopp med Ctrl+C. Start igjen med samme kommando og mappe for å beholde kontoer og spill.

For en annen port: `python server.py --port 8001`. For separat testdatabase, sett `$env:BEER_DB='test.sqlite3'` før oppstart. Miljøvariabler leses fra prosessen, ikke automatisk fra `.env`.

### Lærervisning

Registrer en separat lærerkonto i appen. Tildel rollen fra en terminal med tilgang til riktig database:

```powershell
python admin.py laerer@example.test
```

Logg inn igjen. Opprett klasse og del klassekoden med teststudenten. Studenten legger inn koden ved opprettelse av nytt spill. Andre lærere eller studenter får ikke tilgang til spillet. Det finnes ingen offentlig funksjon for å tildele lærerrolle.

## Tester

```powershell
python -m unittest discover -s tests -v
```

Testene bruker standardbiblioteket og egne midlertidige databasefiler. De tester beregninger, ledetider, alle spillerroller, ugyldig input, repetert forespørsel, eierskap, læreravgrensning, lagring og feilhåndtering. Se [testresultater](docs/testing.md) og [referanseforløp](docs/reference.md). Reelle PostgreSQL- og modellkall er ikke en del av denne lokale pakken.

## Publisering på Vercel

1. Bruk ett Vercel-prosjekt for grupperepoet. Koden må være på grenen du publiserer. Denne implementeringen er først delt i PR 1; `main` inneholder ikke automatisk endringene før fletting.
2. Opprett en PostgreSQL-database, for eksempel i Supabase. Bruk leverandørens pooled tilkoblingsadresse som passer serverløs drift. Den skal bruke TLS, eksempelvis `sslmode=require`. Ikke legg adressen i GitHub eller chatten.
3. Importer `IBE160-2026/G28-gravningsmyhr`. Velg rammeverk `Other`, rotmappe `./`, og ingen egendefinert build-kommando. Repoet har `api/index.py`, `requirements.txt` og `vercel.json`.
4. Legg `DATABASE_URL` inn under Vercels Environment Variables. API-et nekter å bruke lokal SQLite på Vercel. Databaserollen må kunne opprette og bruke tabellen `app_state` i sitt eget skjema. Bruk en egen database for prosjektet.
5. Deploy, kontroller byggeloggen og test opprettelse av konto, en periode, oppfriskning, gjenopptak og resultater. Hvis deploy feiler, bruk den faktiske loggen til retting; den eksterne konfigurasjonen er ikke prøvd ennå.
6. Legg den bekreftede nettadressen i README. En publisert innloggingsside alene er ikke tilstrekkelig kontroll av database og spillflyt.

Produksjonsavhengighet installeres fra `requirements.txt`. Ved lokal testing mot PostgreSQL:

```powershell
python -m pip install -r requirements.txt
# Sett DATABASE_URL privat i terminalen før server.py eller admin.py kjøres.
python server.py
```

### Valgfri KI-refleksjon

Uten nøkler er resultatoppsummeringen regelbasert og tydelig merket. Med begge variablene `ANTHROPIC_API_KEY` og `ANTHROPIC_MODEL` får eieren av et fullført spill en knapp for KI-refleksjon. Bruk en modellidentifikator som er aktiv på din konto. Ingen modell velges skjult, og det gjøres ikke modellkall uten disse innstillingene og et klikk.

Én forespørsel per spill, maksimalt 500 output-tokens og 15 sekunders timeout begrenser kallene. Ved feil beholdes den regelbaserte oppsummeringen. Bare spilltall sendes, ikke navn, e-post eller klassekode. Bekreft leverandørens pris og sett kontogrense før aktivering. KI-teksten må vurderes kritisk opp mot de synlige tallene. Ingen virkelige API-kall er testet i denne leveransen.

## Spillregler

20 perioder; startlager 12, tomme køer og ingen startrestordre. Kundeetterspørsel 4 i periode 1–4 og 8 i periode 5–20. Ordre tar én periode, transport og produksjon to. Lagerkostnad er 0,50 og restordrekostnad 1,00 per enhet og periode. Dette er vår versjonerte undervisningsvariant, ikke en verifisert fasit fra emnet. Se [PRD](docs/planning/prd.md) og [arkitekturbeslutning](docs/implementation.md).

## Struktur og prosess

- `game.py`: ren, deterministisk spillmotor.
- `storage.py`: SQLite/PostgreSQL med transaksjoner.
- `api/index.py`: autentisering, autorisasjon og HTTP.
- `reflection.py`: valgfritt serverkall til Claude.
- `public/`: norsk brukergrensesnitt, stilark og SVG-grafer.
- `tests/`: automatiserte tester.
- `docs/planning/`: PRD, UX, arkitektur og stories.
- [Produktbeskrivelse](product-brief.md), [tilbakemelding](tilbakemelding-product-brief.md), [prosess og begrensninger](docs/implementation.md).

## Kjente begrensninger

Databaseadapteren lagrer én samlet JSON-tilstand med transaksjonslås. Dette gir atomiske oppdateringer og enkel lokal kjøring, men begrenser kapasiteten og passer et lite undervisningsprosjekt. Et modellkall holder låsen i inntil timeout. Ved større bruk bør data normaliseres og refleksjon kjøres i separat arbeidskø. Kontoer har ikke e-postverifisering, passordgjenoppretting eller selvbetjent sletting. Bruk fiktive kontoer til disse forholdene og dataoppbevaring er avklart. Lokal lagring og produksjonslagring er ulike adaptere og produksjonsadapteren trenger en egen integrasjonstest.

Utviklingen er utført med KI-støtte. Testene og nettleserkontrollen er agentutførte; ingen selvstendig studenttesting eller faglærergodkjenning påstås.
