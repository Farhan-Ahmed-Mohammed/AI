def medical_diagnosis():
    print("Wellcome to medical diagnosis")
    print("Asnswer the following questions as 'yes' or 'no' :")
    fever=input("Do you have fever :").lower()
    cough=input("Do you have cough :").lower()
    headach=input("Do you have headach :").lower()
    sore_throath=input("Do you have sore_throath :").lower()
    shortness_of_breath=input("Do you have shortness of breadth :").lower()
    
    if fever=='yes' and cough=='yes' and shortness_of_breath=='yes':
        print("You have covid-19 ,please consualt a doctor")
        
    elif fever=='yes' and cough=='yes' and headach=='yes':
        print("You have common cold ")
        
    elif fever=='no' and cough=='no' and headach=='yes':
        print("You have stress, take rest")
        
    else:
        print("You symtons are unclear meet a doctor")
        
medical_diagnosis()   
