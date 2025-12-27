#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open("C:/Users/windows/Documents/Dude/Coffee_machine/Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as f:

    Template = f.read()

with open("C:/Users/windows/Documents/Dude/Coffee_machine/Mail Merge Project Start/Input/Names/invited_names.txt", "r") as s:
    names_list = s.readlines()

for i in names_list:
    correccted_name = i.strip()
    final_corrected_list = Template.replace("[name]", correccted_name) 

    with open(f"C:/Users/windows/Documents/Dude/Coffee_machine/Mail Merge Project Start/Output/ReadyToSend/letter_for_{correccted_name}.txt","w") as g:
        g.write(final_corrected_list)

 