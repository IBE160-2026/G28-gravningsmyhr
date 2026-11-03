# Brukerflyt og skjermskisser for Beer Game

Dato: 3. november 2026. Status: forslag, ikke brukertestet.

## Formål
Studenten skal forstå hva som skjer i sin rolle, gjøre én beslutning per periode og undersøke konsekvensene etterpå. Begrepene lager, restordre og varer underveis forklares der de brukes.

## Oversikt
```text
Beer Game                          Mine spill | Hjelp | Logg ut
Øv på bestillinger i en forsyningskjede
[Start nytt spill]

Dine spill
Detaljist   Periode 6 av 20   Sist lagret ...   [Fortsett]
Grossist   Fullført          Kostnad ...      [Se resultat]
```
Ingen spill: forklar startknappen. Lastefeil: vis ny prøveknapp og ikke en feilaktig tom liste. Lokal modus får synlig demoetikett.

## Nytt spill
Velg rolle med fire navngitte alternativer. Vis standardreglene og at medspillerne er regelbaserte. Klassekode er valgfri; forklar lærerens innsyn før tilknytning. [Start spill] oppretter ett spill og tar brukeren videre til periode 1.

## Spillbilde
```text
Periode 6 av 20                              [Mine spill]
Fabrikk -> Distributør -> Grossist -> [Detaljist] -> Kunde
Din rolle: Detaljist

Denne perioden: mottatt leveranse ... | ny etterspørsel ...
Etter utlevering: lager ... | restordre ... | varer underveis ...
Kostnad denne perioden ... | samlet kostnad ...

Hvor mye vil du bestille? [     ] enheter
[Bekreft bestilling og avslutt periode 6]
Egen historikk [Vis]
```
Tallene er serverens klargjorte beslutningspunkt, ikke en ny lagring. Bestillingen gjelder neste ledds senere mottak. Første periode får samme forklaring. Knappen deaktiveres mens bekreftelsen behandles, men serveren må også hindre dobbeltføring. Etter lagring vises en bekreftelse; feil bevarer input og lar brukeren prøve igjen. Ved versjonskonflikt hentes oppdatert spill før ny beslutning. Ikke vis andre ledds skjulte verdier i HTML eller API-respons underveis.

## Resultater
Vis fullført status og samlet kjedekostnad, deretter kostnad per ledd. Gi separate grafer for bestillinger, lager og restordre, med periode på x-aksen og enhet på y-aksen. Vis også etterspørsel og tilsvarende datatabeller. Ikke bland kostnader og antall på én umerket akse.
Oppsummeringen har etikett «KI-generert» eller «Regelbasert oppsummering». Tallgrunnlaget for viktige observasjoner skal være synlig. Ikke lov at spillet alltid demonstrerer økt variasjon.
[Start nytt spill] endrer ikke det fullførte spillet.

## Lærer
Lærer velger egen klasse, kopierer invitasjonskode og ser en tabell med studentidentifikator, spillrolle, periode, status og kostnad. Bare fullførte spill har full resultatvisning. Aktive spill viser progresjon og oppnådd kostnad, ikke en falsk sluttrapport. Andre læreres klasser er utilgjengelige.

## Tilgjengelighet og kontroll
Synlig tastaturfokus, etiketter, tekstlige feil og lesbar kontrast. Fokus flyttes til en kort periodebekreftelse etter lagring. Oppsummeringsområdet annonserer lastestatus uten å flytte fokus uventet. Mobile nøkkeltall stables; brede datatabeller kan rulles. Kontroll på 360, 768 og 1440 px, tastatur og forstørret tekst føres som faktiske tester ved implementering.

Krav: F01–F14 og K03–K05 i [PRD](prd.md). Ingen skjerm er implementert.
