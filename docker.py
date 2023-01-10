from python_on_whales import docker
# from python_on_whales import DockerClient
#client = docker.from_env()
docker.image.pull('ssarkizova/hlathena-external', quiet=False)
docker.image.tag('ssarkizova/hlathena-external','hlathena')
returned_string = docker.run('hlathena',["predict","--help"])
print(returned_string)
print(docker.container.run('hlathena',["predict","--help"]))
#print(docker.container.run('hlathena', command=["-v", "`pwd`",":","`pwd`", "-w", "`pwd`", "ssarkizova/hlathena-external","predict", "--runID", "neo_pred", "--rundir", "./test_neo_pred/", "--peptides", 'modified_protein_file.txt', "--alleles", "A0101,A0103"]))
#print(docker.run('hlathena', command=["predict", "--runID", "neo_pred", "--rundir", "./test_neo/", "--peptides", "modified_protein_file.txt", "--alleles", "A0101"]))
print(docker.container.run('hlathena', command=["predict", "--runID", "neo_pred", "--rundir", "./test_neo/", "--peptides", 'sample_input_peptides.txt', "--alleles", "A0101"]))