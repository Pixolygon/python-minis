import re


def censor(s):
    censor_re = re.compile(r'\bfrack\w*\b', re.I)
    censored = censor_re.sub('CENSORED', s)
    return censored


print(censor("Frack you"))
print(censor("I hope you fracking die"))
print(censor("you fracking Frack"))


# def parse_date(d):
#     date_re = re.compile(
#         r'^(?P<day>\d\d)[\/\,\.](?P<month>\d\d)[\/\,\.](?P<year>\d{4})$')
#     match = date_re.search(d)
#     return {
#         'd': match.group('day'),
#         'm': match.group('month'),
#         'y': match.group('year')
#     } if match else None


# # print(parse_date("12,04,2003"))
# # print(parse_date("12.11.2003"))
# # print(parse_date("12.11.200312"))
# # print(parse_date("01/22/1999"))


# def parse_bytes(s):
#     byte_re = re.compile(r'\b[10]{8}\b')
#     match = byte_re.findall(s)
#     return match


# # print(parse_bytes("11010101 101 323"))
# # print(parse_bytes("my data is: 10101010 11100010"))
# # print(parse_bytes("asda"))

# def is_valid_time(t):
#     time_re = re.compile(r'^(\d{1}|\d{2}):\d{2}$')
#     match = time_re.search(t)
#     return True if match else False


# # print(is_valid_time("it is 10:45"))
# # print(is_valid_time("1:23"))
# # print(is_valid_time("10.45"))
# # print(is_valid_time("1999"))
# # print(is_valid_time("145:23"))
