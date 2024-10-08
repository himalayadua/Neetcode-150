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

    
