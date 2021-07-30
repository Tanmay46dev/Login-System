def log_in():
	user_name = input("Type in your username: ")
	password = input("Type in your password: ")
	with open('accounts.txt') as f:
		for line in f.readlines():
			line = line.replace(' ', '')
			line = line.replace('\n', '')
			if line.split('-')[0] == user_name:
				if line.split('-')[1] == password:
					print('Logged in successfuly!!')
				else:
					print(f"incorrect password for: {user_name}")
			else:
				print(f'No account named: {user_name}')


def create_ac():
	user_name = input("Choose your username: ")
	password = input("Type in a strong password: ")
	with open('accounts.txt', 'a') as f:
		f.write(f"{user_name} - {password}\n")
	print("Account created successfuly!!")


def main():
	ans = input("Would you want to log in or create an account? (login/create): ")

	if ans == 'login':
		log_in()
	elif ans == 'create':
		create_ac()
	else:
		print("Invalid option..")

if __name__ == '__main__':
	main()