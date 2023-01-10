import os
import docker
import json
from tqdm import tqdm
with open("hla_dict.json", "r") as file:
    hla_dict = json.load(file)
client = docker.from_env()
patient_list=list(hla_dict.keys())
for patient in tqdm(patient_list):
    patient_id = patient
    alleles = hla_dict[patient_id]
    alleles = ",".join(alleles)
    command = "predict --runID {} --rundir ./test_neo/ --peptides sample_input_peptides.txt --alleles {}".format(patient_id, alleles)
    client.containers.run(
        "ssarkizova/hlathena-external",
        command=command,
        volumes={os.getcwd(): {'bind': os.getcwd(), 'mode': 'rw'}},
        working_dir=os.getcwd(),
        stdin_open=True,
        tty=True
    )
