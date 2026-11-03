# Refleksjonsrapport for Beer Game

**Emne:** IBE160 26H Programmering med KI  
**Gruppe:** G28-gravningsmyhr  
**Student:** Andreas Iden-Gravningsmyhr  
**Dato:** 3. november 2026  
**Status:** KI-assistert utkast basert på dokumentert arbeid og studentens uttalelser. Må leses av studenten og kontrolleres mot den endelige innleveringsoppgaven før levering.

## Prosjektet og målet

Prosjektet er en nettbasert variant av Beer Game. Brukeren velger én av rollene detaljist, grossist, distributør eller fabrikk og tar bestillingsbeslutninger gjennom 20 perioder. De andre rollene følger faste regler. Appen viser lager, restordre, leveranser og kostnader, lagrer progresjonen og viser grafer og en oppsummering etter avslutning. En enkel lærerfunksjon knytter spill til klasser.

Målet er å gjøre det mulig å utforske forsyningskjeder uten å samle fire spillere samtidig. Resultatene skal hjelpe brukeren å undersøke sammenhengen mellom bestillinger, leveringstid, lagermangel og kostnader. Vi har ikke målt om brukerne lærer mer, og en fungerende simulering dokumenterer ikke i seg selv en læringseffekt.

## Hvordan KI ble brukt

Jeg har brukt KI til både planlegging, implementering, testing, dokumentasjon og veiledning under publisering. Arbeidet startet med produktbeskrivelsen. Faglærers tilbakemelding ble senere brukt til å redusere omfanget og konkretisere en PRD med funksjonskrav og akseptansekriterier. KI utarbeidet brukerflyt, et arkitekturforslag og en oppdeling i utviklingsoppgaver.

KI skrev selve programkoden og de automatiske testene. KI-agenten utførte også nettlesertester og rettet feil. Jeg fulgte veiledningen for å flette endringene inn i GitHub, opprette Supabase-prosjekt og publisere via Vercel. Skjermbilder fra oppsettet ble brukt som kontekst for videre veiledning. Dermed bestod mitt dokumenterte bidrag særlig av å bestille og styre arbeidet, avklare valg og gjennomføre konto- og publiseringssteg etter veiledning. Dette er ikke en påstand om at jeg har skrevet koden selv eller selvstendig kontrollert alle beregningene.

En viktig forskjell er KI som utviklingsverktøy og KI som funksjon inne i appen. Utviklingsprosessen er KI-assistert. Medspillerne inne i appen er derimot regelbaserte. Den nåværende sluttoppsummeringen er også regelbasert. Det finnes en valgfri Claude-integrasjon i koden, men jeg valgte å beholde den gratis oppsummeringen foreløpig. Ekte modellrefleksjon er derfor ikke aktivert eller dokumentert som prøvd.

## Omfang og tekniske beslutninger

Den opprinnelige planen var omfattende og inkluderte flerspiller med mennesker og flere lærerfunksjoner. Faglærers tilbakemelding anbefalte solo som kjernen i første versjon. Flerspiller ble derfor utsatt. Regelbaserte medspillere gjør at spillet kan kjøres uten modellkostnad og at like forutsetninger gir samme resultat.

Det første arkitekturforslaget beskrev Next.js og Supabase Auth. Implementasjonen ble senere endret til en Python-server og et JavaScript-grensesnitt uten egen byggeprosess. Lokal kjøring bruker SQLite, mens den publiserte løsningen bruker PostgreSQL via Supabase. Vercel kjører serverkoden. Endringen gjør den lokale løsningen enkel å starte, men krever at dokumentasjonen forklarer avviket fra forslaget.

Lagringen bruker én samlet tilstand i en databasetransaksjon. Dette forenkler konsistens og gjenopptak, men begrenser kapasiteten ved mange samtidige brukere. Det er en konkret avveining i et lite undervisningsprosjekt. En videreutvikling bør dele dataene i flere tabeller og skille språkmodellkall fra den låste spilltilstanden.

## Kvalitetssikring og konkrete erfaringer

Det er ikke tilstrekkelig at KI produserer kode som ser riktig ut. Testgrunnlaget er derfor koblet til spillregler og sentrale brukerhandlinger. I den avsluttende agentkontrollen bestod 19 automatiske tester. De omfatter blant annet ordreledetid, transport, produksjon, inputgrenser, kostnadssummer, eierskap, klasseavgrensning, gjenopptak og samtidige forespørsler. Et separat regneoppsett kontrollerer åtte perioder med varierende bestillinger for hver spillerrolle.

Alle fire roller ble spilt gjennom 20 perioder på den publiserte siden av KI-agenten. Lærerflyten ble testet med lokale testkontoer: lærer opprettet klasse, student knyttet spillet til klassen, og lærer åpnet resultatet. En annen lærer fikk ikke opp klassens spill. Resultatvisningen ble kontrollert på 360, 768 og 1440 piksler, og sentrale deler av spillflyten ble prøvd med tastatur.

Et konkret problem oppstod ved første publisering. Vercel viste en publisert side, men appen svarte med en tjenestefeil. KI-agenten la databasepakken eksplisitt til i prosjektets avhengigheter og forbedret feilkategoriene. Etter ny publisering fungerte registrering, lagring og gjenopptak. Den opprinnelige serverfeilen ble ikke identifisert fra en rå serverlogg, så årsaken bør ikke beskrives sikrere enn det dokumentasjonen støtter.

En annen erfaring var at nettleserverktøyet ikke alltid kunne styre Brave sikkert. Da fortsatte oppsettet med at jeg delte skjermbilder og fulgte trinnvise instruksjoner. Dette viser at også verktøytilgangen, ikke bare språkmodellens evner, påvirker hvor selvstendig KI kan arbeide.

Disse kontrollene ble utført av KI-agenten. De er nyttige, men de erstatter ikke en uavhengig faglig gjennomgang eller dokumentasjon av mine egne brukerprøver. Detaljert teststatus og kjente begrensninger finnes i repoet.

## Min opplevelse og læring

Jeg har ikke opplevd noe som vanskelig i arbeidet så langt. Min tydeligste erfaring er at KI kan gjøre svært mye, forutsatt at man bruker avanserte nok modeller. I dette prosjektet har KI håndtert mange forskjellige oppgaver, fra planlegging og kode til testing og hjelp med publisering.

Denne erfaringen må samtidig avgrenses. At arbeidsprosessen oppleves enkel for meg, betyr ikke at løsningen er feilfri. Publiseringsfeilen viser at et vellykket bygg ikke alene dokumenterer en fungerende applikasjon. Testene og de konkrete prøvene er derfor viktige når jeg vurderer sluttresultatet.

Prosjektet gir også grunnlag for å skille mellom modell, kontekst, prompt og verktøy. Modellkapasitet betyr mye, men agenten trengte også produktbeskrivelsen, lærerens tilbakemelding, tydelige krav, tilgang til GitHub og informasjon fra skjermbildene. Jeg kan derfor ikke konkludere med at en sterkere modell alene er nok til å sikre kvalitet.

## Etiske og teknologiske vurderinger

Ansvar for resultatet forsvinner ikke når koden er KI-generert. Innleveringen må være åpen om hvilke deler KI har produsert og hvilke vurderinger studenten faktisk har gjort. Det ville være misvisende å framstille agentens tester som mine egne eller å etterkonstruere en utviklingsprosess som ikke fant sted.

Brukerkontoer og klasseoversikter gjør tilgangskontroll og personvern relevante. Læreren skal bare se egne klassers spill, og studentene skal ikke se hverandres data. Hemmeligheter må holdes utenfor det offentlige repoet. Kontoenes manglende e-postverifisering, passordgjenoppretting og selvbetjente sletting gjør at løsningen foreløpig bør brukes med testdata. Videre bruk med reelle studenter krever avklart dataoppbevaring og kontoforvaltning.

En regelbasert oppsummering er forutsigbar og gratis å kjøre, men mindre fleksibel enn en språkmodell. En språkmodell kan gi mer varierte forklaringer, men kan også skrive uriktige påstander og innebærer behandling av data hos en ekstern leverandør. Valget om å beholde gratis oppsummering reduserer disse avhengighetene, men betyr at denne delen av den opprinnelige KI-ambisjonen er utsatt.

## Resultat og videre arbeid

Prosjektet har en publisert, kjørbar kjerneflyt og dokumenterte tester. Planleggingen er koblet til implementasjonen, og endringer i omfang og arkitektur er beskrevet. Arbeidet viser at KI kan utføre store deler av et utviklingsprosjekt, samtidig som testing og tydelig dokumentasjon er nødvendig for å vurdere resultatet.

Før innlevering må studenten lese rapporten og prøve løsningen selv, kontrollere emnets endelige krav og frist og ta stilling til de dokumenterte avgrensningene. Spillreglene er en prosjektvariant som ennå ikke er kontrollert mot en særskilt fasit fra undervisningen. Det er ikke gjennomført en brukerundersøkelse eller måling av læringsutbytte.

## Dokumentgrunnlag

- [Produktbeskrivelse](../product-brief.md) og [faglærers tilbakemelding](../tilbakemelding-product-brief.md).
- [PRD](planning/prd.md), [implementasjon og beslutninger](implementation.md).
- [Testresultater](testing.md), [utvidet regnekontroll](reference-extended.md) og [leveransestatus](leveransestatus.md).
- Studentens uttalelser i samtalen 3. november 2026 om egen opplevelse og læring, samt valget om gratis oppsummering.

Rapportutkastet er formulert med KI-støtte. Den endelige oppgaveteksten og overordnet sensorveiledning for refleksjonsdelen er ikke tilgjengelige i dette arbeidet.
