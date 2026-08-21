import re

IPV4_PATTERN = re.compile(
	r"^(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}"
	r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"
)

IPV6_PATTERN = re.compile(
	r"^(?:"
	r"(?:[0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}|"
	r"(?:[0-9A-Fa-f]{1,4}:){1,7}:|"
	r"(?:[0-9A-Fa-f]{1,4}:){1,6}:[0-9A-Fa-f]{1,4}|"
	r"(?:[0-9A-Fa-f]{1,4}:){1,5}(?::[0-9A-Fa-f]{1,4}){1,2}|"
	r"(?:[0-9A-Fa-f]{1,4}:){1,4}(?::[0-9A-Fa-f]{1,4}){1,3}|"
	r"(?:[0-9A-Fa-f]{1,4}:){1,3}(?::[0-9A-Fa-f]{1,4}){1,4}|"
	r"(?:[0-9A-Fa-f]{1,4}:){1,2}(?::[0-9A-Fa-f]{1,4}){1,5}|"
	r"[0-9A-Fa-f]{1,4}:(?:(?::[0-9A-Fa-f]{1,4}){1,6})|"
	r":(?:(?::[0-9A-Fa-f]{1,4}){1,7}|:)"
	r")$"
)


def is_valid_ip(address):
	"""Return True when address is a valid IPv4 or IPv6 address."""
	return bool(IPV4_PATTERN.fullmatch(address) or IPV6_PATTERN.fullmatch(address))

if __name__ == "__main__":
	addresses = [
		"192.168.1.1",
		"2001:0db8:85a3:0000:0000:8a2e:0370:7334",
		"2001:db8::1",
		"256.1.1.1",
		"2001:db8:::1",
	]

	for address in addresses:
		print(f"{address}: {is_valid_ip(address)}")
