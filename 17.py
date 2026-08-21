import re


def extract_hashtags(text: str) -> list[str]:
	"""Return all hashtags found in text, in their original order."""
	return re.findall(r"(?<!\w)#[A-Za-z0-9_]+", text)


if __name__ == "__main__":
	post = input("Enter a social media post: ")
	print(extract_hashtags(post))
