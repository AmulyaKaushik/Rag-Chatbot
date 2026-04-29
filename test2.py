import secrets
import string


def generate_random_code(length: int = 8) -> str:
	chars = string.ascii_uppercase + string.digits
	return "".join(secrets.choice(chars) for _ in range(length))


if __name__ == "__main__":
	print(generate_random_code(10))
