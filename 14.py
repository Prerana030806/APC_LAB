import re


def is_strong_password(password: str) -> bool:
	"""Return True when password meets all strength requirements."""
	pattern = r"^(?=.{8,}$)(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_-]).+$"
	return re.fullmatch(pattern, password) is not None


if __name__ == "__main__":
	password = input("Enter a password: ")
	print(is_strong_password(password))
