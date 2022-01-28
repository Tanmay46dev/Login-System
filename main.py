def check_acc_existance(username, password):
	with open("accounts.txt") as f:
		for line in f.readlines():
			line = line.replace(" ", "").replace("\n", "")
			acc_details = line.split("-")
			if username == acc_details[0] and password == acc_details[1]:
				return True
	return False

def get_user_credentials():
	username = input("Username: ")
	password = input("Password: ")
	
	return {"username": username, "password": password}

def create_ac(username, password):
	with open('accounts.txt', 'a') as f:
		f.write(f"{username} - {password}\n")
	print("Account created successfuly!!")


def main():
	ans = input("Would you want to log in or create an account? (login/create): ")

	credentials = get_user_credentials()
	username = credentials.get("username")
	password = credentials.get("password")

	acc_already_exists = check_acc_existance(username, password)

	if ans == 'login':
		if acc_already_exists:
			print("Logged in successfully")
		else:
			print("Invalid credentials! Please try again.")
			main()
	elif ans == 'create':
		if acc_already_exists:
			print("Account already exists!")
		else:
			create_ac(username, password)
	else:
		print("Invalid option..")
		main()

if __name__ == '__main__':
	main()
