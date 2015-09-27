# coding: utf-8

"""
Input file format: 300005366935;330.70;323.70;483.30;486.90;460.00;A;B;D
"""

DATA_INPUT = 'transformed.csv'
COEFFICIENT = 3670089

fp = open(DATA_INPUT)

SUM_CN = 0
SUM_CH = 0
SUM_LC = 0
SUM_MT = 0
SUM_RE = 0

SUM_PUBLIC_SCHOOL = 0
SUM_PRIVATE_SCHOOL = 0
COUNT_PUBLIC_SCHOOL = 0
COUNT_PRIVATE_SCHOOL = 0

SUM_PARENT_NOT_STUDY = 0
COUNT_PARENT_NOT_STUDY = 0

SUM_PARENT_HIGH_SCHOOL = 0
COUNT_PARENT_HIGH_SCHOOL = 0

SUM_PARENT_HIGHER_SCHOOL = 0
COUNT_PARENT_HIGHER_SCHOOL = 0

for line in fp:
    split_line = line.split(';')
    SUM_CN = float(split_line[1])
    SUM_CH = float(split_line[2])
    SUM_LC = float(split_line[3])
    SUM_MT = float(split_line[4])
    SUM_RE = float(split_line[5])

    # # ask for public school
    # if split_line[6] == 'A':
    #     COUNT_PUBLIC_SCHOOL += 1
    #     SUM_PUBLIC_SCHOOL += (SUM_CN + SUM_CH + SUM_LC + SUM_MT + SUM_RE)

    # # ask for private school
    # if split_line[6] == 'C':
    #     COUNT_PRIVATE_SCHOOL += 1
    #     SUM_PRIVATE_SCHOOL += (SUM_CN + SUM_CH + SUM_LC + SUM_MT + SUM_RE)

    # ask for parent that dont study
    if split_line[7] == 'A' and split_line[8].strip('\n') == 'A':
        COUNT_PARENT_NOT_STUDY += 1
        SUM_PARENT_NOT_STUDY += (SUM_CN + SUM_CH + SUM_LC + SUM_MT + SUM_RE)

    # ask for parent that study in high school
    if split_line[7] == 'E' and split_line[8].strip('\n') == 'E':
        COUNT_PARENT_HIGH_SCHOOL += 1
        SUM_PARENT_HIGH_SCHOOL += (SUM_CN + SUM_CH + SUM_LC + SUM_MT + SUM_RE)

    # ask for parent that study in high school
    if split_line[7] == 'G' and split_line[8].strip('\n') == 'G':
        COUNT_PARENT_HIGHER_SCHOOL += 1
        SUM_PARENT_HIGHER_SCHOOL += (SUM_CN + SUM_CH + SUM_LC + SUM_MT + SUM_RE)


# print "Somatória das áreas do conhecimento: CN: %d, CH: %d, LC: %d, MT: %d, RE: %d" % (SUM_CN, SUM_CH, SUM_LC, SUM_MT, SUM_RE)

# print "Média das áreas do conhecimento: CN: %d, CH: %d, LC: %d, MT: %d, RE: %d" % (int(SUM_CN)/COEFFICIENT, int(SUM_CH)/COEFFICIENT, int(SUM_LC)/COEFFICIENT, int(SUM_MT)/COEFFICIENT, int(SUM_RE)/COEFFICIENT)


# print '-'*80

# print SUM_PUBLIC_SCHOOL
# print COUNT_PUBLIC_SCHOOL

# print SUM_PUBLIC_SCHOOL/COUNT_PUBLIC_SCHOOL

# print SUM_PUBLIC_SCHOOL/5
# print (SUM_PUBLIC_SCHOOL/5)/COUNT_PUBLIC_SCHOOL

# print '-'*80

# print SUM_PRIVATE_SCHOOL
# print COUNT_PRIVATE_SCHOOL

# print SUM_PRIVATE_SCHOOL/COUNT_PRIVATE_SCHOOL

# print SUM_PRIVATE_SCHOOL/5
# print (SUM_PRIVATE_SCHOOL/5)/COUNT_PRIVATE_SCHOOL


print '-'*80

print SUM_PARENT_NOT_STUDY
print COUNT_PARENT_NOT_STUDY

print SUM_PARENT_NOT_STUDY/COUNT_PARENT_NOT_STUDY

print (SUM_PARENT_NOT_STUDY/5)/COUNT_PARENT_NOT_STUDY


print '-'*80

print SUM_PARENT_HIGH_SCHOOL
print COUNT_PARENT_HIGH_SCHOOL

print SUM_PARENT_HIGH_SCHOOL/COUNT_PARENT_HIGH_SCHOOL

print (SUM_PARENT_HIGH_SCHOOL/5)/COUNT_PARENT_HIGH_SCHOOL


print '-'*80

print SUM_PARENT_HIGHER_SCHOOL
print COUNT_PARENT_HIGHER_SCHOOL

print SUM_PARENT_HIGHER_SCHOOL/COUNT_PARENT_HIGHER_SCHOOL

print (SUM_PARENT_HIGHER_SCHOOL/5)/COUNT_PARENT_HIGHER_SCHOOL
