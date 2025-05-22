# Function to load country, ID, sequence records from a file into a list of lists
# Input - FileName (string) of the file contains the records
# Output - a list of records
# Errors are not checked for, file is expected to be in the correct format.
def LoadRecords(FileName):
    # The list of sequnce records to reutrn
    RecordList = []

    FIn = open(FileName, "r")

    # Read file line by line, to save memory.
    for Line in FIn:
        # Tokenize the file line on white space.
        # Record elements cannot contain white space.
        # Elemts in order are, the country code, unique ID, sequnce
        Tokens = Line.split()

        # Save the current record at the end of RecordList
        RecordList.append(Tokens)

    FIn.close()

    return RecordList


# Function to load the first sequence from a data file
# Format is is the same as for LoadRecords
# Input - FileName (string) of the file contains the records
# Output - the sequence (string)
# Errors are not checked for, one records is expected
def LoadSingleSequence(FileName):
    # Load All records, eventhough only the first is needed
    RecordData = LoadRecords(FileName)

    # only return the seqince from the first record.
    return RecordData[0][2]


# Load all records from "Human-Covid19.txt" into a list of list, called Records
Records = LoadRecords("Human-Covid19.txt")

# Load only the Bat sequnce into a string, BatSeq
BatSeq = LoadSingleSequence("Bat-Covid19.txt")


# Function to calculate the distance between two phrases
# Input - first_phrase (string), second_phrase(string)
# Output - distance between phrases(int)
# Errors are not checked for, phrases are expected to be strings

def SequenceDistance(first_phrase, second_phrase):
    same_letters = 0
    # Set the number of same letters to 0 by default

    for eachLetter in range(0, len(second_phrase)):
        # For loop indexing at each letter in both phrases

        if first_phrase[eachLetter] == second_phrase[eachLetter]:
            # If the letters are the same

            same_letters += 1
            # Increase the count of same letters

    return 1 - (same_letters / len(first_phrase))
    # Calculate the difference and return it


# Function to find the closest record in relation to a sequence
# Input - single_sequence (string), list_of_records(array)
# Output - the closest record(array)
# Errors are not checked for

def FindClosestRecord(single_sequence, list_of_records):
    smallest_distance = 2
    # Initialise the smallest distance to a value that is greater that possible

    smallest_record = list_of_records[0][2]
    # Set the smallest record to a random value

    for each_record in list_of_records:
        # For each record in the list

        if SequenceDistance(single_sequence, each_record[2]) < smallest_distance:
            # If the distance is smaller than the smallest distance we have

            smallest_distance = SequenceDistance(single_sequence, each_record[2])
            # Update value for distance

            smallest_record = each_record
            # Update value for record

    return smallest_record
    # Return record


# Function to filter the countries based on their country of origin
# Input - list_of_records(array), country_identifier(string)
# Output - all countries with the same country of origin code(array)
# Errors are not checked

def FilterByCountry(list_of_records, country_identifier):
    my_list = []
    # Initialise list

    for each_record in list_of_records:
        # For each record in the list

        if each_record[0] == country_identifier:
            # If it is from the same country

            my_list.append(each_record)
            # Add it to my list

    return my_list
    # Return list

# Function to find the person most likely to have spread the virus
# Input - list_of_records(array), origin_country(string), targer_country(string)
# Output - Void
# Errors are not checked for


def PrintTransmitter(list_of_records, origin_country, target_country):
    smallest_distance = 2
    # Initialise the smallest distance to a value that is greater that possible

    smallest_record_origin = origin_country[0]
    # Set the smallest record to a random value

    smallest_record_target = target_country[0]
    # Set the smallest record to a random value

    origin_list = FilterByCountry(list_of_records, origin_country)
    # Get the filtered list

    target_list = FilterByCountry(list_of_records, target_country)
    # Get the filtered list

    for each_value in origin_list:
        # For each value in the list

        closest_record = FindClosestRecord(each_value[2], target_list)
        # Find the closest record

        distance = SequenceDistance(closest_record[2], each_value[2])
        # Calculate the distance this record has

        if distance < smallest_distance:
            # If its smaller than our smallest value

            smallest_distance = distance
            # Update the smallest value

            smallest_record_origin = each_value
            # Update value for record

            smallest_record_target = closest_record
            # Update value for record

    print("Unique ID Origin({}): {}, Unique ID Target({}): {}, Distance: {}".format(smallest_record_target[0], smallest_record_target[1], smallest_record_origin[0], smallest_record_origin[1], smallest_distance))
    # Output the Records and their distance


myRecord = FindClosestRecord(BatSeq, Records)
value = SequenceDistance(myRecord[2], BatSeq)
print("County: {}, Unique ID: {}, Distance: {}".format(myRecord[0], myRecord[1], value))

PrintTransmitter(Records, "AGO", "IOT")

