instructor_pod = {}

jacore_leader = {}
andrew_leader = {}
richard_leader = {}
aris_leader = {}
gabriel_leader = {}

jacore_members = {}
andrew_members = {}
richard_members = {}
aris_members = {}
gabriel_members = {}

#4 Create an empty dictionary for the other 3 PODs; Aris, Gabriel and Richard

#5 Add the names and telephone numbers of each member POD
jacore_members['Moussa Ndiaye'] = '(123) 456-7890'
jacore_members['Morris Jones'] = '(925) 286-5922'
jacore_members['Prince Fields'] = '(510) 472-0804'
jacore_members['Akari Johnson'] = '(510) 500-2206'

andrew_members['Mallick Abdullah'] = '(510) 409-8755' 
andrew_members['Ronin Youngjones'] = '(415) 910-3415'
andrew_members['Glenn Ivory'] = '(510) 328-8290'

richard_members['Prince Fields'] = '(510) 472-0804'
richard_members['Mattew Dudley'] = '(510) 816-2411'
richard_members['Kymari Rhodes'] = '(510) 575-1982'
richard_members['Josiah Johnson'] = '(510) 860-5112'

aris_members['Milan Kral'] = '(510) 816-3232'
aris_members['Maurice Richardson'] = '(510) 424-7789'
aris_members['Zyion Williams'] = '(510) 480-5785'
aris_members['Hyab Isayas'] = '(510) 612-3737'

gabriel_members['David Brickley'] = '(510) 631-6288'
gabriel_members['Myles Wilkerson'] = '(510) 500-7266'
gabriel_members['Emmanuel Torbor'] = '(510) 934-4133'

jacore_leader['Jacore'] = jacore_members
andrew_leader['Andrew'] = andrew_members
aris_leader['Aris'] = aris_members
richard_leader['Richard'] = richard_members
gabriel_leader['Gabriel'] = gabriel_members

         
#6 Add all the PODS to the all_pod_members dictionary
instructor_pod['Baba'] = jacore_leader
instructor_pod['Hodari'] = andrew_leader
instructor_pod['David'] = richard_leader
instructor_pod['Paris'] = aris_leader
instructor_pod['Akeem'] = gabriel_leader

#9 Print all the Pod leaders and POD membership



for instructor_pod, pod_leader in instructor_pod.items():
    print("This is the pod's instructor: ", instructor_pod)
    
    for pod_leader, pod_member in pod_leader.items():
        print("This is the pod's leader: ", pod_leader);
        for pod_member, phone_number in pod_member.items():
            print(pod_member,phone_number)
    print("\n")

