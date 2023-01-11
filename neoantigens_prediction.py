import os
import docker
import json
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor as Pool 

def predict(command_var):
    command = "predict --runID {} --rundir ./test_neo/ --peptides proteosome_output.txt --alleles {}".format(command_var[0], command_var[1])
    client.containers.run(
        "ssarkizova/hlathena-external",
        command=command,
        volumes={os.getcwd(): {'bind': os.getcwd(), 'mode': 'rw'}},
        working_dir=os.getcwd(),
        stdin_open=True,
        tty=True
    )


if __name__ == "__main__":     
    with open("hla_dict.json", "r") as file:
        hla_dict = json.load(file)
    client = docker.from_env()
    patient_list=list(hla_dict.keys())
    command_list=[]
    for patient_id in patient_list:
        alleles = hla_dict[patient_id]
        alleles = ",".join(alleles)
        command_list.append((patient_id,alleles))


    with Pool(max_workers=80) as pool:
        pool.map(predict,command_list)