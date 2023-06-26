class Lexicon:

    # Wait Pages
    group_wait_page_text = "Aspetta gli altri partecipanti. Per favore rimani sul browser e non cambiare pagina. Se ti sembra di aspettare da troppo tempo prova a ricaricare la pagina."

    # Consent
    participant_info_title = "Foglio informativo per i partecipanti"
    participant_consent_title = "Consenso informato"
    demographic_data_title = "Dati demografici"
    consent_question = "Ho letto e sono d’accordo con i punti di cui sopra. Se non sei d’accordo, per favore esci dalla pagina chiudendo il browser. Nota bene: non riceverai il pagamento se deciderai di uscire."
    yes = "Si"
    age_question = "Quanti anni hai?"
    prefer_not_to_say = "Preferisco non rispondere"
    gender_question = "Quale è il tuo genere?"
    female = "Femmina"
    male = "Maschio"
    non_binary = "Non-binario"
    other = "Altro"
    worker_id_question = "Per favore inserisci il codice della tua matricola qui."

    # Effort
    effort_intro_title = "Panoramica"
    add_numbers_title = "Esercizio aritmetico mentale"
    effort_results_title = "Risultati"
    number_entered_question = "Numero inserito"
    timer_text = "Tempo rimanente"

    # quiz
    quiz_instructions_title = "Come funziona il gioco"
    quiz_title = "Quiz"
    quiz_results_title = "Risposte corrette"
    quiz_group_assigned_title = "Assegnazione del budget"
    quiz_final_message_title = "Preparazione finale"

    private_question = "1) Quante UM ogni giocatore dovrebbe investire nel proprio conto personale per risolvere il problema privatamente?"
    public_question = "2) In media, ogni giocatore quanto dovrebbe investire (in UM) in totale nel conto di gruppo per risolvere il problema come gruppo, il quale costa 160UM?"
    success_question = "3) Se risolvi il problema come gruppo investendo collettivamente 160UM nel conto di gruppo, e ti rimangono 20UM, quante UM ti rimarranno da convertire alla fine del gioco?"
    failure_question = "4) Se fallite nel risolvere il problema come gruppo, e fallisci nell’investire sufficientemente nel tuo conto privato per risolvere il problema privatamente, quante UM ti rimangono da convertire alla fine del gioco?"
    fair_rich_question = "5) Quale pensi sia un contributo equo al conto di gruppo per un giocatore più ricco (che inizia il gioco con 120UM)?"
    fair_poor_question = "6) Quale pensi sia un contributo equo al conto di gruppo per un giocatore più povero (che inizia il gioco con 80UM?"

    # Game
    contribution_title = "Contributo"
    group_result_title = "Risultato di gruppo"
    contribution_private_question = "Quante UM vorresti investire nel tuo conto privato in questo turno?"
    contribution_public_question = "Quante UM vorresti investire nel conto di gruppo in questo turno?"
    error_total_contribution_greater_than_funds = "Il tuo contributo totale non può eccedere i tuoi fondi rimanenti."
    error_total_contribution_greater_than_20 = "Il tuo contributo totale per ogni turno non può eccedere le 20 UM."

    # Payment (WVS translations to be taken from https://www.worldvaluessurvey.org/WVSDocumentationWV7.jsp)
    payment_thank_you_title = "Grazie"
    WVS_luck_label = "Domanda n°1"
    WVS_luck_left = "1 = Nel lungo termine, il lavoro duro solitamente determina una vita migliore"
    WVS_luck_right = "10 = Il lavoro duro non determina solitamente il successo - è più una questione di fortuna e connessioni."
    WVS_responsibility_label = "Domanda n°2"
    WVS_responsibility_left = "1 = Il governo dovrebbe prendere maggiore responsabilità per assicurarsi che tutti possano mantenersi"
    WVS_responsibility_right = "10 = Le persone dovrebbero prendere maggiore responsabilità per mentenere se stessi"

    # Extra Demographics
    ExtraDemographics_income_label = "Which of the following best describes your household income last year, before tax? If you live with your parents outside of university terms, please include your parents’ income in your response."
    ExtraDemographics_income_choices = [
        "£0 to £13,299",
        "£13,300 to £20,499",
        "£20,500 to £26,799",
        "£26,800 to £35,699",
        "£35,700 to £53,999",
        "£54,000 or more",
        "Prefer not to answer"
    ]
    ExtraDemographics_field_of_study_label = "In which field is your current subject of study?"
    humanities = "Humanities (e.g., Arts, History, Languages, Law, Philosophy)"
    economics = "Social science: Economics"
    psychology = "Social science: Psychology"
    social_science_other = "Social science (Other)"
    natural_science = "Natural science (e.g., Biology, Chemistry, Physics)"
    applied_science = "Applied science (e.g., Business, Education, Medicine)"
    science_other = "Other science (e.g., Computer Science, Mathematics)"
    other = "Other"
    ExtraDemographics_macarthur_ladder_label = "The ladder represents where people stand in society. At the top of the ladder are the people who are the best off, those who have the most money, most education, and best jobs. At the bottom are the people who are the worst off, those who have the least money, least education, worst jobs, or no job. Please choose the number that best represents where you think you stand on the ladder."

    # Don't need to translate
    telefono = "Número de teléfono:"
    telefono2 = "Por favor repite tu número de teléfono:"
    telefono_error_message = "Los números no son iguales."
    metodopago = "Indica el método preferido de pago:"
    metodopago_choices = [
        "DaviPlata",
        "Nequi",
        "Forma de pago presencial (más información del día y horario te llegará por correo electrónico)"
    ]