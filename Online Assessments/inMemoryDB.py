#SET <key> <field> <value> 
#GET <key> <field>
#DELETE <key> <field> 


class inMemoryDB:
    def __init__(self) -> None:
        self.database = {}
    

    def set(self, key: str, field: str, value: str) -> None:
        if key not in self.database:
            self.database[key] = {field, value}
        else:
            self.database[key][field] = value




    def get(self, key: str, field: str) -> str:
        if key not in self.database:
            return ""
        else:
            return self.database[key][field]

        
    def delete(self, key: str, field: str) -> bool:
        if key in self.database:
            del self.database[key][field]
            return True
        else:
            return False


# Level2
# SCAN <key>
# SCAN_BY_PREFIX <key> <prefix>

    def scan(self, key: str) -> list[str]:
        if key not in self.database:
            return []
        else:
            strn = [f"{field}({value})" for field, value in sorted(self.database[key].items())]
            # list comprehension
            # <expression> for-loop <variable-n> in [list]{dict} if <condition>
            return strn


    def scan_by_prefix(self, key: str, prefix: str) -> list[str]:
        if key not in self.database:
            return []
        else:
            strn = [f"{field}({value})" for field, value in sorted(self.database[key].items()) if field.startswith(prefix)]
            # list comprehension
            
            return strn

# Level 3
# SET_AT <key> <field> <value> <timestamp> — should insert a field-value pair or updates the value of the field in the record associated with key. This operation should return an empty string.
# SET_AT_WITH_TTL <key> <field> <value> <timestamp> <ttl> — should insert a field-value pair or update the value of the field in the record associated with key. Also sets its Time-To-Live starting at timestamp to be ttl. The ttl is the amount of time that this field-value pair should exist in the database, meaning it will be available during this interval: [timestamp, timestamp + ttl). This operation should return an empty string.
# DELETE_AT <key> <field> <timestamp> — the same as DELETE, but with timestamp of the operation specified. Should return "true" if the field existed and was successfully deleted and "false" if the key didn't exist.
# GET_AT <key> <field> <timestamp> — the same as GET, but with timestamp of the operation specified.
# SCAN_AT <key> <timestamp> — the same as SCAN, but with timestamp of the operation specified.
# SCAN_BY_PREFIX_AT <key> <prefix> <timestamp> — the same as SCAN_BY_PREFIX, but with timestamp of the operation specified.

