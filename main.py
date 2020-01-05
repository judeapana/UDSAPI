from pprint import pprint
from pandas import DataFrame
from udsapi.Authentication.auth import Auth
from udsapi.APIResultsSet.resultSet import CourseResultSet, TableFinalResultSet

print(" NB: THIS BOT ISNT A COMMAND LINE APP []")
print(" :-) YOU CAN SUPPORT US BUILD THIS BOT ")
print("Please Make Sure You Are Connected To The Internet")
print("=====================")
print("")
username = input("Enter Your Student ID: ")
password = input("Enter Your Password :")

if username and password:
    user = Auth(username, password)
    user.login()
    res = CourseResultSet(user.sessionManager)
    print("fetching results ....")
    print(" ----- Course Registration -----")
    df = DataFrame(res.parser_data())
    print(df)
    print(" ----- Course Registration -----")
    print("")
    print("fetching results ....")
    res = TableFinalResultSet(user.sessionManager)
    for i, j in enumerate(res.resultsNames):
        print(i + 1, " ", j)
    index = int(input("ENTER THE INDEX FOR THE FINAL RESULT YOUR WANT TO VIEW : "))
    print("fetching results ....")
    df = [DataFrame(res.dumpResults(index)[i]) for i in res.dumpResults(index).keys()]
    print(df)
    print(" ----- RESULT -----")
