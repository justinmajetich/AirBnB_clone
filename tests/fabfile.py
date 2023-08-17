from fabric import task

@task
def local(ctx):
    # Your task code here
    result = ctx.run('ls -l')
    print(result.stdout)
