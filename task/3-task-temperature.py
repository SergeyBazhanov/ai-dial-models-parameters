from task.app.main import run

# TODO:
#  Try the `temperature` parameter that controls the randomness of the output. It's a parameter for balancing creativity
#        and determinism. Range: 0.0 to 2.0, Default: 1.0
#  User massage: Describe the sound that the color purple makes when it's angry

run(
    deployment_name='gpt-4o',
    print_only_content=True,
    temperature=0.7,  # Range 0.0-2.0 (try 0.0 for deterministic, 2.0 for very creative)
)