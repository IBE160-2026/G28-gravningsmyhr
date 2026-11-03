# Epics og utviklingsoppgaver for Beer Game

Dato: 3. november 2026. Status: planlagt, ingen oppgaver er implementert.
Krav-ID-er viser til [PRD](prd.md). Oppgavene tas i rekkefølge med egne faktiske endringer og validering.

| Epic | Story | Krav | Akseptansekriterier og kontroll |
|---|---|---|---|
| E1 Grunnlag | S01 Oppstart og lokal database | F14, K01, K10 | Next.js og lokal Supabase starter fra README; lokal innlogging og én prøvetransaksjon virker. Versjoner låses. Demo er avvist ved produksjonskonfigurasjon. |
| E1 Grunnlag | S02 Referanseforløp | M2, F05–F06 | Dokumenter 5–10 perioder med alle fire ledd, ordre, transport og produksjon. Kontroller manuelt med en separat beregning; ikke generer forventningsverdier fra motoren under test. |
| E2 Simulering | S03 Spillmotor | F03–F06, K01 | Ren motor med versjonert konfigurasjon; tester bekrefter referanseforløpet, alle fire studentroller og grenseverdier. |
| E2 Simulering | S04 Beslutningspunkt | F04, F07, K04 | Vis lokal tilstand etter utlevering og før bestilling. GET endrer ingen tilstand. Skjulte data mangler i responsen. |
| E3 Lagring | S05 Transaksjoner og gjenopptak | F05, F08, K02, K09 | Tilstand, køer og historikk lagres samlet. Dobbeltklikk, gjentatt ID, endret payload og konkurrerende faner testes. Oppfriskning gjenoppretter nøyaktig tilstand. |
| E3 Lagring | S06 Konto og eierskap | F01–F02 | To studenter kan ikke se eller endre hverandres spill. Test direkte server- og databaseforespørsler. Utlogging avslutter tilgang. |
| E4 Studentflyt | S07 Oversikt og spill | F03–F08, K03–K06 | Spill i alle fire roller kan fullføres via grensesnittet. Tomtilstand, ugyldig input og lagringsfeil fungerer. Kontroller tastatur og tre skjermbredder. |
| E4 Studentflyt | S08 Resultater | F09, M4 | Grafpunkter og tabeller stemmer med historikken. Fullførte spill er skrivebeskyttet. Vis restordre og varer underveis ved slutt. |
| E5 Refleksjon | S09 Reserveoppsummering | F11, K08 | Faktabaserte observasjoner virker uten modellnøkkel og er tydelig merket regelbasert. |
| E5 Refleksjon | S10 Valgfri KI-oppsummering | F10–F11, K07 | Bruk serverkall med avgrensede data, tidsgrense, kostnadsbegrensning og gjenbruk. Test parallelle forespørsler, feil og timeout. Kontroller tekstens påstander manuelt. |
| E6 Lærer | S11 Klasse og tilknytning | F12, F02 | Lærerrolle tildeles kontrollert. Klassekode knytter nytt spill til klasse etter informasjon om innsyn. Ugyldig kode avvises. |
| E6 Lærer | S12 Læreroversikt | F13, M6 | To lærere ser bare egne klasser. Aktive spill viser progresjon; fullførte viser resultater. Studentbeslutninger kan ikke endres av lærer. |
| E7 Levering | S13 Ren oppstart og publisering | F14, K10, M7 | En annen gjennomgang følger README i rent miljø; testkommandoer virker uten modellnøkkel. Vercel-kjerneflyt kontrolleres og URL legges til etter faktisk deploy. |

## Avhengigheter
S02 før godkjenning av S03. S01 og S03 før S05. S05 og S06 før offentlig tilgjengelig studentflyt. S08 før S09 og S10. S06 før S11 og S12. S13 krever at v1-funksjonene og relevante kontroller faktisk er ferdige.

## Felles ferdigkriterier
Story peker til krav, oppfyller akseptansekriteriene, har relevante tester og dokumentert faktisk resultat. Kode og dokumentasjon samsvarer. KI-forslag som endres eller avvises beskrives når det faktisk skjer. Ingen oppgave markeres ferdig bare fordi kode er generert.

## Beredskap før første implementering
Planleggingen kan brukes til å starte S01. Spillreglene er fortsatt en prosjektvariant som må kontrolleres mot undervisningskrav. Fullkjedefasit og teknisk oppstartsvalidering mangler. Dette er åpne oppgaver, ikke en bestått readiness-vurdering.
