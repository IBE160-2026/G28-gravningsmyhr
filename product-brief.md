# Product Brief: Beer Game

**Gruppe:** G28-gravningsmyhr  
**Emne:** IBE160 Programmering med KI

## Executive Summary

Beer Game er en AI-støttet webapplikasjon som skal gjøre det enklere å lære om forsyningskjeder gjennom praktisk simulering. Studenten tar beslutninger om bestillinger og ser hvordan disse påvirker lager, leveranser og kostnader over tid. Målet er å forstå bullwhip-effekten: at variasjoner i bestillinger kan forsterkes gjennom forsyningskjeden.

Løsningen skal kunne brukes både individuelt og i undervisning. Regelbaserte medspillere fyller de øvrige spillerrollene og gir tilbakemeldinger basert på gjennomførte spill. Tilgangen til språkmodeller gjør det mulig å kombinere digitale medspillere med personlige forklaringer, mens lærere får bedre støtte til organisering og oppfølging.

## The Problem

Den tradisjonelle simuleringen krever fire roller: detaljist, grossist, distributør og fabrikk. Når rollene må fylles av mennesker samtidig, blir gjennomføringen avhengig av deltakernes tilgjengelighet. Fravær kan forsinke en gruppe og gjøre det vanskelig å ta igjen en økt.

Fysiske spill krever også manuell registrering og sammenstilling av resultater. Etterpå kan studentene sitte igjen med tall og grafer uten å forstå sammenhengen mellom egne valg og resultatet. For læreren tar organisering, analyse og individuell oppfølging tid. Selvstendige brukere trenger en måte å prøve simuleringen uten å samle en hel gruppe.

## The Solution

Vi skal utvikle en nettbasert simulering hvor brukeren spiller én rolle og legger inn bestillinger gjennom flere perioder. De øvrige rollene styres i v1 av regelbaserte medspillere. Flerspiller med mennesker utsettes etter faglærers tilbakemelding. Spillbildet viser studentens lokale lagerbeholdning, restordre, bestillinger, leveranser og kostnader. Etter avslutning vises hele kjeden. Spillstatus lagres slik at en økt kan gjenopptas.

Etter spillet viser grafer utviklingen gjennom forsyningskjeden. En AI-generert oppsummering knytter forklaringer til brukerens faktiske beslutninger og resultater. Læreren skal kunne opprette en klasse med invitasjonskode og følge tilknyttede studenters progresjon og resultater. Slik blir gjennomføring og refleksjon en sammenhengende læringsaktivitet.

## What Makes This Different

Det finnes allerede digitale alternativer, blant annet [MIT Sloan Beer Game Online](https://mitsloan.mit.edu/teaching-resources-library/mit-sloan-beer-game-online), som beskrives som en interaktiv flerspillersimulering, og [IIOM Online Single Player Beer Game](https://iiom-web.org/beergame/play.php), som tilbyr solo-spill. Solo er derfor ikke et unikt særpreg. Vårt planlagte fokus er en norsk læringsflyt med tydelige regelbaserte medspillere, gjenopptak og databasert KI-refleksjon. Dette er en prosjektprioritering, ikke en dokumentert overlegenhet over alternativene. Kildene er lest 3. november 2026. AI reduserer behovet for å koordinere fire deltakere, mens personlige forklaringer gjør resultatene mer relevante enn en generell oppsummering for hele klassen.

Sammenlignet med fysisk gjennomføring samler løsningen også spilldata automatisk og gjør oppfølging enklere. Verdien ligger i å kombinere kjent simuleringslogikk, AI og lærerfunksjoner på en brukervennlig måte.

## Who This Serves

**Studenter innen logistikk, økonomi og forsyningskjedestyring** er primærbrukerne. De trenger å kunne gjennomføre spillet og forstå hvordan egne valg påvirker hele kjeden. For dem er suksess å gjenkjenne bullwhip-effekten i egne resultater.

**Lærere** trenger å organisere spill og følge studentenes progresjon med mindre manuelt arbeid. **Individuelle brukere og fagpersoner** skal kunne utforske forsyningskjededynamikk uten å delta i et organisert kurs.

## Success Criteria

Første versjon skal vurderes ut fra om:

- En bruker kan fullføre et spill med AI i de øvrige rollene.
- Bestillinger, lager, restordre, leveranser og kostnader beregnes og vises korrekt.
- Spillstatus bevares ved avbrudd, og spillet kan gjenopptas.
- Visualiseringene gjør det mulig å identifisere bullwhip-effekten i spilldataene.
- AI-oppsummeringen bygger på brukerens registrerte beslutninger og resultater.
- En lærer kan opprette spill og følge studentenes progresjon.

Ved utprøving i undervisning er målet fra prosjektgrunnlaget at minst 80 % av studentene viser bedre forståelse i en vurdering før og etter spillet. Dette er et mål som må undersøkes, ikke et dokumentert resultat.

## Scope

**Innenfor første versjon:** Registrering og innlogging, solo-simulering med fire klassiske roller og tre regelbaserte medspillere, lagring og gjenopptak, resultatgrafer, KI-generert sluttoppsummering med reservefunksjon uten nøkkel og enkel lærervisning for egne klasser. Studenten er primærbruker. Lokal kjøring skal fungere uten betalte tjenester.

**Utenfor første versjon:** Flerspiller med mennesker, sanntidssynkronisering, språkmodellstyrte medspillere, avansert læreradministrasjon, Egen mobilapp, avansert scenario-editor, rangeringer og belønningssystemer, prediktive analyser, sosial deling, avansert gjenavspilling og strategianalyse, flerspråklig støtte og integrasjon med Canvas eller Moodle.

Første versjon skal prioritere at brukeren kan gjennomføre spillet og forstå resultatene. Detaljerte funksjonskrav og tekniske valg beskrives senere i PRD og arkitektur.

## Vision

På kort sikt skal Beer Game bli en fungerende og brukervennlig læringssimulering for både individuell øving og undervisning. Dersom løsningen lykkes, kan den over to til tre år utvikles til en plattform for flere simuleringer innen logistikk og driftsledelse.

Videreutviklingen kan omfatte AI-genererte vurderingsoppgaver basert på spilldata og integrasjon med læringsplattformer. Visjonen er at AI skal støtte læring som medspiller og veileder, slik at flere kan forstå komplekse sammenhenger gjennom egne beslutninger.

## Revisjon 3. november 2026

Omfanget er redusert etter faglærers tilbakemelding 6. oktober: solo er kjernen, lærerfunksjonene forenkles og medspillerne er regelbaserte. Se [PRD](docs/planning/prd.md), [brukerflyt](docs/planning/ux.md), [arkitekturforslag](docs/planning/architecture.md) og [utviklingsoppgaver](docs/planning/stories.md). Spillparametre er foreløpige prosjektvalg. Revisjonen er KI-utarbeidet på studentens bestilling og innebærer ikke faglærergodkjenning.
