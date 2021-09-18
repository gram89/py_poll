# print ("Hello World")
# getting datatypes
# input data
# my_votes = int(input("How many votes did you get in the election?"))
# total_votes = int(input("What are the total votes in the election?"))
# percentage_votes = (my_votes/total_votes)*100
# print (f"I recieved {percentage_votes}% of the total votes")

# adding counties list
# counties = ["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == "Denver":
#     print(counties[1])
# if counties[3] !="Jefferson":
#     print(counties[2])

# temperature = int(input("What is the temperature outside?"))
# if temperature >80:
#     print("Turn on the AC")
# else:
#     print("Open the windows")
# if "Arapahoe" in counties:
#     print("True")
# else:
#     print("False")
# x = 0
# while x<=5:
#     print(x)
#     x=x+1

# counties = ["Arapahoe", "Denver", "Jefferson"]
# for county in counties:
#     print(county)

# counties_dict={}
# counties_dict["Arapahoe"]=422829
# counties_dict["Denver"] = 463353
# counties_dict["Jefferson"] = 432438
# #print(counties_dict)
# print(len(counties_dict))
# print(counties_dict.items())

# voting_data = []
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Jefferson", "registered_voters": 432438})

#How many votes did you get?
# cand_votes = int(input("How many votes did you get?"))
# total_votes = int(input("What is the total vote count?"))
# per_votes = (cand_votes/total_votes)*100
# print(f"I got {cand_votes} which is {per_votes}% of the total vote count of {total_votes}")

# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")

# for county in counties:
#     print(county)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict.keys():
#     print(county)
# for voters in counties_dict.values():
#     print(voters)
# for county, voters in counties_dict.items():
#     print(county, voters)
# for county, voters in counties_dict.items():
#     print(f"{county} has a total of {voters} registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)
# for i in range(len(voting_data)):
#     print(voting_data[i])

for county_dict in voting_data:
    print (f"{county_dict['county']} county has {county_dict['registered_voters']} number of registered voters")
