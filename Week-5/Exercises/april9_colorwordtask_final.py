from expyriment import design, control, stimuli, misc

exp = design.Experiment(name="Block Experiment")

### avoid full screen mode and use a small window for development
control.set_develop_mode()
control.initialize(exp)

TRIAL_TYPES = ["match", "mismatch"]
COLORS = ["red", "green", "blue", "yellow"]

dict_colors = {
    "red": misc.constants.C_RED,
    "green": misc.constants.C_GREEN,
    "blue": misc.constants.C_BLUE,
    "yellow": misc.constants.C_YELLOW
}

# factorial block
factor_block = design.Block(name="Factorial Block")
factor_block.add_trials_full_factorial(
    {"trial_type": TRIAL_TYPES, "word": COLORS},
    copies=1
)
factor_block.shuffle_trials()

for trial in factor_block.trials:

    word = trial.get_factor("word")
    color = dict_colors[word]

    trial.add_stimulus(
        stimuli.TextLine(text=word, text_colour=color)
    )

    trial.preload_stimuli()

exp.add_block(factor_block)

#run - safe loop
control.start()

for block in exp.blocks:
    for trial in block.trials:
        trial.stimuli[0].present()
        exp.clock.wait(1000)

control.end()
