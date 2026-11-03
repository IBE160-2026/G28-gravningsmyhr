# Arbeidssteg og sentrale prompter for Beer Game

Dato: 3. november 2026. Vedlegg til refleksjonsrapporten.

## Kildestatus og avgrensning

Registeret bygger på den tilgjengelige samtalen, dokumentene i repoet og faktiske testresultater. Arbeidsstegene under er rekonstruert fra dette grunnlaget. Det er ikke en komplett, samtidig ført promptlogg eller full transkripsjon av tidligere prosjektøkter. Første generering av produktbeskrivelsen skjedde tidligere og kan ikke gjenskapes sikkert her. Ingen manglende prompt er diktet opp. Hemmeligheter og rå tilkoblingsverdier er utelatt.

Malen ber om alle steg og lagrede prompter. Denne oversikten dokumenterer de tilgjengelige hovedstegene og markerer hullene. Den skal ikke framstilles som dokumentasjon på en full installert BMAD-arbeidsflyt eller som en komplett historikk fra semesterstart.

## Dokumenterte hovedsteg

| Steg | Handling og kontekst | Resultat eller kontroll |
|---|---|---|
| 1 | Studenten ba om hjelp med lærerens Vercel-kunngjøring | Repoet ble identifisert som G28-gravningsmyhr |
| 2 | KI undersøkte repoet og grenene | Det lå dokumentasjon, men ingen appkode, i main |
| 3 | Studenten opplyste at appen trolig ikke var laget | Videre arbeid ble rettet mot planlegging før publisering |
| 4 | Studenten leverte emneoversikt fra Canvas | PRD-påminnelse og vurderingens hoveddeler ble identifisert; endelig innleveringssted var ukjent |
| 5 | Sensorveiledning del 1 og Appendix A ble lest | Prosess, tester, kjørbarhet og repo ble brukt som kvalitetsgrunnlag |
| 6 | Studenten ba om å sette i gang | Første PRD ble skrevet med tydelig merkede spillforslag |
| 7 | Faglærers tilbakemelding i repoet ble lest | Solo, regelbaserte medspillere og enkel lærervisning ble prioritert |
| 8 | Produktbeskrivelse og PRD ble justert | Omfang og periodegrense ble tydeligere |
| 9 | Brukerflyt, arkitekturforslag og tretten oppgaver ble laget | Planleggingen ble lagt i egen gren og PR 1 |
| 10 | Studenten ba om å fortsette og gjøre arbeidet ferdig | Implementering startet; faktisk stack ble Python og JavaScript |
| 11 | Spillmotor og lagring ble skrevet | Deterministiske regler og transaksjoner kunne testes lokalt |
| 12 | HTTP, kontoer, tilgang og klassefunksjon ble skrevet | Student- og lærerroller, kommando-ID og versjonskontroll kom på plass |
| 13 | Grensesnitt, grafer og oppsummering ble skrevet | Norsk spillflyt og reserveoppsummering fungerte uten modellnøkkel |
| 14 | Automatiske tester og lokal nettleserkontroll ble utført | Tolv opprinnelige tester og et helt lokalt spill ble gjennomført |
| 15 | Nettleserstyring i Brave ble stoppet av verktøyet | Studenten fortsatte med skjermbilder og veiledede klikk |
| 16 | Studenten bekreftet fletting av PR 1 i GitHub | Appkode kom inn i main |
| 17 | Studenten importerte repoet i Vercel | Python-oppsett og rotmappe ble gjennomgått |
| 18 | Studenten opprettet Supabase-organisasjon og prosjekt | PostgreSQL ble valgt for varig lagring; Data API var ikke nødvendig for arkitekturen |
| 19 | Studenten åpnet Connect og valgte URI og transaction pooler | DATABASE_URL ble lagt privat i Vercel; faktisk passordverdi er ikke tatt med i dette registeret |
| 20 | Studenten startet deploy | Appen ble publisert, men første visning hadde en tjenestefeil |
| 21 | KI undersøkte kode og la psycopg eksplisitt til i pyproject.toml | Ny deploy fungerte; opprinnelig unntak ble ikke bekreftet fra rå serverlogg |
| 22 | KI prøvde offentlig registrering, periode og gjenopptak | PostgreSQL-flyten fungerte; nettadresse ble lagt i README |
| 23 | Studenten ba om sluttarbeidet | Separat regnekalkulator og flere tester ble laget |
| 24 | KI gjennomførte alle fire roller i 20 perioder på nett | Sluttkostnader samsvarte med lokal beregning |
| 25 | KI prøvde lokal klasseflyt med to lærere og en student | Riktig lærer så resultatet; annen lærer så ikke klassens spill |
| 26 | KI prøvde skjermbredder og sentrale tastaturhandlinger | Ingen dokumentoverflyt i prøvene; fokus etter lagring var kontrollert |
| 27 | Ressurslukking og graflegende ble forbedret | Nitten automatiske tester bestod; GitHub Actions og Vercel fullførte vellykket |
| 28 | Studenten valgte gratis oppsummering | Ekte KI-refleksjon ble utsatt og avviket skrevet i brief og PRD |
| 29 | KI skrev første refleksjonsutkast fra studentens uttalelser | Utkastet skilte mellom agentarbeid og studentens egne erfaringer |
| 30 | Studenten viste Canvas-vurderinger og modulliste | Ingen synlig innleveringsoppgave eller frist ble dokumentert |
| 31 | PDF med prosjektforslag ble lest | Dokumentet var en idéoversikt, ikke en endelig leveringsinstruks |
| 32 | Studenten leverte reflection-report-template (1).md | Forventet lengde 3000–5000 ord og de åtte hoveddelene ble identifisert |
| 33 | Rapporten ble utvidet og strukturert etter malen | Alle 23 underdeler er dekket; personlig gjennomlesing og endelig innleveringsavklaring gjenstår |

## Ordrette brukerprompter fra tilgjengelig samtale

| Prompt | Kontekst og virkning |
|---|---|
| «sett i gang» | Bestilling av første PRD etter gjennomgang av emnegrunnlag |
| «hvordan går jeg videre nå hva gjør jeg med denne» | Behov for forklaring av PRD og videre flyt |
| «kan du gjøre alt dette for meg» | Bestilling av videre dokumentarbeid og GitHub-klargjøring |
| «fortsett - gjør alt ferdig» | Bestilling av implementering og klargjøring for drift |
| «hvor trykker jeg?» | Skjermbildebasert veiledning under GitHub-fletting |
| «jeg har inngenting utover hva du har laget her» | Avklarte at database og publisering måtte settes opp fra start |
| «hva er neste steg for å gjøre dette helt ferdig» | Utløste oversikt over sluttkontroll og dokumentasjon |
| «gjør dete for meg» | Bestilling av sluttkontroll og rapportarbeid |
| «ingenting har vært vanskelig, jeg har lært at ki kan gjøre det aller meste,  forutsatt at du har avanserte nok modeller» | Studentens faktiske uttalelse om personlig erfaring; grunnlag for rapportens personlige refleksjon |
| «Behold gratis oppsummering foreløpig» | Eksplisitt beslutning om å utsette ekte modellrefleksjon |
| «er oppgaven fullført? hvor skal jeg innlevere ?» | Avklarte behovet for faktiske Canvas-instruksjoner |

Flere meldinger bestod av dokumenter, skjermbilder eller korte oppfølgingsspørsmål. Disse er beskrevet i hovedstegene og ikke omskrevet til oppdiktede, detaljerte utviklerprompter.

## Kvalitetsgrunnlag og hull

Repoets docs/testing.md beskriver tester og resultater. docs/reference-extended.md viser den separate beregningen. .logs/g28-gravningsmyhr inneholder øktlogger, mens commit-historikken viser tidspunkt for endringer. Dette gir støtte for hva som er gjort, men er ikke bevis for at studenten selv har utført agentens kontroller.

Den tidligere brief-genereringen og en full prompttranskripsjon mangler. Hvis slike originale logger finnes, bør studenten supplere med en gjennomgått kopi uten passord eller nøkler. Eksakt leveringsfrist, leveringskanal, særskilt regel-fasit og eventuell annen sensorveiledning for refleksjonsdelen er fortsatt ikke mottatt. Malen alene avklarer ikke disse spørsmålene.
