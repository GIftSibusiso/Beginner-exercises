'''
    This is the team allocator project solution example project
'''


def student_list():
    return ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'ddhaalJHB2022 - 2 May - Cape Town Virtual',
    'thandohDBN2022 - 4 April - Phokeng Physical - seat 3', 'zaneleJHB2022 - 2 May - Durban Virtual',
    'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2', 'BusiJHB2022 - 2 May - Durban Virtual',
    'zinhlehDBN2022 - 4 April - Phokeng Physical - seat 1', 'CebiJHB2022 - 2 May - Durban Virtual',
    'lukhona - 4 April - Phokeng Virtual', 'ddhaalJHB2022 - 2 May - Durban Physical - seat 4',
    'gabiDBN2022 - 4 April - Phokeng Virtual', 'ngakithilJHB2022 - 2 May - Durban Physical - seat 5',
    'zimthembilehDBN2022 - 4 April - Phokeng Virtual', 'ngakuyelJHB2022 - 2 May - Durban Physical - seat 2',
    'zimlindilehDBN2022 - 4 April - Phokeng Virtual', 'yenzileJHB2022 - 2 May - Durban Physical - seat 3',
    'zimthandilehDBN2022 - 4 April - Johannesburg Virtual','kuhlengaweDBN2022 - 4 April - Durban Physical - seat 1',
    'zimkhonzileDBN2022 - 4 April - Johannesburg Virtual','hlelokuhlehDBN2022 - 4 April - Durban Physical - seat 3',
    'zizonkehDBN2022 - 4 April - Johannesburg Virtual','sibusisohDBN2022 - 4 April - Durban Physical - seat 2',
    'kholekileDBN2022 - 4 April - Johannesburg Virtual','vusiDBN2022 - 4 April - Durban Physical - seat 9',
    'kholelwahDBN2022 - 4 April - Johannesburg Virtual','zuzumuzihDBN2022 - 4 April - Durban Physical - seat 10',
    'thembelahDBN2022 - 4 April - Johannesburg Virtual','babazileDBN2022 - 4 April - Durban Physical - seat 11',
    'thembisileDBN2022 - 4 April - Johannesburg Virtual','owenkosiDBN2022 - 4 April - Durban Physical - seat 8',
    'thembisiweDBN2022 - 4 April - Johannesburg Physical - seat 5', 'nobuhleJHB2022 - 2 May - Cape Town physical',
    'thenjisiweDBN2022 - 4 April - Johannesburg Physical - seat 6', 'nonkonzoJHB2022 - 2 May - Cape Town Physical',
    'thethelelileDBN2022 - 4 April - Johannesburg Physical - seat 7', 'nombusoJHB2022 - 2 May - Cape Town Virtual',
    'thembiDBN2022 - 4 April - Johannesburg Physical - seat 4', 'nozizweJHB2022 - 2 May - Cape Town Virtual']

def space_maker(string):
    output = ""
    for i in string:
        if i != " ":
            output += i
    return output


def dbn_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Durban campus only.
    '''
    dbn_students = []

    for student in student_list:
        campus = student.split("-")[2]
        if "Durban" in campus:
            dbn_students.append(space_maker(student).lower())

    return dbn_students


def cpt_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Cape Town campus only.
    '''
    cpt_students = []

    for student in student_list:
        campus = student.split("-")[2]
        if "Cape Town" in campus:
            cpt_students.append(space_maker(student).lower())
    return cpt_students


def jhb_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Johannesburg campus only.
    '''
    jhb_students = []

    for student in student_list:
        campus = student.split("-")[2]
        if "Johannesburg" in campus:
            jhb_students.append(space_maker(student).lower())

    return jhb_students


def nw_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the North West campus only.
    '''
    nw_students = []

    for student in student_list:
        campus = student.split("-")[2]
        if "Phokeng" in campus:
            nw_students.append(space_maker(student).lower())

    return nw_students


def dbn_physical_students(dbn_students):
    '''
    from the list of dbn_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    dbn_physical_students = []

    for student in dbn_students:
        attendance = student.split("-")[2].lower()
        if "physical" in attendance and "durban" in attendance:
            dbn_physical_students.append(space_maker(student).lower())

    return dbn_physical_students


def dbn_physical_teams(dbn_physical_students):
    '''
    from the list of dbn_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    dbn_physical_teams = []
    team = []

    for students in dbn_physical_students:
        if len(team) == 4:
            dbn_physical_teams.append(team)
            team = []
        team.append(space_maker(students).lower())
        
    if len(team) > 0:
        dbn_physical_teams.append(team)

    return dbn_physical_teams



def dbn_teams_file(durban_physical_teams):
    '''
    write and save the information in the dbn_physical_teams into a textfile
    '''
    with open("campus_teams.txt", "w") as file:
        file.write("Durban physical team 2022\n")
    team_number = 1
    for team in durban_physical_teams:
        with open("campus_teams.txt", "a") as file:
            file.write(f"dbn team{team_number}\t")
        team_number += 1
        for student in team:
             with open("campus_teams.txt", "a") as file:
                file.write(f"{student}\n\t\t\t")
        with open("campus_teams.txt", "a") as file:
            file.write("\n")


def cpt_physical_students(cpt_students):
    '''
    from the list of cpt_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    cpt_physical_students = []

    for student in cpt_students:
        attendance = student.split("-")[2].lower()
        if "physical" in attendance and "capetown" in space_maker(attendance):
            cpt_physical_students.append(space_maker(student).lower())
    
    return cpt_physical_students


def cpt_physical_teams(cpt_physical_students):
    '''
    from the list of cpt_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    cpt_physical_teams = []
    team = []

    for students in cpt_physical_students:
        if len(team) == 4:
            cpt_physical_teams.append(team)
            team = []
        team.append(space_maker(students).lower())
        
    if len(team) > 0:
        cpt_physical_teams.append(team)

    return cpt_physical_teams


def cpt_teams_file(capetown_final_teams):
    '''
    write and save the information in the cpt_physical_teams into a textfile
    '''
    with open("campus_teams.txt", "a") as file:
        file.write("Cape Town physical team 2022\n")
    team_number = 1
    for team in capetown_final_teams:
        with open("campus_teams.txt", "a") as file:
            file.write(f"cpt team{team_number}\t")
        team_number += 1
        for student in team:
             with open("campus_teams.txt", "a") as file:
                file.write(f"{student}\n\t\t\t")
        with open("campus_teams.txt", "a") as file:
            file.write("\n")


def jhb_physical_students(jhb_students):
    '''
    from the list of jhb_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    jhb_physical_students = []

    for student in jhb_students:
        attendance = student.split("-")[2].lower()
        if "physical" in attendance and "johannesburg" in attendance:
            jhb_physical_students.append(space_maker(student).lower())
    
    return jhb_physical_students


def jhb_physical_teams(jhb_physical_students):
    '''
    from the list of jhb_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    jhb_physical_teams = []
    team = []

    for students in jhb_physical_students:
        if len(team) == 4:
            jhb_physical_teams.append(team)
            team = []
        team.append(space_maker(students).lower())
        
    if len(team) > 0:
        jhb_physical_teams.append(team)

    return jhb_physical_teams


def jhb_teams_file(jhb_final_teams):
    '''
    write and save the information in the jhb_physical_teams into a textfile
    '''
    with open("campus_teams.txt", "a") as file:
        file.write("Johannesburg physical team 2022\n")
    team_number = 1
    for team in jhb_final_teams:
        with open("campus_teams.txt", "a") as file:
            file.write(f"jhb team{team_number}\t")
        team_number += 1
        for student in team:
             with open("campus_teams.txt", "a") as file:
                file.write(f"{student}\n\t\t\t")
        with open("campus_teams.txt", "a") as file:
            file.write("\n")


def nw_physical_students(nw_students):
    '''
    from the list of nw_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    nw_physical_students = []

    for student in nw_students:
        attendance = student.split("-")[2].lower()
        if "physical" in attendance and "phokeng" in attendance:
            nw_physical_students.append(space_maker(student).lower())
    
    return nw_physical_students


def nw_physical_teams(nw_physical_students):
    '''
    from the list of nw_physical_students, create list of 4 students per team, and add them to 
    one big list
    '''
    nw_physical_teams = []
    team = []

    for students in nw_physical_students:
        if len(team) == 4:
            nw_physical_teams.append(team)
            team = []
        team.append(space_maker(students).lower())
        
    if len(team) > 0:
        nw_physical_teams.append(team)

    return nw_physical_teams


def nw_teams_file(nw_final_teams):
    '''
    write and save the information in the nw_physical_teams into a textfile
    '''
    with open("campus_teams.txt", "a") as file:
        file.write("North West physical team 2022\n")
    team_number = 1
    for team in nw_final_teams:
        with open("campus_teams.txt", "a") as file:
            file.write(f"nw team{team_number}\t")
        team_number += 1
        for student in team:
             with open("campus_teams.txt", "a") as file:
                file.write(f"{student}\n\t\t\t")
        with open("campus_teams.txt", "a") as file:
            file.write("\n")


def get_virtual_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students attending virtually.
    '''
    virtual_campus = []

    for student in student_list:
        attendance = student.split("-")[2].lower()
        if "virtual" in attendance:
            virtual_campus.append(student)

    return virtual_campus
virtual_students = get_virtual_students(student_list())

def virtual_teams(virtual_students_list):
    '''
    from the list of virtual_students above,  create list of 4 students per team, and add them to 
        one big list
    '''
    virtual_teams = []
    team = []

    for students in virtual_students_list:
        if len(team) == 4:
            virtual_teams.append(team)
            team = []
        team.append(space_maker(students).lower())
        
    if len(team) > 0:
        virtual_teams.append(team)

    return virtual_teams
vt = virtual_teams(virtual_students)

def virtual_teams_file(virtual_teams):
    '''
    write and save the information in the virtual_teams into a textfile
    '''
    with open("virtual_teams.txt", "w") as file:
        file.write("Virtual teams 2022\n")
    team_number = 1
    for team in virtual_teams:
        with open("virtual_teams.txt", "a") as file:
            file.write(f"virtual team{team_number}\t")
        team_number += 1
        for student in team:
             with open("virtual_teams.txt", "a") as file:
                file.write(f"{student}\n\t\t\t\t")
        with open("virtual_teams.txt", "a") as file:
            file.write("\n")
virtual_teams_file(vt)

if __name__ == '__main__':
    '''
    call all your functions below to make your program execute    
    '''
    dbn = dbn_campus_students(student_list())
    dbn_phy = dbn_physical_students(dbn)
    cpt = cpt_campus_students(student_list())
    jhb = jhb_campus_students(student_list())
    nw = nw_campus_students(student_list())
    dbn_teams = dbn_physical_teams(dbn_phy)
    dbn_teams_file(dbn_teams)
    cpt_phy = cpt_physical_students(cpt)
    cpt_team = cpt_physical_teams(cpt_phy)
    cpt_teams_file(cpt_team)
    jhb_phy = jhb_physical_students(jhb)
    jhb_teams = jhb_physical_teams(jhb_phy)
    jhb_teams_file(jhb_teams)
    nw_phy = nw_physical_students(nw)
    nw_teams = nw_physical_teams(nw_phy)
    nw_teams_file(nw_teams)

