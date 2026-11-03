# Leveransestatus for Beer Game

Kontrollert 3. november 2026. Statusen beskriver faktisk arbeid og er ikke en formell godkjenning eller karaktervurdering.

## Klar og kontrollert

- Publisert app: https://g28-gravningsmyhr.vercel.app/
- Alle fire roller gjennomført i 20 perioder på nett med bestilling 4 hver periode.
- Registrering, innlogging, lagring, omlasting, gjenopptak og utlogging prøvd mot PostgreSQL.
- Resultatgrafer, periodeoversikt og gratis, regelbasert oppsummering tilgjengelige.
- Lokal lærerflyt prøvd i nettleser: klasse, studenttilknytning, fullført spill og resultatinnsyn.
- Separasjon mellom lærere og mellom studenter kontrollert i tester; en annen lærer så ingen spill i klasseoversikten.
- 19 automatiske tester består, inkludert HTTP, samtidighet og separat åtteperiodersberegning.
- Resultatvisning kontrollert på 360, 768 og 1440 piksler. Spillbilde kontrollert på 360 piksler. Sentrale tastaturhandlinger prøvd.
- PRD, produktbeskrivelse, arkitekturbeslutning, teststatus, driftsveiledning og refleksjonsutkast er samlet i repoet.

## Bevisst avgrenset etter studentens valg

Studenten valgte 3. november å beholde gratis, regelbasert oppsummering foreløpig. Ekte språkmodellrefleksjon er en utsatt funksjon. Claude-adapteren er valgfri og ikke prøvd med betalt nøkkel. Dette er et dokumentert avvik fra den opprinnelige forventningen om en KI-generert sluttoppsummering; det må vurderes mot endelige emnekrav, ikke omtales som en ferdig KI-funksjon.

Flerspiller med mennesker og avanserte lærerfunksjoner er fortsatt utenfor v1. Medspillerne er regelbaserte, ikke språkmodeller. Lærerrollen tildeles administrativt; appen har ingen knapp der en student kan gi seg selv lærerinnsyn.

## Studenten må fullføre før innlevering

1. Roter databasepassordet som tidligere ble delt, oppdater DATABASE_URL privat i Vercel, publiser med den nye verdien og kontroller innlogging og en periode. Dette er ikke utført eller bekreftet av agenten.
2. Les refleksjonsutkastet og prøv appen selv. Rapporten beskriver agentens tester som agentutførte. Studentens egne prøver skal først dokumenteres når de faktisk er gjort.
3. Kontroller endelig Canvas-oppgave, frist, rapportformat og eventuelle nye fagkrav. Bare emneoversikt, to PDF-er og tidligere kunngjøringer er tilgjengelige her. PRD-påminnelsen innen 5. november er ikke dokumentasjon på eksamensfristen.
4. Sammenhold prosjektets spillregler med eventuell fastsatt undervisningsfasit. Krysskontroll mellom to beregningsmetoder verifiserer implementasjonen mot vår regeltekst, ikke at reglene er de læreren ønsker.
5. Avklar lagring og sletting før bruk med reelle studentdata. Nåværende kontoer mangler e-postverifisering, passordgjenoppretting og selvbetjent sletting.

## Hva som ikke er gjort

Ingen innlevering i Canvas, læringsmåling, rekruttering av brukere, betalt KI-aktivering eller faglærergodkjenning. Lærerflyten er kontrollert lokalt og tilgangslogikken er den samme som på nett; det er ikke gitt produksjonslærerrolle til en testkonto for å teste den offentlig.

## Kravoversikt

| Krav | Status og belegg |
|---|---|
| F01–F09 | Lokal implementering; offentlig kjerneflyt og fire fulle spill kontrollert |
| F10 | Utsatt etter studentens valg; valgfri adapter finnes, reelt modellkall ikke testet |
| F11 | Gratis reserveoppsummering virker i offentlig resultatvisning |
| F12–F13 | Lokal klasse-/lærerflyt og tilgangstester består |
| F14 | Lokal kjøring og isolerte testidentiteter uten cloud-nøkler |
| K01–K02 | Isolert motor, transaksjonstester, replay og samtidighet |
| K03–K05 | Stikkprøvd tastaturflyt og skjermbredder; ingen full WCAG-revisjon |
| K06–K07 | Ingen systematisk ytelsesmåling; modelltimeout er simulert, ikke reelt modellkall |
| K08–K10 | Kjerneflyt uten modell; lokal og offentlig kjøring dokumentert |

## Reproduserbar demonstrasjon

Start nytt spill, velg detaljist og bestill 4 i alle perioder. Etter periode 20 skal kostnadene være 550, 44, 54 og 106 per ledd, totalt 754. For å kontrollere gjenopptak: avbryt etter fem bekreftede perioder, last siden på nytt, velg Fortsett og fullfør. Se `docs/testing.md` for flere testresultater.
