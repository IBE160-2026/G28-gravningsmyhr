# Feilsøking av publisert database

## 2026-11-03 — KI-assistent

### Oppgave
Undersøk publisert app som viser tjenestefeil etter Vercel-deploy.

### Plan
Kontroller faktisk side og avhengighetsdeklarasjon. Rett manglende eksplisitt driverdeklarasjon og legg til feilkategorier uten rå unntak.

### Resultat
Publisert side viste tjenestefeil før innlogging. psycopg er nå eksplisitt oppført i pyproject.toml i tillegg til requirements.txt. Feilhåndtering viser DB_DRIVER, DB_CONNECTION eller SERVICE_CONFIG og logger bare kategori og unntakstype. Ingen passord er lagt i repoet.

### Åpne punkter
Ny Vercel-deploy og databasetilkobling må kontrolleres. Rotårsak er ikke bekreftet fra en serverlogg. Brukeren må rotere databasepassord som ble delt i chatten og oppdatere Vercel privat.

## Oppfølging etter ny deploy

Vercel rapporterte vellykket deploy for commit 20736dac67d928cb0122e3e1909958423c2bf1b8. Innloggingssiden fungerer nå. Agenten opprettet en fiktiv testkonto, startet et detaljistspill, lagret første periode, lastet siden på nytt og gjenopptok til beslutningspunkt for periode 2. Kjedekostnad etter første periode var 22 og detaljistkostnad 4. Offentlig URL er lagt til i README. Det er en testkonto og et ufullført testspill i produksjonsdatabasen. Den eksakte opprinnelige unntakstypen er ikke bekreftet; avhengighetsendringen ble fulgt av fungerende tilkobling.

Åpent: full offentlig 20-periodersflyt, lærerflyt, ekte KI-integrasjon og passordrotasjon som nevnt over. Ingen nye hemmeligheter er innhentet eller lagret i Git.
