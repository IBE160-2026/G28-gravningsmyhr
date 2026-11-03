# Sluttkontroll og dokumentasjon

## 2026-11-03 — KI-assistent på bestilling fra Andreas

### Oppgave
Brukeren ba om å gjennomføre sluttarbeidet. Studenten oppga at ingenting hadde vært vanskelig og at erfaringen var at avanserte KI-modeller kan gjøre det meste. Studenten valgte å beholde gratis oppsummering foreløpig.

### Plan
Kontroller fire fulle spill på nett, lærerflyt lokalt, beregninger og tilgang. Rett funn og oppdater dokumentene. Utarbeid refleksjonsutkast ut fra faktiske aktiviteter og studentens egne uttalelser.

### Resultat
Implementasjonscommit 49d72b05fea5b6ebdcca5c0515906d53efdaa23b. 19 automatiske tester består lokalt. Separat ankomstmatrise-kalkulator kontrollerer åtte perioder for fire roller. Nye HTTP-tester dekker samtidighet, replay, eierskap og input.
Offentlig fullføring med bestilling 4 ga kjedesummer 754, 3820, 10232 og 17600 for detaljist, grossist, distributør og fabrikk. Lokal beregning ga samme tall.
Lokal nettleser kontrollerte læreropprettet klasse, studenttilknytning, 20 perioder, lærerens resultatinnsyn og at annen lærer ikke så spillet. Ingen produksjonslærerrolle ble tildelt.
Resultater kontrollert på 360/768/1440 px og spillbilde på 360 uten horisontal dokumentoverflyt. Tastaturprøver bekreftet Tab/Enter og fokus til statusmelding.
Databaseforbindelsen lukkes også ved initialiseringsfeil. Graflegende bruker samme linjefarger og mønstre som grafen.
PRD og brief beskriver utsatt KI-refleksjon etter studentens valg. Refleksjonsrapportutkast, leveransestatus, testresultater og regnegrunnlag finnes i docs. Rapporten tilskriver ikke agentens tester til studenten.
Tidligere GitHub Actions-kjøringer på Python 3.12 bestod; den nye kjøringen kontrolleres separat.
En lang dokumentkommando ble avvist av automatisk godkjenning. Dokumentendringene ble deretter utført med filredigeringsverktøyet uten shellkommandoen.

### Åpne punkter
Passordrotasjon og Vercel-verdi må studenten håndtere privat. Endelig Canvas-oppgave, frist og emnets spillfasit er ikke tilgjengelige. Refleksjonsutkastet må leses av studenten, og egne brukerprøver mangler. Kontoforvaltning og dataoppbevaring må avklares før bruk med reelle studentdata. Ingen Canvas-innlevering eller faglærergodkjenning er utført.
