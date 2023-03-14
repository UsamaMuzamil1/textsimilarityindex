# create function
def percentageOfSimilarity(str1, str2):
    longerString = str1 if len(str1) > len(str2) else str2
    shorterString = str1 if len(str1) <= len(str2) else str2
    longerLength = len(longerString)
# return 1.0 basically returning True as the final value of the function while return 0 is basically returning False as the final value of the function.
    if longerLength == 0:
        return 1.0
    return (longerLength - editDistance(longerString, shorterString)) / float(longerLength)



# in this step we use two loops one for column 1 and other for column 2
# I also used append method in both loops which is used to add single string at each time
def editDistance(str1, str2):
    matrix = []
    for i in range(len(str1) + 1):
        matrix.append([i])
    for j in range(len(str2) + 1):
        matrix[0].append(j)
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i].append(matrix[i - 1][j - 1])
            else:
                matrix[i].append(min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1)
    return matrix[len(str1)][len(str2)]



# enter two strings which we used to find for similarity
per = percentageOfSimilarity("taha", "talha")
per1 = percentageOfSimilarity("taha", "tata")
per2 = percentageOfSimilarity("taha", "hata")
per3 = percentageOfSimilarity("usama", "osama")
per4 = percentageOfSimilarity("ayesha", "ashii")
per5 = percentageOfSimilarity("talal", "bilal")


# now print them and also multiply by 100(percentage)
print("Similarity percentage is :", per * 100)
print("Similarity percentage is :", per1 * 100)
print("Similarity percentage is :", per2 * 100)
print("Similarity percentage is :", per3 * 100)
print("Similarity percentage is :", per4 * 100)
print("Similarity percentage is :", per5 * 100)
