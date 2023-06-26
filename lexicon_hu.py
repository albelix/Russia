class Lexicon:

    # Wait Pages
    group_wait_page_text = "A többi résztvevőre várunk. Kérjük, hogy maradjon ebben a böngészőben, és ne kattintson el. Régóta vár? Próbálja meg frissíteni az oldalt."

    # Consent
    participant_info_title = "Tájékoztató"
    participant_consent_title = " Beleegyezés"
    demographic_data_title = " Demográfiai adatok"
    consent_question = " Elolvastam, és egyetértek a fenti pontokkal. Ha nem ért egyet, akkor kérjük, hogy lépjen ki a böngésző bezárásával. Felhívjuk figyelmét, hogy nem kap kifizetést, ha úgy dönt, hogy kilép."
    yes = "Igen"
    age_question = "Hány éves?"
    prefer_not_to_say = "Inkább nem árulom el"
    gender_question = "Mi a neme?"
    female = "Nő"
    male = "Férfi"
    non_binary = "Nem-bináris"
    other = "Egyéb"
    worker_id_question = "Kérjük, itt adja meg az e-mail címet, amivel regisztrált."

    # Effort
    effort_intro_title = "Áttekintés"
    add_numbers_title = "Fejszámoló feladat"
    effort_results_title = "Eredmények"
    number_entered_question = "Beírt szám"
    timer_text = "Teljes hátralévő idő"

    # quiz
    quiz_instructions_title = "Hogyan működik a játék?"
    quiz_title = "Játék előtti kvíz"
    quiz_results_title = "Helyes válaszok"
    quiz_group_assigned_title = "Induló pénzegység mennyiség"
    quiz_final_message_title = "A felkészítés utolsó pontja"
    private_question = "1) Mennyi pénzegységet kellene minden játékosnak az egyéni számlájára utalnia, hogy egyedül megoldja a problémát?"
    public_question = "2) Átlagosan fejenként mennyi pénzegységet kellene a csoport minden tagjának a csoportszámlára utalnia, hogy csoportként megoldják a problémát, amely 160 pénzegységbe kerül?"
    success_question = "3) Ha csoportként oldják meg a problémát úgy, hogy együttesen 160 pénzegységet utalnak a csoportszámlára, és Ön 20 pénzegységet nem költ el, akkor mennyi pénzegységgel zárja a játékot?"
    failure_question = "4) Ha nem sikerül csoportként megoldani a problémát, és nem utal eleget az egyéni számlájára ahhoz, hogy egyedül oldja meg a problémát, akkor mennyi pénzegységgel zárja a játékot?"
    fair_rich_question = "5) Mit gondol, mi lenne a gazdagabb játékosok (akik 120 pénzegységgel kezdik a játékot) méltányos teljes befizetése a csoportszámlára?"
    fair_poor_question = "6) Mit gondol, mi lenne a szegényebb játékosok (akik 80 pénzegységgel kezdik a játékot) méltányos teljes befizetése a csoportszámlára?"

    # Game
    contribution_title = "Befizetés"
    group_result_title = "Csoporteredmény"
    contribution_private_question = " Mennyi pénzegységet kíván az egyéni számlájára utalni ebben a körben?"
    contribution_public_question = "Mennyi pénzegységet kíván a csoportszámlára utalni ebben a körben?"
    error_total_contribution_greater_than_funds = "A befizetése nem lehet több, mint az eddig el nem költött pénze."
    error_total_contribution_greater_than_20 = "Az összbefizetése egyik körben sem lehet több 20 pénzegységnél."

    # Payment (WVS translations to be taken from https://www.worldvaluessurvey.org/WVSDocumentationWV7.jsp)
    payment_thank_you_title = "Köszönjük!"
    WVS_luck_label = "1. kérdés"
    WVS_luck_left = "1 = Hosszú távon a kemény munka rendszerint jobb életet hoz."
    WVS_luck_right = "10 = A kemény munka általában nem hoz sikert – rendszerint ez inkább a szerencse és a kapcsolatok kérdése."
    WVS_responsibility_label = "2. kérdés"
    WVS_responsibility_left = "1 = Az államnak nagyobb felelősséget kellene vállalnia az emberekről való gondoskodásban."
    WVS_responsibility_right = "10 = Az embereknek nagyobb felelősséget kellene vállalniuk abban, hogy gondoskodjanak önmagukról."

    # Extra Demographics
    ExtraDemographics_income_label = "Az alábbiak közül melyik kategória jellemzi legjobban háztartásának tavalyi, adózás előtti havi átlagos összjövedelmét? Ha az egyetemi időszakon kívül a szüleivel él, kérjük, a szülei havi átlagos összjövedelmét adja meg válaszában."
    ExtraDemographics_income_choices = [
        "0Ft.",
        "1Ft.-tól 200,000Ft.-ig.",
        "200,000Ft.-tól 500,000Ft.-ig",
        "450,000Ft-tól 900,000Ft.-ig",
        "900,000Ft.-tól 1,400,000Ft.-ig",
        "1,400,000Ft-tól 2,000,000Ft.-ig",
        "2,000,000Ft. felett",
        "Inkább nem válaszolok"
        ]
    ExtraDemographics_field_of_study_label = "Milyen szakon tanul jelenleg?"
    humanities = "Bölcsészettudományok (pl. művészetek, történelem, nyelvek, jog, filozófia)"
    economics = "Társadalomtudomány: közgazdaságtan"
    psychology = "Társadalomtudomány: pszichológia"
    social_science_other = "Társadalomtudomány (egyéb)"
    natural_science = "Természettudomány (pl. biológia, kémia, fizika)"
    applied_science = "Alkalmazott tudomány (pl. üzleti tudományok, oktatás, orvostudomány)"
    science_other = "Egyéb tudományok (pl. számítástechnika, matematika)"
    other = "Egyéb"
    ExtraDemographics_macarthur_ladder_label = "A létra azt jelzi, hogy az emberek hol állnak a „társadalmi ranglétrán”. A létra tetején azok állnak, akik a legjobb helyzetben vannak, akiknek a legtöbb pénzük, a legmagasabban iskolázottak és a legjobb állásuk van. Az alján azok állnak, akiknek a legrosszabb helyzetük van, akiknek a legkevesebb a pénzük, legalacsonyabb a képzettségük, legrosszabb állásuk van, vagy nincs is állásuk. Kérjük, válassza ki azt a fokot, amely a legjobban tükrözi, hogy Ön hol áll a létrán."

    telefono = "Número de teléfono:"
    telefono2 = "Por favor repite tu número de teléfono:"
    telefono_error_message = "Los números no son iguales."
    metodopago = "Indica el método preferido de pago:"
    metodopago_choices = [
        "DaviPlata",
        "Nequi",
        "Forma de pago presencial (más información del día y horario te llegará por correo electrónico)"
    ]