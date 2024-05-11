def validate_password(password):
  """
  Checks if a password meets the following criteria:
  - Minimum length of 6 characters
  - Maximum length of 16 characters
  - Contains at least one lowercase letter (a-z)
  - Contains at least one uppercase letter (A-Z)
  - Contains at least one digit (0-9)
  - Contains at least one special character from [$#@]
  - Does not contain any whitespace characters

  Args:
      password (str): The password to be validated.

  Returns:
      bool: True if the password is valid, False otherwise.
  """
  # Check if the password meets the minimum and maximum length requirements
  if len(password) < 6 or len(password) > 16:
    return False

  # Check if the password contains at least one lowercase letter
  if not any(c.islower() for c in password):
    return False  
  
  # Check if the password contains at least one uppercase letter
  if not any(c.isupper() for c in password):
    return False 
  
  # Check if the password contains at least one digit
  if not any(c.isdigit() for c in password):
    return False
  # Check if the password contains at least one special character
  if not any(c in "$#@" for c in password):
    return False
  # Check if the password contains any whitespace characters
  if " " in password:
    return False
  return True

def main():
  """
  Prompts the user for a password and checks its validity.
  Provides informative feedback based on the validation results.
  """

  password = input("Enter a password: ")

  if validate_password(password):
    print("Your password is valid!")
  else:
    print("Your password is invalid. Please ensure it meets the following criteria:")
    print("- Minimum length of 6 characters")
    print("- Maximum length of 16 characters")
    print("- Contains at least one lowercase letter (a-z)")
    print("- Contains at least one uppercase letter (A-Z)")
    print("- Contains at least one digit (0-9)")
    print("- Contains at least one special character from [$#@]")
    print("- Does not contain any whitespace characters")

if __name__ == "__main__":
  main()