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
