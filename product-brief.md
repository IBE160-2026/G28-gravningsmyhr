# Product Brief: Beer Game

**Gruppe:** G28-gravningsmyhr  
**Emne:** IBE160 Programmering med KI

## Executive Summary

Beer Game er en AI-støttet webapplikasjon som skal gjøre det enklere å lære om forsyningskjeder gjennom praktisk simulering. Studenten tar beslutninger om bestillinger og ser hvordan disse påvirker lager, leveranser og kostnader over tid. Målet er å forstå bullwhip-effekten: at variasjoner i bestillinger kan forsterkes gjennom forsyningskjeden.

Løsningen skal kunne brukes både individuelt og i undervisning. AI fyller ledige spillerroller og gir tilbakemeldinger basert på gjennomførte spill. Tilgangen til språkmodeller gjør det mulig å kombinere digitale medspillere med personlige forklaringer, mens lærere får bedre støtte til organisering og oppfølging.

## The Problem

Den tradisjonelle simuleringen krever fire roller: detaljist, grossist, distributør og fabrikk. Når rollene må fylles av mennesker samtidig, blir gjennomføringen avhengig av deltakernes tilgjengelighet. Fravær kan forsinke en gruppe og gjøre det vanskelig å ta igjen en økt.

Fysiske spill krever også manuell registrering og sammenstilling av resultater. Etterpå kan studentene sitte igjen med tall og grafer uten å forstå sammenhengen mellom egne valg og resultatet. For læreren tar organisering, analyse og individuell oppfølging tid. Selvstendige brukere trenger en måte å prøve simuleringen uten å samle en hel gruppe.

## The Solution

Vi skal utvikle en nettbasert simulering hvor brukeren spiller én rolle og legger inn bestillinger gjennom flere perioder. De øvrige rollene kan fylles av mennesker eller AI. Et samlet spillbilde viser lagerbeholdning, restordre, bestillinger, leveranser og kostnader. Spillstatus lagres slik at en økt kan gjenopptas.

Etter spillet viser grafer utviklingen gjennom forsyningskjeden. En AI-generert oppsummering knytter forklaringer til brukerens faktiske beslutninger og resultater. Læreren skal kunne opprette spill for studenter og følge progresjonen. Slik blir gjennomføring og refleksjon en sammenhengende læringsaktivitet.

## What Makes This Different

Kombinasjonen av AI-spillere og tilbakemelding fra egne spilldata er løsningens viktigste særpreg. AI reduserer behovet for å koordinere fire deltakere, mens personlige forklaringer gjør resultatene mer relevante enn en generell oppsummering for hele klassen.

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

**Innenfor første versjon:** Registrering og innlogging, simulering med de fire klassiske rollene, spill alene med AI og flerspiller med mennesker og/eller AI. Versjonen skal ha oversikt over spillets utvikling, lagring av spillstatus, resultatvisualisering, AI-generert sluttoppsummering og grunnleggende støtte for lærere og klasser.

**Utenfor første versjon:** Egen mobilapp, avansert scenario-editor, rangeringer og belønningssystemer, prediktive analyser, sosial deling, avansert gjenavspilling og strategianalyse, flerspråklig støtte og integrasjon med Canvas eller Moodle.

Første versjon skal prioritere at brukeren kan gjennomføre spillet og forstå resultatene. Detaljerte funksjonskrav og tekniske valg beskrives senere i PRD og arkitektur.

## Vision

På kort sikt skal Beer Game bli en fungerende og brukervennlig læringssimulering for både individuell øving og undervisning. Dersom løsningen lykkes, kan den over to til tre år utvikles til en plattform for flere simuleringer innen logistikk og driftsledelse.

Videreutviklingen kan omfatte AI-genererte vurderingsoppgaver basert på spilldata og integrasjon med læringsplattformer. Visjonen er at AI skal støtte læring som medspiller og veileder, slik at flere kan forstå komplekse sammenhenger gjennom egne beslutninger.
