class Lexicon:

    # Wait Pages
    group_wait_page_text = "Esperando a los otros participantes. Por favor, permanece en esta página. ¿Esperando mucho tiempo? Intenta a actualizar la página."

    # Consent
    participant_info_title = "Hoja de información del participante"
    participant_consent_title = "Consentimiento"
    demographic_data_title = "Datos demográficos"
    consent_question = "Estoy de acuerdo en participar en este estudio y acepto los términos y condiciones mencionadas con los puntos anteriores. Si no estás de acuerdo, sal cerrando el navegador. Por favor, ten en cuenta que no recibirás el pago si decides salir"
    yes = "Sí"
    age_question = "¿Cuál es tu edad (años)?"
    prefer_not_to_say = "Prefiero no decirlo"
    gender_question = "¿Cuál es tu género?"
    female = "Mujer"
    male = "Hombre"
    non_binary = "No binario"
    other = "Otro"
    worker_id_question = "Por favor, introduzca aquí su identificación universitaria"

    # Esfuerzo
    effort_intro_title = "Juego"
    add_numbers_title = "Tarea de Aritmética Mental"
    effort_results_title = "Resultados"
    number_entered_question = "Número introducido"
    timer_text = "Tiempo total restante"

    # quiz
    quiz_instructions_title = "Cómo funciona el juego"
    quiz_title = "Cuestionario previo al partido"
    quiz_results_title = "Respuestas correctas"
    quiz_group_assigned_title = "Asignación de presupuesto"
    quiz_final_message_title = "Preparación final"
    quiz_error_message = "Tu respuesta a la pregunta {} fue incorrecta. Vuelve a leer la pregunta e inténtalo de nuevo."

    private_question = "1) ¿Cuánto en UM tendría que invertir cada jugador en su cuenta privada para resolver el problema de forma privada?"
    public_question = "2) En promedio, ¿cuánto en total (en UM) tendría que invertir cada jugador del grupo en la cuenta del grupo para resolver el problema como grupo, que cuesta 160UM?"
    success_question = "3) Si resuelven el problema como grupo invirtiendo colectivamente 160UM en la cuenta del grupo, y te quedan 20UM, ¿cuánto en UM te quedarán al final del juego?"
    failure_question = "4) Si no consigues resolver el problema como grupo, y no inviertes lo suficiente en tu cuenta privada para resolver el problema de forma privada, ¿cuánto en UM te quedarán al final del juego?"
    fair_rich_question = "5) ¿Cuál crees que sería una contribución total justa a la cuenta del grupo por parte de los jugadores más ricos (que empiezan el juego con 120UM)?"
    fair_poor_question = "6) ¿Cuál crees que sería una contribución total justa a la cuenta del grupo por parte de los jugadores más pobres (que empiezan el juego con 80UM)?"

    # Juego
    contribution_title = "Contribución"
    group_result_title = "Resultado del grupo"
    contribution_private_question = "¿Cuánto en UM te gustaría invertir en tu cuenta privada en esta ronda?"
    contribution_public_question = "¿Cuánto en UM te gustaría invertir en la cuenta del grupo en esta ronda?"
    error_total_contribution_greater_than_funds = "Tu contribución total no puede superar tus fondos restantes."
    error_total_contribution_greater_than_20 = "Tu contribución total en cada ronda no puede superar las 20 UM"

    # Pago
    payment_thank_you_title = "Gracias"
    WVS_luck_label = "Pregunta 1"
    WVS_luck_left = "1: A la larga, esforzarse en el trabajo suele llevar a una vida mejor."
    WVS_luck_right = "10: Esforzarse en el trabajo no suele llevar al éxito—eso depende más de la suerte y los contactos."
    WVS_responsibility_label = "Pregunta 2"
    WVS_responsibility_left = "1: El Gobierno debería asumir más responsabilidad en proporcionar un medio de vida a todo el mundo."
    WVS_responsibility_right = "10: Cada uno debería asumir individualmente más responsabilidad para lograr su propio medio de vida."

    # Extra Demographics
    # Spanish normal: "¿Cuál de las siguentes opciones describe mejor tu ingreso del hogar el año pasado, antes de impuestos? Si vives con tus padres durante las vacaciones universitarias, deberías incluir los ingresos de ellos."
    # Colombian version: "Si vives con tus padres de forma permanentemente o si te encuentras en el período de vacaciones universitarias, deberías incluir los ingresos de ellos."
    ExtraDemographics_income_label = "¿Cuál de las siguentes opciones describe mejor tu ingreso del hogar el año pasado, antes de impuestos? Si vives con tus padres de forma permanentemente o si te encuentras en el período de vacaciones universitarias, deberías incluir los ingresos de ellos."
    ExtraDemographics_income_choices = [
        "$0 to $38.999.999",
        "$39.000.000 to $52.999.999",
        "$53.000.000 to $69.999.999",
        "$70.000.000 to $97.999.999",
        "$98.000.000 o más",
        "Prefiero no decirlo"
    ]
    ExtraDemographics_field_of_study_label = "Cuál es tu disciplina de estudio?"
    humanities = "Humanidades (e.g., Arte, Historia, Lenguaje, Leyes, Filosofía)"
    economics = "Sciencias sociales: Economiá"
    psychology = "Sciencias sociales: Psicología"
    social_science_other = "Sciencias sociales: Otro"
    natural_science = "Sciencias naturales (e.g., Biología, Química, Física)"
    applied_science = "Sciencias aplicadas (e.g., Negocio, Educación, Medicina)"
    science_other = "Otras sciencias (e.g., Computación, Matemáticas)"
    other = "Otro"
    ExtraDemographics_macarthur_ladder_label = "La escalera representa dónde se para la gente en la sociedad. " \
                                               "En la cima está la gente más rica, que tiene más dinero, mejor educación, " \
                                               "y mejores trabajos. En el fondo está la gente más pobre, que tiene menos dinero, " \
                                               "menos educación, y los peores trabajos, o está desempleada. " \
                                               "Por favor, elige el número que representa dónde te ubicarías en la escalera."

    telefono = "Número de teléfono:"
    telefono2 = "Por favor repite tu número de teléfono:"
    telefono_error_message = "Los números de teléfono no son iguales."
    metodopago = "Indica el método preferido de pago:"
    metodopago_choices = [
        "DaviPlata",
        "Nequi",
        "Forma de pago presencial: Jueves, 2 de marzo de 12:30pm a 1:30pm - facultad de economía (te enviaremos más información sobre la sala exacta por correo)",
        "Forma de pago presencial: Viernes, 3 de marzo de 9:30am a 10:30am - facultad de economía (te enviaremos más información sobre la sala exacta por correo)"
    ]