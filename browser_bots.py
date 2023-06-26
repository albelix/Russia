import os
import time
from threading import Thread

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException        
from selenium.webdriver.chrome.options import Options


def restart_room(session_name="consent", n_participants=12, heroku=False):

	if heroku:
		room_management_url = "https://privatepublic.herokuapp.com/room_without_session/solutions"
	else:
		room_management_url = "http://localhost:8000/room_with_session/solutions"

	driver = webdriver.Firefox()
	driver.get(room_management_url)

	try:
		username_input = driver.find_element(By.ID, "id_username")
		username_input.send_keys("admin")
		password_input = driver.find_element(By.ID, "id_password")
		password_input.send_keys("orangezebra")
		login_button = 	driver.find_element(By.ID, "btn-login")
		login_button.click()
	except:
		pass

	driver.get(room_management_url)

	try:
		close_button = 	driver.find_element(By.ID, "close-room")
		close_button.click()
	except selenium.common.exceptions.NoSuchElementException:
		pass

	select_session_config = Select(driver.find_element(By.ID, 'session_config'))
	select_session_config.select_by_value(session_name)


	input_n_participants = driver.find_element(By.ID, "num_participants")
	input_n_participants.send_keys(n_participants)

	create_button = driver.find_element(By.ID, "btn-create-session")
	create_button.click()




def run_consent_one_bot(bot_index, driver=None):

	if not driver:
		local_url = "http://localhost:8000/room/solutions?participant_label=sub{:02d}".format(bot_index)		
		driver = webdriver.Firefox()
		driver.get(local_url)

	running = True
	while running:

		# Participant Info page
		try:
			next_button = driver.find_element(By.CLASS_NAME, "otree-btn-next")
			next_button.location_once_scrolled_into_view
			next_button.click()
		except:
			pass

		# Consent Page
		try:
			consent_radio= driver.find_element(By.ID, "id_consent-0")
			consent_radio.click()
			next_button = driver.find_element(By.CLASS_NAME, "otree-btn-next")
			next_button.location_once_scrolled_into_view
			next_button.click()
		except:
			pass

		try:
			# Demographic Data
			select_age = Select(driver.find_element(By.ID, 'id_age'))
			select_age.select_by_value('35-44')

			select_gender = Select(driver.find_element(By.ID, 'id_gender'))
			select_gender.select_by_value('Other')

			next_button = driver.find_element(By.CLASS_NAME, "otree-btn-next")
			next_button.click()
			running = False
		except:
			pass


def run_consent_one_group():

	os.system("pkill firefox")
	restart_room("consent")

	threads = []
	for bot_index in range(1,5):
		t = Thread(target=run_consent_one_bot, args=(bot_index,))
		threads.append(t)
		t.start()


def run_effort_one_bot(bot_index, driver=None):

	if not driver:
		local_url = "http://localhost:8000/room/solutions?participant_label=sub{:02d}".format(bot_index)
		driver = webdriver.Firefox()
		driver.get(local_url)

	# Keep looping through until we get to the end
	running = True
	while running:
		time.sleep(2)

		try:
			effort_intro_flag = driver.find_element(By.ID, "effort-intro-flag")
			next_button = driver.find_element(By.CLASS_NAME, "otree-btn-next")
			next_button.location_once_scrolled_into_view
			next_button.click()
		except:
			pass


		try:
			effort_add_flag = driver.find_element(By.ID, "effort-add-flag")
			effort_entry = driver.find_element(By.ID, "id_number_entered")
			effort_entry.send_keys('123')
			next_button = driver.find_element(By.CLASS_NAME, "otree-btn-next")
			next_button.click()
		except:
			pass

		try:
			effort_results_flag = driver.find_element(By.ID, "effort-results-flag")
			next_button = driver.find_element(By.CLASS_NAME, "otree-btn-next")
			next_button.click()
			running = False
		except:
			pass


def run_effort_one_group():

	os.system("pkill firefox")
	restart_room("effort")

	threads = []
	for bot_index in range(1,5):
		t = Thread(target=run_effort_one_bot, args=(bot_index,))
		threads.append(t)
		t.start()


def run_quiz_one_bot(bot_index, driver=None):


	if not driver:
		local_url = "http://localhost:8000/room/solutions?participant_label=sub{:02d}".format(bot_index)
		driver = webdriver.Firefox()
		driver.get(local_url)

	running = True
	
	"""
	Run through pages using try except blocks
	Most of them jsut require a clisk "Next"
	Quiz requires correct answers
	If last page is found, the running is set to False. 

	"""
	while running:
		time.sleep(2)

		try:
			next_button = driver.find_element(By.CLASS_NAME, "otree-btn-next")
			next_button.click()
		except:
			pass

		try:
			quiz_radio_1= driver.find_element(By.ID, "id_private-3")
			quiz_radio_1.click()

			quiz_radio_2= driver.find_element(By.ID, "id_public-2")
			quiz_radio_2.click()

			quiz_radio_3= driver.find_element(By.ID, "id_success-1")
			quiz_radio_3.click()

			quiz_radio_4= driver.find_element(By.ID, "id_fail-0")
			quiz_radio_4.click()

			quiz_fair_rich = driver.find_element(By.ID, "id_fair_rich")
			quiz_fair_rich.send_keys(bot_index+1)

			quiz_fair_poor = driver.find_element(By.ID, "id_fair_poor")
			quiz_fair_poor.send_keys(bot_index+2)

			next_button = driver.find_element(By.CLASS_NAME, "otree-btn-next")
			next_button.location_once_scrolled_into_view
			next_button.click()
		except:
			pass

		try:
			quiz_last_page_flag = driver.find_element(By.ID, "quiz-finish-flag")
			next_button = driver.find_element(By.CLASS_NAME, "otree-btn-next")
			next_button.click()
			running = False
		except:
			pass




def run_quiz_one_group():

	os.system("pkill firefox")
	restart_room("quiz")

	threads = []
	for bot_index in range(1,5):
		t = Thread(target=run_quiz_one_bot, args=(bot_index,))
		threads.append(t)
		t.start()

def run_game_one_bot(bot_index, driver=None):

	if not driver:

		local_url = "http://localhost:8000/room/solutions?participant_label=sub{:02d}".format(bot_index)
		driver = webdriver.Firefox()
		driver.get(local_url)

	running = True
	
	"""
	Run through pages using try except blocks
	Most of them jsut require a clisk "Next"
	Quiz requires correct answers
	If last page is found, the running is set to False. 

	"""
	while running:
		time.sleep(2)

		try:
			next_button = driver.find_element(By.CLASS_NAME, "otree-btn-next")
			next_button.click()
		except:
			pass

		try:
			quiz_fair_rich = driver.find_element(By.ID, "id_contribution_private")
			quiz_fair_rich.send_keys("2")

			quiz_fair_poor = driver.find_element(By.ID, "id_contribution_public")
			quiz_fair_poor.send_keys("1")

			next_button = driver.find_element(By.CLASS_NAME, "otree-btn-next")
			next_button.location_once_scrolled_into_view
			next_button.click()
		except:
			pass

		try:
			game_last_page_flag = driver.find_element(By.ID, "game-finished-flag")
			next_button = driver.find_element(By.CLASS_NAME, "otree-btn-next")
			next_button.click()
			running = False
		except:
			pass


def run_game_one_group():

	os.system("pkill firefox")
	restart_room("game")

	threads = []
	for bot_index in range(1,5):
		t = Thread(target=run_game_one_bot, args=(bot_index,))
		threads.append(t)
		t.start()

def run_payment_one_bot(bot_index, driver=None):

	if not driver:
		local_url = "http://localhost:8000/room/solutions?participant_label=sub{:02d}".format(bot_index)
		driver = webdriver.Firefox()
		driver.get(local_url)

	running = True
	
	"""
	Run through pages using try except blocks
	Most of them jsut require a clisk "Next"
	Quiz requires correct answers
	If last page is found, the running is set to False. 

	"""
	while running:
		time.sleep(2)

		# WVS Page
		try:
			wvs_radio_1 = driver.find_element(By.ID, "id_WVS_luck-1")
			wvs_radio_1.click()

			wvs_radio_2 = driver.find_element(By.ID, "id_WVS_responsibility-3")
			wvs_radio_2.click()
		except:
			pass

		try:	
			email = driver.find_element(By.ID, "id_email_address")
			email.send_keys("test@gmail.com")
		except:
			pass
		
		try:
			next_button = driver.find_element(By.CLASS_NAME, "otree-btn-next")
			next_button.click()
		except:
			pass

		# Extra Demographics
		# Demographic Data
		try:
			select_ladder = Select(driver.find_element(By.ID, 'id_macarthur_ladder'))
			select_ladder.select_by_value('9')

			select_gender = Select(driver.find_element(By.ID, 'id_income'))
			select_gender.select_by_value('Prefer not to answer')

			select_field_study = Select(driver.find_element(By.ID, 'id_field_of_study'))

			next_button = driver.find_element(By.CLASS_NAME, "otree-btn-next")
			next_button.click()
		except:
			pass

		try:
			payment_last_page_flag = driver.find_element(By.ID, "payment-finished-flag")
			running = False
		except:
			pass


def run_payment_one_group():

	os.system("pkill firefox")
	restart_room("payment")

	threads = []
	for bot_index in range(1,5):
		t = Thread(target=run_payment_one_bot, args=(bot_index,))
		threads.append(t)
		t.start()


def run_full_one_bot(bot_index=1, heroku=False, dropout=None):

	if heroku:
		app_url = "https://privatepublic.herokuapp.com/room/solutions?participant_label=sub{:02d}".format(bot_index)
	else:
		app_url = "http://localhost:8000/room/solutions?participant_label=sub{:02d}".format(bot_index)
	
	driver = webdriver.Firefox()
	driver.get(app_url)


	run_consent_one_bot(bot_index=bot_index, driver=driver)
	if dropout == "Effort":
		driver.close()
		return None
	run_effort_one_bot(bot_index=bot_index, driver=driver)

	if dropout == "Quiz":
		driver.close()
		return None
	run_quiz_one_bot(bot_index=bot_index, driver=driver)

	if dropout == "Game":
		driver.close()
		return None
	run_game_one_bot(bot_index=bot_index, driver=driver)
	run_payment_one_bot(bot_index=bot_index, driver=driver)

	driver.close()


def run_full(heroku=False):

	n_participants=8
	os.system("pkill firefox")
	restart_room("full_experiment", n_participants=n_participants, heroku=heroku)

	threads = []
	for bot_index in range(1,n_participants+1):
		t = Thread(target=run_full_one_bot, args=(bot_index,heroku))
		threads.append(t)
		t.start()


def run_with_odd_number_of_players(heroku=False):

	room_size = 12
	n_participants=6
	os.system("pkill firefox")
	restart_room("full_experiment", n_participants=room_size, heroku=heroku)

	threads = []
	for bot_index in range(1,n_participants+1):
		t = Thread(target=run_full_one_bot, args=(bot_index,heroku))
		threads.append(t)
		t.start()


def run_with_dropouts(heroku=False):

	room_size = 12
	n_participants=12
	os.system("pkill firefox")
	restart_room("full_experiment", n_participants=room_size, heroku=heroku)

	threads = []
	for bot_index in range(1,n_participants-2):
		t = Thread(target=run_full_one_bot, args=(bot_index,heroku))
		threads.append(t)
		t.start()

	# Drooputs	
	t = Thread(target=run_full_one_bot, args=(bot_index+1,heroku, "Effort"))
	threads.append(t)
	t.start()

	t = Thread(target=run_full_one_bot, args=(bot_index+2,heroku, "Quiz"))
	threads.append(t)
	t.start()

	t = Thread(target=run_full_one_bot, args=(bot_index+3,heroku, "Game"))
	threads.append(t)
	t.start()


if __name__=="__main__":
	run_full()