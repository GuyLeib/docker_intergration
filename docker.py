from python_on_whales import docker
# from python_on_whales import DockerClient
client = docker.from_env()
docker.image.pull('ssarkizova/hlathena-external', quiet=False)
docker.image.tag('ssarkizova/hlathena-external','hlathena')
# returned_string = docker.run('hlathena',["predict","-h"])
returned_string = docker.run('hlathena', command=["predict", "--runID", "test2", "--rundir", "./test/", "--peptides", "/home/dsi/leibguy/test/sample_input_peptides.txt", "--alleles", "A0101"])
print(returned_string)
