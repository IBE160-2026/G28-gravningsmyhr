# Arkitekturforslag for Beer Game

> Historisk forslag. Implementert arkitektur og begrunnede avvik står i [arkitekturbeslutningen](../implementation.md).

Dato: 3. november 2026. Status: planleggingsforslag som må valideres i oppstartsoppgaven. Ingen programvare er installert i prosjektet gjennom dette dokumentet.

## Valg og begrunnelse
Foreslått stack er Next.js med TypeScript for visning og server, og Supabase for PostgreSQL og autentisering. Én webapplikasjon på Vercel reduserer behovet for separat backend-hosting. Spillmotoren er en ren TypeScript-modul uten database, nettverk eller modellkall. Språkmodellleverandør velges senere; reserveoppsummeringen bygges først.

Lokal kjøring bruker samme database- og autentiseringstype gjennom lokal Supabase-stack. På Windows krever denne stacken Supabase CLI og en Docker-kompatibel containerruntime. Det er gratis lokal drift, men et reelt installasjonsbehov som README må beskrive. Ingen SQLite-fil skal brukes som varig lagring på Vercel. Nøyaktige avhengighetsversjoner låses når oppstarten faktisk er testet.

## Komponenter
Nettleser -> Next.js server -> spilltjeneste -> spillmotor
Spilltjeneste -> PostgreSQL
Innlogging -> Supabase Auth
Sluttrapport -> oppsummeringstjeneste -> regelbasert tekst eller valgfri språkmodell

Nettleseren får bare tillatt visning av eget spill. Motoren arbeider med full kjedetilstand på serveren. En grafklient mottar full historikk først når spillet er avsluttet, eller når lærerens tillatte resultattilgang er kontrollert.

## Datamodell
- profiles: bruker-ID, visningsidentifikator, rolle.
- classes: ID, lærer-ID, navn og invitasjonskode.
- games: ID, eier-ID, klasse-ID eller null, studentens spillrolle, regelversjon, konfigurasjon, bekreftet periode, versjon og full tilstand.
- game_periods: spill-ID, periode og historikk for fire ledd. Unik kombinasjon av spill og periode.
- game_commands: spill-ID, unik forespørsels-ID, forventet versjon, bestillingsverdi og resultatversjon.
- summaries: spill-ID, dataversjon, status, kilde og tekst. Unik vellykket oppsummering per dataversjon.

Tilstand inkluderer lager, restordre, alle ordrekøer, transport og produksjon, kostnad og tidligere beslutninger. JSON kan brukes til versjonert motortilstand; relasjonelle eierskapsfelt brukes for tilgang.

## Transaksjon og periodekontrakt
GET av spill beregner et beslutningspunkt fra bekreftet tilstand uten å mutere databasen. POST sender bestilling, forventet versjon og en stabil forespørsels-ID.
Serveren kontrollerer identitet og eierskap, validerer input og beregner neste tilstand. En databasefunksjon skriver tilstand, historikk og kommando i én transaksjon med kontroll av forventet versjon. Ingen serverløs prosess beholder lås eller tilstand mellom forespørsler.
Samme forespørsels-ID med samme innhold returnerer tidligere resultat; gjenbruk med annet innhold avvises. Utdatert versjon gir konflikt, ikke en ekstra periode. Unike nøkler og låsing eller betinget oppdatering håndheves i databasen, ikke bare i brukergrensesnittet.

## Autentisering og tilgang
Nettversjonen bruker ekte innlogging. Lærerrolle gis administrativt og kan ikke endres av brukeren selv. Server og database kontrollerer at student eier spillet, og at lærer eier spillets klasse. Kontoer har studentrolle som standard.
Full motortilstand er ikke direkte lesbar fra nettleseren. Databasens tilgangsregler og serverrespons må testes sammen. Privilegert databasetilgang holdes på serveren; eventuelle privilegerte rutiner har eksplisitte eierskapskontroller og begrensede rettigheter.
Demoidentiteter er kun lokale og kan ikke aktiveres i produksjon. Lokal demo skal bruke lokal autentisering eller en strengt lokalt avgrenset adapter. Verifiser dette gjennom en egen negativ produksjonstest.

## Oppsummering og drift
Spill kan avsluttes uten modell. Første rapport er regelbasert; valgfri KI bruker kun relevante tall uten navn og e-post. Tidsavbrudd og modellfeil ødelegger ikke resultatvisningen.
Modellkall er autorisert, begrenset og gjenbruker lagret resultat. Bruk en databasebasert status/lås med utløp slik at parallelle sidevisninger ikke utløser ubegrensede kall. Modellnavn, kostnadstak og endelig køstrategi avklares før integrasjon.
Miljøvariabler og migrasjoner dokumenteres. Preview og produksjon skal ikke ukritisk dele ekte studentdata. Logger bruker spill-ID og feilkategori, ikke passord, token eller fulle personopplysninger.

## Foreslått struktur
```text
src/app/                 sider og serverendepunkter
src/domain/game/         typer, regler og ren spillmotor
src/server/              tilgang, lagring og oppsummering
src/components/          visningskomponenter
supabase/migrations/     skjema, tilgangsregler og transaksjoner
supabase/seed.sql         lokale demonstrasjonsdata
tests/                   fasit, integrasjon og brukerflyt
docs/planning/           PRD, UX, arkitektur og stories
```

## Validering før bygging
Opprett en minimal lokal app med lokal Supabase. Bekreft lokal innlogging og en transaksjon, bygg lokalt og prøv en Vercel-forhåndsvisning når konto er tilgjengelig. Lås først da versjoner og skriv faktiske oppstartskommandoer. Ingen slik test er utført i denne dokumentøkten.

## Primærkilder
- [Next.js installasjon og TypeScript-oppsett](https://nextjs.org/docs/app/getting-started/installation)
- [Supabase lokal utvikling og containerkrav](https://supabase.com/docs/guides/local-development)

Kildene er lest 3. november 2026. Foreslått anvendelse og datamodell er prosjektets egne designvalg. Tilgangspolicyer og transaksjoner må kontrolleres mot offisiell dokumentasjon under implementering.
