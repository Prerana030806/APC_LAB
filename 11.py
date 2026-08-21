import re


def is_valid_email(email: str) -> bool:
	"""Return True when email matches the required format."""
	pattern = r"^[A-Za-z0-9._-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z0-9]{2,6}$"
	return re.fullmatch(pattern, email) is not None


if __name__ == "__main__":
	email = input("Enter an email address: ")
	print(is_valid_email(email))
