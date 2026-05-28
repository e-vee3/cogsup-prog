from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK

## global settings
exp = design.Experiment(
    name="Blindspot", 
    background_colour=C_WHITE,
    foreground_colour=C_BLACK
) 

control.set_develop_mode()
control.initialize(exp)

## stimuli
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

## experiment
def run_trial():

    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=(0, 0))
    fixation.preload()

    circle = make_circle(75)

    fixation.present()
    exp.clock.wait(500)

    circle.present()
    exp.keyboard.wait()

control.start(subject_id=1)

run_trial()
    
control.end()