def input_preprocess(input):
    inputs = input.split('\n')
    protagonist = inputs[0]
    characters = inputs[1]
    story = inputs[-1]
    return protagonist, characters, story

def prompt_preprocess(prompt):
    panels = prompt.split('\n\n')
    prompts = []
    for p in panels:
        prompts.append(p.split('>')[1].strip().replace("\n"," "))
    return prompts