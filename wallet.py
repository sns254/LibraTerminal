#Libra Wallet in Python
from pylibra import LibraClient, LibraWallet
from pylibra.transaction import TransferTransaction
from termcolor import cprint
from time import sleep
import pyqrcode, sys

client = LibraClient()
address_dict = {}

def current_accounts(wlt):
	print("\n")
	for i in range(0,6):
		acct = wlt.get_account(i)
		cprint(f"Account {i}: {acct.address}", "blue")
		if client.get_account_state(acct) == None or round(client.get_account_state(acct).balance/1000000) == 0:
			cprint(f"Balance: 0 tLibra", "red")
		else:
			cprint(f"Balance: {round(client.get_account_state(acct).balance/1000000)} tLibra", "green")

		address_dict[f"{i}"] = acct.address
	print("\n")

def qr_create(loc):
	qr = pyqrcode.create(loc)
	print(qr.text().replace("0","⬜").replace("1","⬛"))

def send_tx(addr, amt, acct):
	if addr == str(wallet.get_account(int(acct)).address):
		cprint("\nReceiver is the same as the sender\n", "yellow")
		sleep(3)
		return False
	try:
		tx_account = wallet.get_account(int(acct))
		balance_before = client.get_account_state(tx_account).balance
		tx = TransferTransaction(addr, amt*1000000)
		fromacct = wallet.get_account(int(acct))
		client.send_transaction(wallet.get_account(int(acct)), tx)
		balance_after = client.get_account_state(tx_account).balance
		if balance_after == balance_before:
			cprint("\nTx failed. Check that you have sufficient funds", "red")
		else:
			cprint(f"\nSuccess! {str(amt)} tLibra sent to {addr}", "green")
			sleep(3)
	except:
		cprint("\nInsufficient funds", "red")

while True:
	#Create the control panel
	cprint("---"*11, "yellow")
	cprint("\nWelcome! Please select an option:\n", "yellow")
	cprint("---"*11, "yellow")
	cprint("\n[CREATE] a new wallet\n[IMPORT] an existing mnemonic\n","blue")

	user_input = input("")

	if user_input.lower() == "create" or user_input.lower() == "import":
		if user_input.lower() == "create":

			cprint("Are you sure? This will overwrite any previously saved mnemonic phrase.[y/n]", "red")
			ui2 = input("\n")

			if ui2.lower() == "y":
				wallet = LibraWallet()
				cprint("\nYOUR MNEMONIC SEED IS:\n", "blue")
				cprint(wallet.to_mnemonic(), "green")
				cprint("\nThis will be saved to 'seed.txt'. For extra security, write it down somewhere.\n\n", "blue")

				with open("seed.txt", "w") as file:
					file.write(wallet.to_mnemonic())
					mnemonic = wallet.to_mnemonic()
					break

		if user_input.lower() == "import":

			try:
				with open("seed.txt", "r") as file:
					mnemonic = file.read()
					wallet = LibraWallet(mnemonic)
					break
			except:
				cprint("No file found. Create a wallet first.\n", "yellow")
				sleep(3)
	else:
		cprint("\nCouldn't understand input.", "yellow")
		sleep(3)

while True:
	cprint("--"*13, "yellow")
	cprint("\nWhat would you like to do?\n", "yellow")
	cprint("--"*13, "yellow")
	cprint("\n[RECV] tLibra\n[SEND] tLibra\n[MINT] tLibra\n[LIST] Balance\n[QUIT] to quit\n", "blue")
	user_input = input("")

	if user_input.lower() == "list":
		current_accounts(wallet)
	if user_input.lower() == "recv" or user_input.lower() == "send":
		if user_input.lower() == "recv":
			cprint("\nWhich account do you want to receive to?\n", "blue")
			ui2 = input()
			try:
				cprint(address_dict[ui2], "green")
				cprint("\nShow QR?[y/n]\n")
				ui3 = input()
				if ui3.lower() == "y":
					qr_create(address_dict[ui2])

				cprint("Press Enter to continue","cyan")
				filler = input()
			except:
				cprint("\nRun the 'LIST' command to see available accounts.", "yellow")
		
		if user_input.lower() == "send":
			cprint("\nWhich account do you want to send from?[0-5]", "blue")
			ui2 = input()
			cprint("\nWhich address do you want to send to?", "blue")
			ui3 = input()
			cprint("\nHow much do you want to send?", "blue")
			ui4 = input()
			try:
				send_tx(ui3, int(ui4), ui2)
			except:
				cprint("\nCould not make sense of input", "red")
				sleep(3)

	if user_input.lower() == "mint":
		cprint("\nHow much do you want to mint?", "blue")
		ui2 = input()
		cprint("\nWhich account do you want to send funds to?[0-5]", "blue")
		ui3 = input()

		acct_address = wallet.get_account(int(ui3))

		try:
			client.mint_with_faucet(acct_address, int(ui2)*1000000)
			cprint(f"\n{ui2} tLibra sent to account {ui3}!", "green")

		except:
			cprint("\nCould not mint that amount", "yellow")
			sleep(3)

	if user_input.lower() == "quit" or user_input.lower() == "q":
		sys.exit()
 









