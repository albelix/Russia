class Lexicon:

    # Wait Pages
    group_wait_page_text = "Waiting for the other participants. Please stay on this browser and do not click away. Waiting a long time? Try refreshing the page."

    # Consent
    participant_info_title = "Participant Information Sheet"
    participant_consent_title = "Consent"
    demographic_data_title = "Demographic Data"
    consent_question = "I have read and I agree with the points above. If you do not agree then please exit by closing the browser. Please note: you will not receive payment if you choose to exit."
    yes = "Yes"
    age_question = "What is your age (years)?"
    prefer_not_to_say = "Prefer not to say"
    gender_question = "What is your gender?"
    female = "Female"
    male = "Male"
    non_binary = "Non-binary"
    other = "Other"
    worker_id_question = "Please enter your university ID here."

    # Effort
    effort_intro_title = "Overview"
    add_numbers_title = "Mental Arithmetic Task"
    effort_results_title = "Results"
    number_entered_question = "Number Entered"
    timer_text = "Total time left"

    # quiz
    quiz_instructions_title = "How the Game Works"
    quiz_title = "Pre-Game Quiz"
    quiz_results_title = "Correct Answers"
    quiz_group_assigned_title = "Budget Assignment"
    quiz_final_message_title = "Final Preparation"
    quiz_error_message = "Your response to Question {} was incorrect. Please re-read the question and try again."

    private_question = "1) How much in MU would each player have to invest in their private account to solve the problem privately?"
    public_question = "2) On average, how much in total (in MU) would each player in the group have to invest in the group account to solve the problem as a group, which costs 160MU?"
    success_question = "3) If you solve the problem as a group by collectively investing 160MU into the group account, and you have 20MU remaining, how much in MU do you get to keep at the end of the game?"
    failure_question = "4) If you fail to solve the problem as a group, and you fail to invest enough in your private account to solve the problem privately, how much in MU do you get to keep at the end of the game?"
    fair_rich_question = "5) What do you think would be a fair total contribution to the group account from richer players (who start the game with 120MU)?"
    fair_poor_question = "6) What do you think would be a fair total contribution to the group account from poorer players (who start the game with 80MU)?"

    # Game
    contribution_title = "Contribution"
    group_result_title = "Group Result"
    contribution_private_question = "How much in MU would you like to invest in your private account in this round?"
    contribution_public_question = "How much in MU would you like to invest in the group account in this round?"
    error_total_contribution_greater_than_funds = "Your total contribution cannot exceed your remaining funds."
    error_total_contribution_greater_than_20 = "Your total contribution in each round cannot exceed 20 MU."

    # Payment (WVS translations to be taken from https://www.worldvaluessurvey.org/WVSDocumentationWV7.jsp)
    payment_thank_you_title = "Thank you"
    WVS_luck_label = "Question 1"
    WVS_luck_left = "1 = In the long run, hard work usually brings a better life"
    WVS_luck_right = "10 = Hard work doesn't generally bring success - it's more a matter of luck and connections"
    WVS_responsibility_label = "Question 2"
    WVS_responsibility_left = "1 = The government should take more responsibility to ensure that everyone is provided for" 
    WVS_responsibility_right = "10 = People should take more responsibility to provide for themselves"

    # Extra Demographics
    ExtraDemographics_income_label = "Which of the following best describes your household income last year, before tax? If you live with your parents outside of university terms, please include your parents’ income in your response."
    ExtraDemographics_income_choices = [
        "£0 to £19,999",
        "£20,000 to £26,999",
        "£27,000 to £35,999",
        "£36,000 to £49,999",
        "£50,000 or more",
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
    telefono_error_message = "Los números de teléfono no son iguales."
    metodopago = "Indica el método preferido de pago:"
    metodopago_choices = [
        "DaviPlata",
        "Nequi",
        "Forma de pago presencial (más información del día y horario te llegará por correo electrónico)"
    ]
