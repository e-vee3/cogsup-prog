from expyriment import design, control, stimuli, misc
import random

### this is a minimal example using expyriment for an experiment ###

#create an experiment object using "exp"

exp = design.Experiment(name= "Deterministic and Stochastic")

### avoid full screen mode and use a small window for development
control.set_develop_mode()

#initialize the experiment (this creates the window and prepares everything)
control.initialize(exp)

#define some constant for the experiment
STIMSIZE = 100 #size of the stimuli in pixels
GREY = misc.constants.C_GREY #a grey color for the stimulus
LATERAL_OFFSET = 200 #offset for lateral positioning

LEFT_KEY = misc.constants.K_LEFT
RIGHT_KEY = misc.constants.K_RIGHT

###The data headers##

exp.data_variable_names = [
    "block",
    "trial",
    "circle_position",
    "response",
    "rt",
    "accuracy"
]

### making your blocks ##

deterministic_block = design.Block(name="Deterministic")
stochastic_block = design.Block(name="Stochastic")

### the deterministic trials ##
for i in range(5):

    trial = design.Trial()

    square = stimuli.Rectangle(
        size=(STIMSIZE, STIMSIZE),
        colour=GREY,
        position=(-LATERAL_OFFSET, 0)
    )

    circle = stimuli.Circle(
        radius=STIMSIZE // 2,
        colour=GREY,
        position=(LATERAL_OFFSET, 0)
    )

    square.preload()
    circle.preload()

    trial.add_stimulus(square)
    trial.add_stimulus(circle)

    #saves condition information
    trial.set_factor("circle_position", "right")

    deterministic_block.add_trial(trial)

### Stochastic trials - circle will come randomly left or right

positions = ["left", "right"] * 5
random.shuffle(positions)

for pos in positions:

    trial = design.Trial()

    #determines positions
    if pos == "left":

        circle_pos = (-LATERAL_OFFSET, 0)
        square_pos = (LATERAL_OFFSET, 0)

    else:

        circle_pos = (LATERAL_OFFSET, 0)
        square_pos = (-LATERAL_OFFSET, 0)

    square = stimuli.Rectangle(
        size=(STIMSIZE, STIMSIZE),
        colour=GREY,
        position=square_pos
    )

    circle = stimuli.Circle(
        radius=STIMSIZE // 2,
        colour=GREY,
        position=circle_pos
    )

    square.preload()
    circle.preload()

    trial.add_stimulus(square)
    trial.add_stimulus(circle)

    #save
    trial.set_factor("circle_position", pos)

    stochastic_block.add_trial(trial)

### adding blocks to experiment

exp.add_block(deterministic_block)
exp.add_block(stochastic_block)

### start experiment

control.start(subject_id=1)

### run blocks

for block in exp.blocks:

    # block instruction screen
    instruction = stimuli.TextScreen(
        heading=f"{block.name} Block",
        text="Press LEFT key if the circle is on the LEFT.\n"
            "Press RIGHT key if the circle is on the RIGHT.\n\n"
            "Press any key to start, good luck!"
    )

    instruction.present()
    exp.keyboard.wait()

### run the trials

for trial_number, trial in enumerate(block.trials):

    #present both of the stimuli
    trial.stimuli[0].present(clear=True, update=False)
    trial.stimuli[1].present(clear=False, update=True)

    #collect the responses
    key, rt = exp.keyboard.wait(
        keys=[LEFT_KEY, RIGHT_KEY],
        duration=2000
    )

    #correct answer
    circle_position = trial.get_factor("circle_position")

    if circle_position == "left":
        correct_key = LEFT_KEY
    else:
        correct_key = RIGHT_KEY

    #determine accuracy
    if key is None:
        accuracy = "invalid"

    elif key == correct_key:
        accuracy = "correct"

    else:
        accuracy = "incorrect"

    #save data
    exp.data.add([
        block.name,
        trial_number + 1,
        circle_position,
        key,
        rt,
        accuracy
    ])

    #short pause between trials
    exp.clock.wait(500)

#end the experiment

control.end()