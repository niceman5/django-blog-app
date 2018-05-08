import re

def validate_phone_number(number):
    if not re.match( r'^01[016789][1-9]\d{6,7}$', number ):
        return False
    return True


print(validate_phone_number('01012341234'))
print(validate_phone_number('010123412341'))
print(validate_phone_number('0111231234'))
print(validate_phone_number('011123123'))
print(validate_phone_number('0110123123'))