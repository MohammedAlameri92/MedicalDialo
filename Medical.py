
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog



class DiseaseDiagnosisApp:
    def __init__(self, master):
        self.master = master
        master.title("Disease Diagnosis Tool")
        
        self.label = tk.Label(master, text="What is the patient’s name?",fg='black',bg='yellow',font=('Times New Roman',14))
        self.label.pack()
        self.label.place(x=45,y=200)

        self.patient_name_entry = tk.Entry(master,font=('Times New Roman',14))
        self.patient_name_entry.pack()
        self.patient_name_entry.place(x=60,y=235)

#-------------------------------------Button Diagnosis------------------------------

        self.start_button = tk.Button(master, text="Start Diagnosis",fg='black',bg='red',font=('Times New Roman',12), command=self.start_diagnosis)
        self.start_button.pack()
        self.start_button.place(x=100,y=280)
#------------------------------Resulting-------------------------------------

        self.result_label = tk.Label(master, text="",fg='black',font=('Times New Roman',14))
        self.result_label.pack()
        self.result_label.place(x=30,y=320)


        self.photo=tk.PhotoImage(file="C:/Users/Qursan/Desktop/MohammedNoman_202070363_AI/Q.png")
        self.imo=tk.Label(master,image=self.photo)
        self.imo.place(x=10,y=10,width=288,height=190)


#------------------------------Name Developer----------------------------------------
        self.Develop = tk.Label(master, text="Developer By : Mohammed Noman",fg='black',font=('Times New Roman',12))
        self.Develop.pack()
        self.Develop.place(x=30,y=380)

#------------------------------Dr.Supervised----------------------------------------       
        self.Supervised = tk.Label(master, text="Supervised By Dr:Ahamed Al-Arashi",fg='black',font=('Times New Roman',12))
        self.Supervised.pack()
        self.Supervised.place(x=30,y=400)
        

##-------------------------------------Given The Name and The symptoms-------------------------------------
    def symptom(self, patient, indication):
        response = messagebox.askyesno("Symptom Check", f"Does {patient} have a {indication}?")
        return response




#--------------------------------Given The hypotheses-------------------------------------------
    def hypotheses(self, patient, disease):
        if disease == "measles":
            return self.symptom(patient, "fever") and self.symptom(patient, "cough") and \
                   self.symptom(patient, "conjunctivitis") and self.symptom(patient, "runny nose") and \
                   self.symptom(patient, "rash")
        elif disease == "german_measles":
            return self.symptom(patient, "fever") and self.symptom(patient, "headache") and \
                   self.symptom(patient, "runny nose") and self.symptom(patient, "rash")
        elif disease == "flu":
            return self.symptom(patient, "fever") and self.symptom(patient, "headache") and \
                   self.symptom(patient, "body ache") and self.symptom(patient, "conjunctivitis") and \
                   self.symptom(patient, "chills") and self.symptom(patient, "sore throat") and \
                   self.symptom(patient, "cough") and self.symptom(patient, "runny nose")
        elif disease == "common cold":
            return self.symptom(patient, "headache") and self.symptom(patient, "sneezing") and \
                   self.symptom(patient, "sore throat") and self.symptom(patient, "chills") and \
                   self.symptom(patient, "runny nose")
        elif disease == "mumps":
            return self.symptom(patient, "fever") and self.symptom(patient, "swollen glands")
        elif disease == "chicken pox":
            return self.symptom(patient, "fever") and self.symptom(patient, "rash") and \
                   self.symptom(patient, "body ache") and self.symptom(patient, "chills")
        elif disease == "whooping cough":
            return self.symptom(patient, "cough") and self.symptom(patient, "sneezing") and \
                   self.symptom(patient, "runny nose")
        else:
            return False


#--------------------------------Functions For Diagnosis-------------------------------------
    def start_diagnosis(self):
        patient = self.patient_name_entry.get()
        diseases = ["measles", "german_measles", "flu", "common cold", "mumps", "chicken pox", "whooping cough"]
        
        for disease in diseases:
            if self.hypotheses(patient, disease):
                self.result_label.config(text=f"{patient} probably has {disease.replace('_', ' ')}")
              #  self.show_photo(disease)
                return
        self.result_label.config(text="Sorry, I don’t seem to be able to diagnose the disease.")
        #self.photo_label.config(image='')
# #--------------------------------------Show the photo for disease-------------------
    # def show_photo(self, disease):
    # # Construct the image path based on the disease name
    #     photo_path = "C:/Users/Qursan/Desktop/MohammedNoman_202070363_AI/disease.png"

    #     try:
    #     # Print the path to debug
    #         print(f"Trying to load image from: {photo_path}")
    #         self.photo = tk.PhotoImage(file=photo_path)
    #         self.photo_label.config(image=self.photo)
    #         self.photo_label.image = self.photo  # Keep a reference to avoid garbage collection
    #     except Exception as e:
    #         messagebox.showerror("Error", f"Could not load image: {e}")




#----------------------------------GUI Setup-----------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('310x450+500+100')
    app = DiseaseDiagnosisApp(root)
    root.mainloop()