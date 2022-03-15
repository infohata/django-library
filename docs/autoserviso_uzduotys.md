# Užduotis: Autoservisas
Sukurti programą su Django framework'u, kuri leistų įvesti autoservisų informaciją:

* Paslaugas (pavadinimu, pvz. Alyvos keitimas, stabdžių kaladėlių keitimas ir pan.)
* Paslaugų kainas (su paslauga ir jos kaina)
* Automobilių modelius (su metais, markėmis, modeliais ir varikliais)
* Automobiliais (konkrečiais, su automobilio ID, klientu (pradžiai - stringu), valstybiniu numeriu, VIN kodu)
* Taisymo užsakymus (automobiliu, bendra suma ir atskiromis eilutėmis su atliktomis paslaugomis, kiekiais ir kainomis)

![](autoservisas.png)

## 1. Projektas, modelis

* Dirbame Github'e, public repozitorija
* Sukurti naują Django projektą su appsu Autoservice
* Sukurti visus modelius pagal nurodytą programos DB struktūrą
* Sukurti meniu punktus visiems sukurtiems modeliams
* Susikurti superuser vartotoją, prisijungti ir išbandyti įrašyti visų modelių įrašus
* Visus užrašus, kintamuosius (kiek įmanoma) aprašyti anglų kalba.
* Padaryti vertimus, kad perjungus iš anglų kalbos į lietuvių, automatiškai išsiverstų visi užrašai.

## 2. Adminas, modelių duomenų manipuliavimas, filtrai

* Padaryti, kad modelių pavadinimai būtų atvaizduojami teisingai (vienaskaita ir daugiskaita)
* Padaryti, kad užsakymo formoje būtų matomos ir užsakymo eilutės (į jas galima būtų įrašyti informaciją)
* Padaryti, kad užsakymo sąraše būtų matomi automobilio ir datos stulpeliai
* Padaryti, kad automobilių sąraše būtų matomi kliento, automobilio, valstybinio numerio ir VIN numerio stulpeliai
* Padaryti, kad Paslaugų sąraše būtų matomi paslaugos pavadinimų ir kainų stulpeliai
* Į Automobilių sąrašą įdėti filtrą pagal klientą ir automobilio modelį*
* Į Automobilių sąrašą įdėti paiešką pagal valstybinį numerį ir VIN kodą

## 3. Šablonai, statika, base.html

* Padaryti, kad programa matytų templates ir static katalogus
* Padaryti nukreipimas iš puslapio "/" į "/autoservice" (redirect)
* Pridėti pasirenkamą statuso lauką į užsakymų modelį
* Sukurti puslapį (ne admin), kuriame būtų matoma statistika: paslaugų kiekis, atliktų užsakymų kiekis, automobilių kiekis
* Susikurti savo puslapio stilių (base.html failą). Jei reikia, pridėkite css ir kitus failus (patartina naudoti bootstrap). Palite panaudoti paskaitoje rodytus pavyzdžius. Panaudokite frontend kurse išmoktas žinias! :)
* Padaryti mygtukus (arba pasirinkimą), kuris leistų pasirinkti puslapio kalbą.

## 4. Views

* Sukurti puslapį (per funkciją views faile), pvz. autoservice/automobiliai, kuriame būtų atvaizduoti visi servise užregistruoti automobiliai.
* Paspaudus ant automobilio nuorodos, būtų rodoma detali informacija apie automobilį (savininkas, automobilio modelis, valstybinis numeris, VIN kodas)
* Sukurti puslapį (per klasę views faile), pvz. autoservice/uzsakymai, kuriame būtų atvaizduoti visi vykdomi serviso užsakymai.
* Paspaudus ant užsakymo nuorodos, būtų rodoma detali informacija apie užsakymą. Čia pat būtų matomos ir užsakymo eilučių informacija.

## 5. Paieška, nuotraukos, puslapiavimas

* Padaryti, kad įrašai užsakymų puslapyje būtų puslapiuojami (per klasę).
* Padaryti, kad įrašai automobilių puslapyje būtų puslapiuojami (per funkciją).
* Puslapyje įdėti paieškos laukelį, kuris ieškotų automobilių pagal savininką, modelį, valstybinį numerį, VIN kodą
* Padaryti, kad prie automobilio įrašo galima būtų pridėti nuotrauką ir ji būtų atvaizduojama automobilių puslapyje

## 6. Autorizacija

* Padaryti, kad pagrindiniame puslapyje būtų rodomas sesijos apsilankymų skaičius.
* Padaryti login puslapį, per kurį leistų prisijungti vartotojui.
* Jei reikia, perdaryti base.html meniu, kad prisijungimo punkto nerodytų prisijungus, atsijungimo atsijungus ir pan.
* Susikonfiguruoti el. paštą slaptažodžio keitimui.
* Susikurti savo siunčiamo el. laiško šabloną (keičiant slaptažodį).
* Pakeisti visus administracinius slaptažodžio keitimo puslapius savo formomis (kaip šios paskaitos medžiagoje).

## 7. Vartotojo specifiniai veiksmai

* Į užsakymo modelį įdėti vartotojo lauką (ForeignKey su User, kaip paskaitoje).
* Į užsakymo modelį įdėti automobilio gražinimo termimo lauką.
* Į administratoriaus puslapį pridėti šiuo du laukus.
* Į užsakymo modelį įdėti @property metodą, kuris pasibaigus automobilio gražinimo terminui, gražintų True.
* Padaryti meniu punktą "Mano Užsakymai", kuris vestų į puslapį, kuriame prisijungęs vartotojas galėtų matyti tik savo užsakymus.
* Padaryti, kad jei automobilio gražinimo laikas praėjo, užsakymas būtų pažymimas raudona spalva.
* Į automobilio (konkretaus, su savininku, valstybiniu numeriu, VIN kodu) modelį įdėti aprašymo lauką. Jame būtų leidžiama įvesti html kodą (padaryti teksto redagavimą su tinyMCE).
* Padaryti, kad HTML aprašymas būtų teisingai atvaizduojamas automobilio formoje (puslapyje, ne admin).

## 8. Vartotojo registracija, login/logout

* Padaryti vartotojo registracijos formą pagal šioje pamokoje išmoktus žingsnius.
* Prie užsakymo eilutės modelio pridėti lauką sumą (per @property), kuri būtų automatiškai paskaičiuota, padauginus kiekį iš kainos.
* Pakeisti, kad užsakymo laukas suma būtų automatiškai paskaičiuojamas pagal realias užsakymo eilučių sumas
* Padaryti, kad prisijungusiam vartotojui leistų palikti komentarus prie savo užsakymų (administratorius galėtų atsakyti į komentarus per administratoriaus puslapį).

## 9. Vartotojo profilis
* Sukurti naują su vartotoju susietą profilio modelį su nuotraukos lauku, įdėti jį į admin ir išbandyti.
* Padaryti naują profilio puslapį, kuriame būtų atvaizduojamas profilio vardas, el. pašto adresas ir nuotrauka. Jei nuotrauka neprisegta, būtų rodoma default nuotrauka (ją reikia įdėti į media katalogą).
* Padaryti, kad sukūrus vartotoją, būtų automatiškai sukurtas ir jo profilis.
* Padaryti, kad profilio puslapyje būtų galima redaguoti vartotojo informaciją, pakeisti nuotrauką.
* Padaryti, kad prisegta profilio nuotrauka būtų automatiškai sumažinama iki norimo dydžio (pagal dizainą).
* Padaryti, kad vartotojo nuotrauka būtų matoma prie kiekvieno užsakymo, užsakymų sąraše.


## 10. CRUD

* Jei reikia, perdaryti vartotojo užsakymų puslapius į ListView ir DetailView klases.
* Padaryti, kad prisijungęs vartotojas galėtų kurti naujus užsakymus (be eilučių, tik pasirinkęs automobilį ir terminą). Panaudoti CreateView
* Padaryti, kad prisijungęs vartotojas galėtų redaguoti savo užsakymus. Panaudoti UpdateView
* Padaryti, kad prisijungęs vartotojas galėtų ištrinti savo užsakymus. Panaudoti DeleteView
