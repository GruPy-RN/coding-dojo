def manipulate(s):
	plus = s.find("+")
	at = s.find("@")
	if plus == -1:
		return s[0:at].replace('.', '') + s[at:]
	return s[0:plus].replace('.', '') + s[at:]

def count_users(input_file="input.txt"):
    with open(input_file) as f:
        lines = f.readlines()
    number_of_lines = int(lines[0])
    users = set(manipulate(email) for email in lines[1:])
    return len(users)
