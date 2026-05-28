from expyriment import design, control, stimuli, misc

exp = expyriment.design.Experiment(name="First Experiment")
expyriment.control.initialize(exp)

### avoid full screen mode and use a small window for development
control.set_develop_mode()

TRIAL_TYPES = ["match", "mismatch"]
COLORS = ["red", "green", "blue", "orange"]
FACTORS = {"trial_type": TRIAL_TYPES, "word": COLORS}

dict_colors = {
    "red": "green",
    "green": "blue",
    "blue": "orange",
    "orange": "red"
}

block = design.Block("Block 1")
block.add_trials_full_factorial(FACTORS, copies=1)
block.shuffle_trials(method=0, max_repetition=None, n_segments=1)

#Deterministic block

block_one = expyriment.design.Block(name="Deterministic Block")

trial_one = expyriment.design.Trial()
stim = expyriment.stimuli.TextLine(text="I am a stimulus in Deterministic Block, Trial 1")
stim.preload()
trial_one.add_stimulus(stim)

trial_two = expyriment.design.Trial()
stim = expyriment.stimuli.TextLine(text="I am a stimulus in Deterministic Block, Trial 2")
stim.preload()
trial_two.add_stimulus(stim)

block_one.add_trial(trial_one)
block_one.add_trial(trial_two)
exp.add_block(block_one)

#factorial randomized block
block = design.Block

for trial in block.trials:
    trial_type = trial.get_factor("trial_type")
    word = trial.get_factor("word")

    color = word if trial_type == "match" else dict_colors[word]
    trial.set_factor("color", color)
    trial.set_factor("correct_key", ord(color[0]))

    trial.add_stimulus(stimuli.TextLine(word, text_colour=color))
    trial.preload_stimuli()

block_two = expyriment.design.Block(name="A name for the second block")
trial_one = expyriment.design.Trial()
stim = expyriment.stimuli.TextLine(text="I am a stimulus in Block 2, Trial 1")
stim.preload()
trial_one.add_stimulus(stim)
trial_two = expyriment.design.Trial()
stim = expyriment.stimuli.TextLine(text="I am a stimulus in Block 2, Trial 2")
stim.preload()
trial_two.add_stimulus(stim)
block_two.add_trial(trial_one)
block_two.add_trial(trial_two)
exp.add_block(block_two)


expyriment.control.start()

for block in exp.blocks:
    for trial in block.trials:
        trial.stimuli[0].present()
        exp.clock.wait(1000)

expyriment.control.end()