

```python
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

User input
user_email = input("Enter your email address: ")

if is_valid_email(user_email):
    print("✅ Valid email address.")
else:
    print("❌ Invalid email format.")
```

---

🔍 Explanation:
- `\w` → letter, number or underscore
- `+` → one or more characters
- `@` → must include @
- `.` → must end with something like `.com`, `.org`, etc.

---

🧪 Sample Output:

*Input:* `test@gmail.com`  
*Output:* ✅ Valid email address.

*Input:* `test@com`  
*Output:* ❌ Invalid email format.

---

📌 *Optional:* You can also check if the email actually exists (by sending a confirmation mail), but that requires more advanced tools.

Would you like to check *phone numbers or passwords* too?

